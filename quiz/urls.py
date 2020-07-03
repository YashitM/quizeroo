from django.conf.urls import url
from django.contrib import admin
from quiz import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^play/(?P<category_id>[0-9]+)/$', views.play, name='play'),
]