
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('app01.urls', namespace='app01')),
]
