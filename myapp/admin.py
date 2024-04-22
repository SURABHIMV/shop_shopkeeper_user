from django.contrib import admin
from .models import shop,shopkeeper,shop_user,added_shopkeeper,product
# Register your models here.

class shop_Admin(admin.ModelAdmin):
    list_display = ['shop_Name']
admin.site.register(shop,shop_Admin)

class shopkeeper_Admin(admin.ModelAdmin):
    list_display = ['shopkeeper_Name']
admin.site.register(shopkeeper,shopkeeper_Admin)

class user_Admin(admin.ModelAdmin):
    list_display = ['user_Name']
admin.site.register(shop_user,user_Admin)

class addedshopkeeper_Admin(admin.ModelAdmin):
    list_display = ['addedshopkeeper_Name']
admin.site.register(added_shopkeeper,addedshopkeeper_Admin)


class product_Admin(admin.ModelAdmin):
    list_display = ['product_Name','product_Quantity']
admin.site.register(product,product_Admin)