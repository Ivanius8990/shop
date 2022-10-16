"""internet_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from shop.views import *

router = routers.SimpleRouter()
router.register(r'products', StoreViewSet)
print(router.urls)

urlpatterns = [
    path('', index,name='index'),
    path('store/', Store.as_view(),name='store'),
    path('api/v1/', include(router.urls)),
    path('product/<int:id>/', product, name='product'),
    path('checkout', checkout, name='checkout'),
    path('basket', basket, name='basket'),

]
