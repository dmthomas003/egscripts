from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$',views.userprofile, name='userprofile-detail'),
        url(r'^categories/', views.CategoryListView.as_view(), name='categories'),
        url(r'^category/(?P<slug>[^/]+)$', views.CategoryDetailView.as_view(), name='category-detail'),
        url(r'items/$', views.ItemListView.as_view(), name='items'),
        url(r'^item/(?P<pk>\d+)$', views.ItemDetailView.as_view(), name='item-detail'),
        #url(r'^contributors/', views.ContributorListView.as_view(), name='contributors'),
        #url(r'^contributor/(?P<slug>[^/]+)$', views.ContributorDetailView.as_view(), name='contributor-detail'),
        #url(r'^userprofile/$', views.userprofile, name='userprofile-detail'),
        ]
