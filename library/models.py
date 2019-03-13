# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse 
from django.utils import timezone
import uuid 


class ItemType(models.Model):

    name = models.CharField(max_length=35)

    def get_absolute_url(self):
        return reverse('type-detail', args=[str(self.name)])

    def __str__(self):
        return self.name


class ItemLanguage(models.Model):

    name = models.CharField(max_length=35)

    def get_absolute_url(self):
        return reverse('language-detail', args=[str(self.name)])

    def __str__(self):
        return self.name


class Category(models.Model):

    name = models.CharField(max_length=35)
    
    def get_absolute_url(self):
        return reverse('category-detail', args=[str(self.name)])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Item(models.Model):

    """

    basic model for scripts, commands, etc in library
    type, category, and language models 
    contributor is automatically populated when submitted by form

    """

    USER = 'User'
    IMHUSER = 'IMH-User'
    ROOT = 'Root'
    T1A = 'T1A'
    T1E = 'T1E'

    RUN_AS = (
            (USER, 'User'),
            (IMHUSER, 'IMH-User'),
            (ROOT, 'Root'),
            (T1A, 'Tier1Adv'),
            (T1E, 'T1e'),
            )

    name = models.CharField(max_length=100)
    contributor = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', blank=True, null=True)
    subcategory = models.ManyToManyField('Category', related_name='subcategory', blank=True, default=category)
    item_type = models.ForeignKey('ItemType', blank=True, null=True, on_delete=models.SET_NULL)
    language = models.ForeignKey('ItemLanguage', blank=True, null=True, on_delete=models.SET_NULL)
    text = models.TextField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    location = models.CharField(max_length=100, blank=True, null=True)
    run_as = models.CharField(max_length=35, default=IMHUSER, choices=RUN_AS)
    reviewed = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('item-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


## extension of django.contrib.auth built in User model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    saved = models.ManyToManyField('Item')
    is_t1e = models.BooleanField(default=False)

    def __str__(self):
        return self.user.get_username()


class KBA(models.Model):
    
    """

    model for kbas related to script and command items
    would just be links to outside articles
    eventually maybe create seperate article model for internal kbas

    """

    url = models.CharField(max_length=250)
    category = models.ForeignKey('Category', blank=True, null=True)
    title = models.CharField(max_length=100)
    reviewed = models.BooleanField(default=False)
    related_item = models.ManyToManyField('Item')
    author = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
