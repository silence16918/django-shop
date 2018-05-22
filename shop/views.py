from django.shortcuts import render, redirect
from .models import Wheel, Nav, MustBuy, Shop, MainShow, FoodTypes, Goods, User, Cart, Order
from django.http import JsonResponse
import time
import random
from django.conf import settings
import os
from django.contrib.auth import logout

# Create your views here.


def index(request):
    return redirect("/main/")


# 主页
def main(request):
    # 获取轮播数据
    loopWheelList = Wheel.objects.all()
    # 获取导航数据
    navList = Nav.objects.all()
    # 每日必抢
    nav2List = MustBuy.objects.all()
    # 便利店数据
    shopList = Shop.objects.all()
    shop1 = shopList[0]
    shop2 = shopList[1:3]
    shop3 = shopList[3:7]
    shop4 = shopList[7:11]
    # 主要显示
    mainList = MainShow.objects.all()
    return render(request, 'home/main.html',
                  {"title": "首页",
                   "loopWheelList": loopWheelList,
                   "navList": navList,
                   "nav2List": nav2List,
                   "shop1": shop1,
                   "shop2": shop2,
                   "shop3": shop3,
                   "shop4": shop4,
                   "mainList": mainList}
                  )


# 闪送超市
def market(request, pageid, cid, sortid):
    # 左侧数据
    leftList = FoodTypes.objects.all()
    # 右侧数据
    if cid == '0':
        goodsList = Goods.objects.filter(categoryid=pageid)
    else:
        goodsList = Goods.objects.filter(categoryid=pageid, childcid=cid)

    # 排序goodsList
    if sortid == '0':
        pass
    elif sortid == '1':
        goodsList = goodsList.order_by("productnum")
    elif sortid == '2':
        goodsList = goodsList.order_by("price")
    elif sortid == '3':
        goodsList = goodsList.order_by("-price")

    # 子类名称
    fllist = []
    foodtype = FoodTypes.objects.get(typeid=pageid)
    allcname = foodtype.childtypenames
    # "全部分类:0#进口零食:103547#饼干糕点:103544#膨化食品:103543#坚果炒货:103542#肉干蜜饯:103546#糖果巧克力:103545"
    idnames = allcname.split("#")
    for str in idnames:
        arr = str.split(":")
        fllist.append({"code": arr[1], "title": arr[0]})

    titlelist = [{"title": "综合排序", "index": "0"},
                 {"title": "销量排序", "index": "1"},
                 {"title": "价格最低", "index": "2"},
                 {"title": "价格最高", "index": "3"}]

    return render(request, 'home/market.html',
                  {"title": "闪送超市",
                   "leftList": leftList,
                   "goodsList": goodsList,
                   "titlelist": titlelist,
                   "id": pageid,
                   "fllist": fllist}
                  )


# 购物车
def cart(request):
    token = request.session.get("token")
    cartslist = []
    trueNum = 0
    trueFlag = True
    if token == None:
        cartslist = []
    else:
        user = User.objects.get(userToken=token)
        userid = user.userAccount
        cards = Cart.object1.filter(userAccount=userid)
        for item in cards:
            if item.isChose:
                trueNum += 1
            cartslist.append(item)

    if trueNum != len(cartslist):
        trueFlag = False

    return render(request, 'home/cart.html',
                  {"title": "购物车",
                   "cartslist": cartslist,
                   "trueFlag": trueFlag}
                  )


