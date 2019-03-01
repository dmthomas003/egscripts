# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from library.models import Item, Category
from django.contrib import admin

# Register your models here.


class ItemInline(admin.TabularInline):
    model = Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'reviewed')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
#need to set custom name for categories field, currently "categorys"
