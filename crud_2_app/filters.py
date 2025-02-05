from cProfile import label

import django_filters
from django import forms
from django.db.models import CharField
from django_filters import CharFilter
from unicodedata import lookup

from crud_2_app.models import product


class BrandFilter(django_filters.FilterSet):
    brand = CharFilter(label="",lookup_expr='icontains',widget = forms.TextInput(attrs={'placeholder': 'search brand', 'class': 'form-control'}))
    class Meta:
        model = product
        fields = ['brand',]

class SellerFilter(django_filters.FilterSet):
    product_user__name = CharFilter(label="",lookup_expr='icontains',widget = forms.TextInput(attrs={'placeholder': 'search seller', 'class': 'form-control'}))

    class Meta:
        model = product
        fields = ['product_user__name', ]

#

