from django import template
from django.db.models import Count

from shop.models import *

register = template.Library()


@register.simple_tag
def get_categories():
    return Category.objects.all()


@register.simple_tag
def cat_product_count():
    return Category.objects.annotate(Count('shopproducts'))


@register.simple_tag
def get_brand():
    return Brand.objects.all()


@register.simple_tag
def brand_product_count():
    return Brand.objects.annotate(Count('shopproducts'))


@register.simple_tag
def raiting_count(rait):
    return range(rait)


