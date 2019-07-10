from django.contrib import admin
from django.urls import path
from store import views

urlpatterns = [
    path('index/', views.index , name='index'),   # 访问首页路由
    path('login/', views.login, name='login'),   # 访问登录路由
    path('list/', views.list, name='list'),   # 访问商品列表路由
    path('buytoday/', views.buytoday, name='buytoday'),   # 访问今日团购路由
    path('information/', views.information, name='information'),   # 访问母婴资讯路由
    path('about/', views.about, name='about'),   # 访问关于我们路由
    path('shopcart/', views.shopcart, name='shopcart'),   # 访问购物车路由
    path('details/', views.details, name='details'),   # 访问产品详情路由
    path('add/', views.add),   # 访问产品详情路由
]