import django_filters
from .models import Property




class PropertyFilter(django_filters.FilterSet):
    '''
    Customize filter to be case insensitive
    '''
    size__lte = django_filters.NumberFilter(field_name="size", lookup_expr="lte")
    size__gte = django_filters.NumberFilter(field_name="size", lookup_expr="gte")
    type = django_filters.CharFilter(field_name="type", lookup_expr="icontains")
    
    class Meta:
        model = Property
        fields = ['size__lte', 'size__gte', 'type', 'actions']