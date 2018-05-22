from django.conf.urls import url

from . import views

urlpatterns = [
    # 主页
    url(r'^main/$', views.main, name='main'),

    # 闪送超市/主分类/子分类/排序规则/
    url(r'^market/(\d+)/(\d+)/(\d+)/$', views.market, name='market'),
    # 购物车
    url(r'^cart/$', views.cart, name='cart'),
    # 修改购物车(添加、删除、修改是否选中)
    url(r'^changcart/(\d+)/$', views.changcart),
    # 提交订单
    url(r'^saveorder/$', views.saveorder),

    # 我的
    url(r'^mine/$', views.mine, name='mine'),
    # 注册
    url(r'^register/$', views.register),
    # 保存用户
    url(r'^saveuser/$', views.saveuser),
    # 验证用户id是否可用
    url(r'^checkuserid/$', views.checkuserid),
    # 退出登陆
    url(r'^quit/$', views.quit),
    # 登陆
    url(r'^login/$', views.login),
    # 验证用户登录
    url(r'^checkuserlogin/$', views.checkuserlogin),

]
