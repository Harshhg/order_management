"""order-management-backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from rest_framework.routers import DefaultRouter

from order_management.orders.views import OrderViewSet
from order_management.users.views import AuthViewSet

default_router = DefaultRouter(trailing_slash=False)
default_router.register('api/auth', AuthViewSet, basename='login')
default_router.register('api/order', OrderViewSet, basename='orders')


urlpatterns = [
    path('admin/', admin.site.urls)
] + default_router.urls



