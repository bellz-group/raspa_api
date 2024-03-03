import django_filters
from .models import DevelopedProperty


class DevdPropertyFilter(django_filters.FilterSet):
    '''
    Customize filter to be case insentitive
    '''
    size = django_filters.CharFilter(field_name="property_name", lookup_expr="icontains")
    type = django_filters.CharFilter(field_name="type", lookup_expr="icontains")
    bdrs = django_filters.CharFilter(field_name="bdrs", lookup_expr="icontains")
    flrs = django_filters.CharFilter(field_name="flrs", lookup_expr="icontains")


    class Meta:
        model = DevelopedProperty
        fields = ['size', 'type', 'bdrs', 'flrs']
