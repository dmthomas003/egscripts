# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from library.models import Item, Category, UserProfile
from library.forms import ContributionForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, Group


@login_required
def index(request):

    """

    eliminate 

    should be basic landing page but currently stats page
    the contents of this index function view should be moved
    to the sidebar

    """

    num_scripts = Item.objects.filter(reviewed=True).count()
    newest = Item.objects.filter(reviewed=True)[::-1][:5]
    #5 most used

    context = {
        'num_scripts': num_scripts,
        #'num_contributors': num_contributors,
        'newest': newest,
        }

    if Group.objects.filter(name='Contributor'):
        contributors = Group.objects.get(name='Contributor')
        num_contributors = contributors.user_set.count()
        context['num_contributors'] = num_contributors

    return render(request, 'library/index.html', context=context)


@login_required
def userprofile(request):

    """

    main view for logged in user

    includes contribution form if user is a member of 
    contributor group and a list of pending and reviewed
    items

    need to add saved list

    need to remove redundancies in context objects and template

    """

    username = request.user.get_username()
    if UserProfile.objects.filter(user=request.user):
        profile = UserProfile.objects.get(user=request.user)
    else:
        UserProfile.objects.create(
            user=request.user
            )
        profile = UserProfile.objects.get(user=request.user)
    #join_date = request.user.date_joined
    #last_login = request.user.last_login
    contributions = Item.objects.filter(reviewed=True).filter(contributor=request.user)
    total_contributions = contributions.count()
    pending_contributions = Item.objects.filter(reviewed=False).filter(contributor=request.user)
    pending_count = pending_contributions.count()

    ## form to contribute new item
    ## is added to pending list until reviewed by admin 
    if request.method == 'POST':
        contribution_form = ContributionForm(request.POST)
        if contribution_form.is_valid():
            item = Item.objects.create(
                name = contribution_form.cleaned_data.get('name'),
                contributor = request.user,
                category = contribution_form.cleaned_data.get('category'),
                text = contribution_form.cleaned_data.get('text'),
                description = contribution_form.cleaned_data.get('description'),
                location = contribution_form.cleaned_data.get('location'),
                )
            return HttpResponseRedirect(reverse('userprofile-detail'))
    else:
        contribution_form = ContributionForm()
    context = {
            'username': username,
            'contributions': contributions,
            'total_contributions': total_contributions,
            'pending_contributions': pending_contributions,
            'pending_count': pending_count,
            'contribution_form': contribution_form,
            #'join_date': join_date,
            #'last_login': last_login,
            }

    return render(request, 'library/userprofile.html', context=context)


class CategoryListView(LoginRequiredMixin, generic.ListView):
    template_name = 'library/categories.html'
    model = Category


class CategoryDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'library/category.html'
    model = Category
    slug_field = 'name'


class ItemListView(LoginRequiredMixin, generic.ListView):
    template_name = 'library/items.html'
    model = Item


class ItemDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'library/item.html'
    model = Item


"""
class ContributorListView(LoginRequiredMixin, generic.ListView):
    template_name = 'library/contributors.html'
    model = Contributor


class ContributorDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'library/contributor.html'
    model = Contributor
    slug_field = 'username'
"""
