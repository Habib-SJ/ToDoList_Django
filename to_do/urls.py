from django.contrib import admin
from django.urls import path
from .views import home


appname = 'to_do'
urlpatterns = [
    path('', home),
]