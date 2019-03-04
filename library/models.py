# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse 
from django.utils import timezone
import uuid 


class Category(models.Model):

    name = models.CharField(max_length=30)
    
    def get_absolute_url(self):
        return reverse('category-detail', args=[str(self.name)])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


## central model of library
## seperate model for category makes it easier to extend
## contributor is automatically populated when submitted by form
## still need to add additional fields (run as, kbas, etc.)
class Item(models.Model):

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
    category = models.ForeignKey('Category', default='Misc')
    subcategory = models.ManyToManyField('Category', related_name='subcategory', blank=True, default=category)
    text = models.TextField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    location = models.CharField(max_length=100, blank=True, null=True)
    run_as = models.CharField(max_length=35, default=IMHUSER, choices=RUN_AS)
    reviewed = models.BooleanField(default=False)
    #date reviewed = models.DateField(...)

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


## model for kbas related to script and command items
## would just be links to outside articles
## eventually maybe create seperate article model for internal kbas
class KBA(models.Model):
    
    url = models.CharField(max_length=250)
    category = models.ForeignKey('Category', default='Misc')
    title = models.CharField(max_length=100)
    reviewed = models.BooleanField(default=False)
    related_item = models.ForeignKey('Item', null=True)
    author = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
