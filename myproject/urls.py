"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from myapp import views
urlpatterns = [   
    path('admin/', admin.site.urls),
    path('signup_shop/',views.signupPage_shop,name='signup_shop'),
    path('login_shop/',views.loginPage_shop,name='login_shop'),
    path('signup_shopkeeper/',views.signupPage_shopkeeper,name='signup_shopkeeper'),
    path('login_shopkeeper/',views.loginPage_shopkeeper,name='login_shopkeeper'),
    path('signup_user/',views.signupPage_user,name='signup_user'),
    path('login_user/',views.loginPage_user,name='login_user'),
    path('shop_dashboard/',views.shopkeeper_data,name='shop_dashboard'),
    path('user_dashboard/',views.user,name='user_dashboard')
]
