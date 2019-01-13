from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('article/(?P<article_id>[0-9]+)$', views.article_page,name='article_page'),
    path('edit/(?P<article_id>[0-9]+)$', views.edit_page,name='edit_page'),
    path('edit/Action$', views.edit_action,name='edit_action'),
]
