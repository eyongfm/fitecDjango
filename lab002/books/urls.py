from django.contrib import admin
from django.urls import include, re_path
from django.urls import path

from lab002.books import views

urlpatterns = [
    re_path(r'^api/books$', views.books_list),
]

