from django.contrib import admin

# Register your models here.

from .models import User, Cart


# 用户表
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    def userAccount(self):
        return self.userAccount

    userAccount.short_description = "用户id"

    def userName(self):
        return self.userName

    userName.short_description = "用户昵称"

    def userPhone(self):
        return self.userPhone

    userPhone.short_description = "手机号码"

    def userAdderss(self):
        return self.userAdderss

    userAdderss.short_description = "地址"

    def userRank(self):
        return self.userRank

    userRank.short_description = "等级"
    list_display = ["pk", userAccount, userName, userPhone, userAdderss, userRank]
    list_per_page = 10


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_filter = ["userAccount"]
    list_display = ["pk", "userAccount", "productid", "productnum", "productprice", "isChose", "productimg",
                    "productname", "orderid", "isDelete"]
    list_per_page = 10
