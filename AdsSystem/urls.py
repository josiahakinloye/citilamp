from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^newAd$', views.new_ad, name='new_ad')
]