from urllib import request

from django.db.models import Count
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.http import JsonResponse
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


class Store(ListView):
    model = ShopProducts
    template_name = 'shop/store.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context


# def store(request):
#     if request.method == 'GET':
#         posts = ShopProducts.objects.all()
#         context = {
#             'menu': menu,
#             'title': 'главная страница',
#             'posts': posts,
#         }
#         return render(request, 'shop/store.html', context=context, )
#         posts = ShopProducts.objects.all()
#         context = {
#             'menu': menu,
#             'title': 'главная страница',
#             'posts': posts,
#         }
#         return render(request, 'shop/store.html', context=context, )
#     else:
#         price_max = request.POST.get('price-max')
#         price_min = request.POST.get('price-min')
#         print(price_min, price_max)
#
#         checked_cats = request.POST.getlist('cat_inputs')
#         checked_cats = list(map(int, checked_cats))
#
#         checked_brands = request.POST.getlist('brand_inputs')
#         checked_brands = list(map(int, checked_brands))
#
#         if len(checked_cats) != 0 and len(checked_brands) == 0:
#             posts = ShopProducts.objects.filter(cat__in=checked_cats,price__gte=price_min,prise__lte=prise_max)
#         elif len(checked_cats) == 0 and len(checked_brands) != 0:
#             posts = ShopProducts.objects.filter(brand__in=checked_brands,prise__gte=prise_min,prise__lte=prise_max)
#         elif len(checked_cats) != 0 and len(checked_brands) != 0:
#             posts = ShopProducts.objects.filter(brand__in=checked_brands, cat__in=checked_cats,prise__gte=prise_min,prise__lte=prise_max)
#         else:
#             posts = ShopProducts.objects.filter(prise__gte=prise_min,prise__lte=prise_max)
#         context = {
#             'menu': menu,
#             'title': 'главная страница',
#             'posts': posts,
#             'checked_cats': checked_cats,
#             'checked_brands': checked_brands
#         }
#         return render(request, 'shop/store.html', context=context, )


def checkbox_filters(request):
    """Проверка доступности логина"""
    categories = request.GET.get('categories', None)
    brands = request.GET.get('brands', None)
    print(categories)
    print(brands)
    # print(Books.objects.filter(name=name).exists())
    response = {
        'categories': categories,
        'brands': brands
    }
    print(response)
    return JsonResponse(response)


def product(request, id):
    post = ShopProducts.objects.get(pk=id)
    # session_key = request.session.session_key
    # if not session_key:
    #     request.session.cycle_key()
    # print(request.session.session_key)
    context = {
        'menu': menu,
        'title': 'главная страница',
        'post': post,
    }
    return render(request, 'shop/product.html', context=context, )


def checkout(request):
    form = UsersForm
    context = {
        'form': form,
    }
    return render(request, 'shop/checkout.html', context=context, )


def basket(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    return_dict = {}
    data = request.POST
    numb = data.get('numb')
    prod_id = data.get('id')

    Basket.objects.create(session_key=session_key,prod_id=prod_id,numb=numb)
    total_prod = Basket.objects.filter(session_key=session_key).count()
    return_dict['total_prod'] = total_prod
    print(prod_id)
    print(numb)
    print(return_dict)
    # ff=Basket.objects.get(pk=1)
    # aa=ff.products.prise
    # print(aa)
    return JsonResponse(return_dict)
