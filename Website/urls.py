from django.contrib import admin
from django.urls import path, include
from Website import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('websitedetail', views.websitedetail, name='websitedetail'),
    path('marketplace', views.marketplace, name='marketplace'),
    path('selltype', views.selltype, name='selltype'),
    path('sellwebsite', views.sellwebsite, name='sellwebsite'),
    path('sell', views.sell, name='sell'),
    path('sell2', views.sell2, name='sell2'),
]