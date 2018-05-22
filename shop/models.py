from django.db import models


# Create your models here.

# 轮播
class Wheel(models.Model):
    img = models.CharField(max_length=150)
    name = models.CharField(max_length=20)
    trackid = models.CharField(max_length=10)


# 导航
class Nav(models.Model):
    img = models.CharField(max_length=150)
    name = models.CharField(max_length=20)
    trackid = models.CharField(max_length=10)


# 每日必抢模型类
class MustBuy(models.Model):
    img = models.CharField(max_length=100)
    name = models.CharField(max_length=20)
    trackid = models.CharField(max_length=10)


# 便利店数据模型类
class Shop(models.Model):
    img = models.CharField(max_length=100)
    name = models.CharField(max_length=20)
    pd = models.CharField(max_length=10)


#主体
class MainShow(models.Model):
    trackid = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    img = models.CharField(max_length=100)
    categoryid = models.CharField(max_length=10)
    brandname = models.CharField(max_length=20)

    img1 = models.CharField(max_length=100)
    childcid1 = models.CharField(max_length=10)
    productid1 = models.CharField(max_length=10)
    longname1 = models.CharField(max_length=50)
    price1 = models.CharField(max_length=10)
    marketprice1 = models.CharField(max_length=10)

    img2 = models.CharField(max_length=100)
    childcid2 = models.CharField(max_length=10)
    productid2 = models.CharField(max_length=10)
    longname2 = models.CharField(max_length=50)
    price2 = models.CharField(max_length=10)
    marketprice2 = models.CharField(max_length=10)

    img3 = models.CharField(max_length=100)
    childcid3 = models.CharField(max_length=10)
    productid3 = models.CharField(max_length=10)
    longname3 = models.CharField(max_length=50)
    price3 = models.CharField(max_length=10)
    marketprice3 = models.CharField(max_length=10)


#类型
class FoodTypes(models.Model):
    typeid = models.CharField(max_length=10)
    typename = models.CharField(max_length=20)
    typesort = models.IntegerField()
    childtypenames = models.CharField(max_length=150)


# 商品模型类
class Goods(models.Model):
    # 商品id
    productid = models.CharField(max_length=10)
    # 商品图片
    productimg = models.CharField(max_length=150)
    # 商品名称
    productname = models.CharField(max_length=50)
    # 商品长名称
    productlongname = models.CharField(max_length=100)
    # 是否精选
    isxf = models.NullBooleanField(default=False)
    # 是否买一赠一
    pmdesc = models.CharField(max_length=10)
    # 规格
    specifics = models.CharField(max_length=20)
    # 价格
    price = models.CharField(max_length=10)
    # 超市价格
    marketprice = models.CharField(max_length=10)
    # 组id
    categoryid = models.CharField(max_length=10)
    # 子类组id
    childcid = models.CharField(max_length=10)
    # 子类组名称
    childcidname = models.CharField(max_length=10)
    # 详情页id
    dealerid = models.CharField(max_length=10)
    # 库存
    storenums = models.IntegerField()
    # 销量
    productnum = models.IntegerField()


# 用户模型类
class User(models.Model):
    # 用户账号，要唯一
    userAccount = models.CharField(max_length=20, unique=True)
    # 密码
    userPasswd = models.CharField(max_length=20)
    # 昵称
    userName = models.CharField(max_length=20)
    # 手机号
    userPhone = models.CharField(max_length=20)
    # 地址
    userAdderss = models.CharField(max_length=100)
    # 头像路径
    userImg = models.CharField(max_length=150)
    # 等级
    userRank = models.IntegerField()
    # touken验证值，每次登陆之后都会更新
    userToken = models.CharField(max_length=50)

    @classmethod
    def createuser(cls, account, passwd, name, phone, address, img, rank, token):
        u = cls(userAccount=account, userPasswd=passwd, userName=name, userPhone=phone, userAdderss=address,
                userImg=img, userRank=rank, userToken=token)
        return u


# 购物车表
class CartManager1(models.Manager):
    def get_queryset(self):
        return super(CartManager1, self).get_queryset().filter(isDelete=False)


class CartManager2(models.Manager):
    def get_queryset(self):
        return super(CartManager2, self).get_queryset().filter(isDelete=True)


#购物车
class Cart(models.Model):
    userAccount = models.CharField(max_length=20)
    productid = models.CharField(max_length=10)
    productnum = models.IntegerField()
    productprice = models.CharField(max_length=10)
    isChose = models.BooleanField(default=True)
    productimg = models.CharField(max_length=150)
    productname = models.CharField(max_length=100)
    orderid = models.CharField(max_length=20, default="0")
    isDelete = models.BooleanField(default=False)
    object1 = CartManager1()
    object2 = CartManager2()

    @classmethod
    def createcart(cls, userAccount, productid, productnum, productprice, isChose, productimg, productname, isDelete):
        c = cls(userAccount=userAccount, productid=productid, productnum=productnum, productprice=productprice,
                isChose=isChose, productimg=productimg, productname=productname, isDelete=isDelete)
        return c


# 订单
class Order(models.Model):
    orderid = models.CharField(max_length=20)
    userid = models.CharField(max_length=20)
    progress = models.IntegerField()

    @classmethod
    def createorder(cls, orderid, userid, progress):
        o = cls(orderid=orderid, userid=userid, progress=progress)
        return o
