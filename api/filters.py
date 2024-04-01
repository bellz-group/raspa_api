import django_filters
from .models import DevelopedProperty




class DevdPropertyFilter(django_filters.FilterSet):
    '''
    Customize filter to be case insensitive
    '''
    size__lte = django_filters.NumberFilter(field_name="size", lookup_expr="lte")
    size__gte = django_filters.NumberFilter(field_name="size", lookup_expr="gte")
    type = django_filters.CharFilter(field_name="type", lookup_expr="icontains")
    # bdrs__lte = django_filters.NumberFilter(field_name="bdrs", lookup_expr="lte")
    # bdrs__gte = django_filters.NumberFilter(field_name="bdrs", lookup_expr="gte")
    # flrs__lte = django_filters.NumberFilter(field_name="flrs", lookup_expr="lte")
    # flrs__gte = django_filters.NumberFilter(field_name="flrs", lookup_expr="gte")

    class Meta:
        model = DevelopedProperty
        fields = ['size__lte', 'size__gte', 'type', 'actions']