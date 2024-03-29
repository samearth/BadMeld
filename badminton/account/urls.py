"""badminton URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.register , name='register'),
    path('login/', views.login ,name='login'),
    path('',views.index , name='index'),
    path('home/',views.home , name='home'),
    path('logout/',views.logouts,name='logouts'),
    path('profile/',views.profile,name='profile'),
    path('about/' , views.about , name='about'),
    path('issue/' , views.add_inventory, name="issue"),
    path('updatei',views.update_inventory, name="updatei"),
    path('issue1/',views.issue , name="issue1"),
    path('complaints/',views.complaints , name="complaints"),
    path('blog/', views.blog , name="blog"),
    path('current-data/' , views.scraped , name="current_data"),
    path('sell/' , views.sell , name="sell"),
    path('shop/' , views.shop , name = "shop")
]