#加入购物车
def changcart(request, flag):
    # 判断是否登录
    token = request.session.get("token")
    if token is None:
        return JsonResponse({"data": "0", "status": "error"})

    # 用户
    user = User.objects.get(userToken=token)
    # 用户id
    userid = user.userAccount
    # 商品id
    productid = request.POST.get("productid")
    # 商品信息
    product = Goods.objects.filter(productid=productid)[0]

    # 从购物车里取数据（用户id、商品id）
    carts = Cart.object1.filter(userAccount=userid, productid=productid)
    if carts.count() == 0:
        # 没有这样的数据
        onecart = Cart.createcart(userid, productid, 1, product.price, True, product.productimg, product.productlongname, False)
        onecart.save()
        return JsonResponse({"data": 1, "status": "success"})
    else:
        c = carts[0]
        if flag == '0':
            # 增加
            if product.storenums != 0:
                c.productnum = c.productnum + 1
                product.storenums -= 1
                newprice = float(product.price) * c.productnum
                newprice = "%.2f" % newprice
                c.productprice = newprice
                c.save()
                product.save()
        elif flag == '1':
            # 减少
            c.productnum = c.productnum - 1
            product.storenums += 1
            product.save()
            print(c.productnum)
            if c.productnum == 0:
                c.delete()
                return JsonResponse({"data": 0, "status": "success"})
            else:
                newprice = float(product.price) * c.productnum
                newprice = "%.2f" % newprice
                c.productprice = newprice
                c.save()
        elif flag == '2':
            c.isChose = not c.isChose
            c.save()
            if c.isChose:
                str = "√"
            else:
                str = ""
            return JsonResponse({"data": str, "status": "success"})

        return JsonResponse({"data": c.productnum, "status": "success"})


#订单
def saveorder(request):
    token = request.session.get("token")
    user = User.objects.get(userToken=token)
    carts = Cart.object1.filter(userAccount=user.userAccount)
    if carts.count() == 0:
        return JsonResponse({"data": 1, "status": "error"})

    cartorder = carts.filter(isChose=True)
    if cartorder.count() == 0:
        return JsonResponse({"data": 2, "status": "error"})

    orderid = time.time() + random.randrange(1, 100000)
    orderid = "%d" % orderid
    order = Order.createorder(orderid, user.userAccount, 0)
    order.save()
    for item in cartorder:
        item.orderid = orderid
        item.isDelete = True
        item.save()

    return JsonResponse({"data": 0, "status": "success"})



# 我的主页
def mine(request):
    username = request.session.get("username", "未登录")
    return render(request, 'home/mine.html', {"title": "我的", "username": username})


# 注册
def register(request):
    return render(request, 'home/register.html', {"title": "注册"})


# 保存用户
def saveuser(request):
    useraccunt = request.POST.get("userAccount")
    userPass = request.POST.get("userPass")
    userName = request.POST.get("userName")
    userPhone = request.POST.get("userPhone")
    userAdderss = request.POST.get("userAdderss")
    f = request.FILES["userImg"]
    fpath = os.path.join(settings.MDEIA_ROOT, useraccunt + ".png")
    with open(fpath, "wb") as pic:
        for data in f.chunks():
            pic.write(data)
    token = time.time() + random.randrange(1, 100000)
    token = "%f" % token
    user = User.createuser(useraccunt, userPass, userName, userPhone, userAdderss, fpath, 0, token)
    user.save()

    request.session["username"] = userName
    request.session["token"] = token

    # 重定向到mine
    return redirect("/mine/")


# 验证用户id是否可用
def checkuserid(request):
    userid = request.POST.get("checkid")
    try:
        user = User.objects.get(userAccount=userid)
    except User.DoesNotExist as e:
        # 没找到用户说明可以注册
        return JsonResponse({"data": 0, "status": "success"})
    # 找到用户说明不可以注册
    return JsonResponse({"data": 0, "status": "error"})


# 退出
def quit(request):
    logout(request)
    return redirect("/mine/")


# 登录
def login(request):
    return render(request, 'home/login.html', {"title": "登陆"})


# 检查登录
def checkuserlogin(request):
    useraccunt = request.POST.get("ua")
    userpasswd = request.POST.get("up")

    try:
        user = User.objects.get(userAccount=useraccunt)
    except User.DoesNotExist as e:
        return JsonResponse({"data": 0, "status": "error"})

    if userpasswd != user.userPasswd:
        return JsonResponse({"data": 0, "status": "error"})

    request.session["username"] = user.userName
    request.session["token"] = user.userToken
    return JsonResponse({"data": 0, "status": "success"})
