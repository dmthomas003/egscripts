from django.test import TestCase
from library.models import Item, Category, UserProfile, FavoritesList
from django.contrib.auth.models import User, Group, Permission
from django.utils import timezone
from django.core.urlresolvers import reverse


class CategoryTest(TestCase):

    def create_category(self):
        name='Misc'

        return Category.objects.create(name=name)

    def test_category_creation(self):
        c = self.create_category()
        self.assertTrue(isinstance(c, Category))


class ItemTest(TestCase):

    def create_category(self):
        name='Misc'

        return Category.objects.create(name=name)

    def create_item(self):
        name = 'test_item00'
        text = 'test item 00'
        category = self.create_category()
        description = 'description of test item 00'
        reviewed = True

        return Item.objects.create(name=name, category=category, text=text, description=description, reviewed=reviewed)

    def test_item_creation(self):
        i = self.create_item()
        self.assertTrue(isinstance(i, Item))


class UserProfileTest(TestCase):

    def create_category(self)

    def create_user(self):
        username = 'testuser'

    def create_favoriteslist(self):

