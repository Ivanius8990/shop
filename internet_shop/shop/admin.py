from django.contrib import admin
from shop.models import *


class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')

admin.site.register(ShopProducts, ShopAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Category, CategoryAdmin)


class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Brand, CategoryAdmin)

# class BasketAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'cat','brand')
#     list_display_links = ('id', 'title')
#     search_fields = ('title', 'content')
#
# admin.site.register(Basket, BasketAdmin)
