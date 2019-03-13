# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from library.models import Item, Category, UserProfile, ItemType, ItemLanguage
from django.contrib import admin

# Register your models here.


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'reviewed')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_t1e']


class ItemTypeAdmin(admin.ModelAdmin):
    list_display = ['name']


class ItemLanguageAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(ItemType, ItemTypeAdmin)
admin.site.register(ItemLanguage, ItemLanguageAdmin)
