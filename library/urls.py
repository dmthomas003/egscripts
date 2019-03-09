from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.userprofile, name='userprofile-detail'),
        url(r'^userprofile/$', views.userprofile, name='userprofile-detail'),
        url(r'^category/(?P<slug>[^/]+)$', views.CategoryDetailView.as_view(), name='category-detail'),
        url(r'items/$', views.ItemListView.as_view(), name='items'),
        url(r'^item/(?P<pk>\d+)$', views.ItemDetailView.as_view(), name='item-detail'),
        url(r'^types/$', views.TypeListView.as_view(), name='types'),
        url(r'^languages/$', views.LanguageListView.as_view(), name='languages')
        ]
