import django_filters
from .models import Property, PropertyListing




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



class PropertyListingFilter(django_filters.FilterSet):
    '''
    Customize filter to be case insensitive
    '''
    price__lte = django_filters.NumberFilter(field_name="price", lookup_expr="lte")
    price__gte = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    
    class Meta:
        model = PropertyListing
        fields = [
                    "price__lte","price__gte", "listing_type", 
                    "property__features__name", "property__type",
                    "property__size", 
                    "property__features__count", "property__features"
                    ]
        

