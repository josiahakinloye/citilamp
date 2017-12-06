from django.conf.urls import url
from django.contrib import admin

from .views import (
	post_list,
	PostDetailView
	)

urlpatterns = [
	url(r'^$', post_list, name='list'),
    #url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/$', PostDetailView.as_view(), name='detail'),
]
