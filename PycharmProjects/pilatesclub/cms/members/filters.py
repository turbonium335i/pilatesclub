import django_filters
from django.db.models import Q
from .models import *

class memberFilter(django_filters.FilterSet):
    class Meta:
        model = client
        fields = {
            'name': ['icontains'],
            'phone': ['icontains'],
            'comments': ['icontains'],
        }

class UserFilter(django_filters.FilterSet):
    multi_name_fields = django_filters.CharFilter(method='filter_by_all_name_fields', label='Name, Comment, Phone')

    class Meta:
        model = client
        fields = []

    def filter_by_all_name_fields(self, queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value) | Q(phone__icontains=value) | Q(comments__icontains=value)
        )