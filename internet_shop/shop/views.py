from django.shortcuts import render
from django.views.generic import ListView
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from shop.forms import UsersForm
from shop.models import *
from shop.serializers import ShopProductSerializer

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


class StoreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset =ShopProducts.objects.all()
    serializer_class = ShopProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'cat': ['in','exact'],
        'brand': ['in', 'exact']
    }
    @action(methods=['get'], detail=False)
    def category(self, request):
        data = list(Category.objects.values())
        return JsonResponse(data, safe=False)
    @action(methods=['get'], detail=False)
    def brand(self, request):
        data = list(Brand.objects.values())
        return JsonResponse(data, safe=False)


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
    print(data)
    del_item=data.get('del_item')
    if del_item:
        Basket.objects.filter(session_key=session_key, id=del_item).delete()
    else:
        numb = data.get('numb')
        prod_id = data.get('id')
        title = ShopProducts.objects.values('title').get(pk=prod_id)['title']
        prise_item = ShopProducts.objects.values('prise').get(pk=prod_id)['prise']
        Basket.objects.update_or_create(session_key=session_key,prod_id=prod_id,numb=numb,title=title,prise_item=prise_item)
        return JsonResponse(return_dict)

