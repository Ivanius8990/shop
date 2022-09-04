from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render

from internet_shop import settings
from internet_shop.settings import MEDIA_ROOT, MEDIA_URL
from shop.forms import UsersForm
from shop.models import *

menu = [{"title": "Домашняя", 'url_name': 'index'},
        {"title": "Горячие предложения", 'url_name': 'index'},
        {"title": "Категории", 'url_name': 'store'},
        {"title": "Ноутбуки", 'url_name': 'index'},
        {"title": "Смартфоны", 'url_name': 'index'},
        {"title": "Камеры", 'url_name': 'index'},
        {"title": "Аксессуары", 'url_name': 'index'}, ]


def index(request):
    context = {
        'menu': menu,
        'title': 'главная страница'
    }
    return render(request, 'shop/index.html', context=context)


def store(request):
    if request.method == 'GET':
        posts = ShopProducts.objects.all()
        context = {
            'menu': menu,
            'title': 'главная страница',
            'posts': posts,
        }
        return render(request, 'shop/store.html', context=context, )
    else:
        prise_max = request.POST.get('price-max')
        prise_min = request.POST.get('price-min')
        print(prise_min, prise_max)

        checked_cats = request.POST.getlist('cat_inputs')
        checked_cats = list(map(int, checked_cats))

        checked_brands = request.POST.getlist('brand_inputs')
        checked_brands = list(map(int, checked_brands))

        if len(checked_cats) != 0 and len(checked_brands) == 0:
            posts = ShopProducts.objects.filter(cat__in=checked_cats,prise__gte=prise_min,prise__lte=prise_max)
        elif len(checked_cats) == 0 and len(checked_brands) != 0:
            posts = ShopProducts.objects.filter(brand__in=checked_brands,prise__gte=prise_min,prise__lte=prise_max)
        elif len(checked_cats) != 0 and len(checked_brands) != 0:
            posts = ShopProducts.objects.filter(brand__in=checked_brands, cat__in=checked_cats,prise__gte=prise_min,prise__lte=prise_max)
        else:
            posts = ShopProducts.objects.filter(prise__gte=prise_min,prise__lte=prise_max)
        context = {
            'menu': menu,
            'title': 'главная страница',
            'posts': posts,
            'checked_cats': checked_cats,
            'checked_brands': checked_brands
        }
        return render(request, 'shop/store.html', context=context, )


def product(request, id):
    post = ShopProducts.objects.get(pk=id)
    context = {
        'menu': menu,
        'title': 'главная страница',
        'post': post,
    }
    return render(request, 'shop/product.html', context=context, )


def checkout(request):
    form=UsersForm
    context = {
        'form': form,
      }
    return render(request, 'shop/checkout.html', context=context,)
