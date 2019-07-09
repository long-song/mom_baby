from django.contrib import admin
from django.urls import path
from store import views

urlpatterns = [
    path('index/', views.index),   # 访问首页路由
    path('login/', views.login),   # 访问登录路由
]