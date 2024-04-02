from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from api.filters import PropertyFilter 
from .models import *
from .serializers import *
from rest_framework import filters, viewsets, status, permissions
from django.db.models import Q

class Index(APIView):
    def get(self, request, format=None):
        return Response(
            {
                "message": "This is the index route of the RASPA API",
                "developer": "Olaniyi George"
            })


class PropertyListCreateViewSet(generics.ListCreateAPIView):
    
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_class = PropertyFilter
    filterset_fields = ('size', 'type', 'actions')
    search_fields = ['property_name', 'address', 'description' ]

    def filter_queryset(self, queryset):
        """
        Gets the text representation of an action ('rent', 'sale', 'invest') from 
        the param and returns properties that have that action in their actions code.
        i.e if the action param is rent, it returns properties up for rent alone, 
        up for rent and sale, and up for rent, sale and investments.
        """
        queryset = super().filter_queryset(queryset)
        actions = self.request.query_params.getlist('action')
        if actions:
            action_codes = {
                "NoActions": "000",
                'rent': ['001', '011', '101', '111'],
                "sale": ['010', '011', '110','111'],
                "invest":['100', '101', '110', '111']
            }
            # Construct Q objects for filtering properties with the specified actions
            q_objects = Q()
            
            action = actions[0]
            action_code = action_codes.get(action)
            if action_code:
                if isinstance(action_code, list):
                    q_objects |= Q(actions__in=action_code)
                else:
                    q_objects |= Q(actions__contains=action_code)
            # Filter queryset to include properties that match the specified actions
            queryset = queryset.filter(q_objects)
        return queryset


class PropertyDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Property.objects.all()
    serializer_class = PropertyDetailsSerializer


class PropertyFeatures(viewsets.ModelViewSet):

    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # A queryset defined for schema generation metadata
            return Feature.objects.none()
        
        # Get property id and filter features by property
        property_id = self.kwargs.get("pk")
        try:
            property = Property.objects.get(id=property_id)
        except:
            property = None
        if property is None:
            return Response({"error":"Property not found"}, status=status.HTTP_404_NOT_FOUND)
        
        return Feature.objects.all()
        #return Feature.objects.filter(property=property.id)
    

class Feature(generics.RetrieveAPIView):

    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer


    def get(self, request, *args, **kwargs):

        return super().get(request, *args, **kwargs)






# ---------- CORE ACTIONS ----------

class TourBookingView(viewsets.ModelViewSet):
    """
    Returns all avaliable property tours to admin users only. Allows filtering of property tours
    based on number of "booked_by"s, the property and date of tour.
    Also allows creating/scheduling property tours
    """

    queryset = PropertyTour.objects.all()
    serializer_class = TourBookingSerializer
    permission_classes = []
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ("property", )
    lookup_field = 'pk'

    def get_permissions(self):
        if self.request.method == "GET":
            return [permissions.IsAdminUser()]
        # Build create permission into self.request.method == "POST"
        return super().get_permissions()


    def create(self, request, *args, **kwargs):
        # make sure request user is the same as the manager of the property 

        return super().create(request, *args, **kwargs)


class BookTour(APIView):
    """
    On GET: Adds the request user to the booked_by field of a PropertyTour 
    instance.
    This effectively, books a tour on a property for the user
    """
    queryset = PropertyTour.objects.all()
    serializer_class = TourBookingSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "pk"



    def get(self, request, *args, **kwargs):
        tour_id = kwargs.get("pk")
        try:
            tour = PropertyTour.objects.get(id=tour_id)
        except:
            tour = None
        
        user = request.user
        print(user)

        return Response(
            {
                "message": "This is the index route of the RASPA API",
                "developer": "Olaniyi George"
            })



    def update(self, request, *args, **kwargs):
        # if the request user is not the property lister, allow update on only the 
        return super().update(request, *args, **kwargs)
    

class BuyView(viewsets.ModelViewSet):

    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


    def create(self, request, *args, **kwargs):

        return super().create(request, *args, **kwargs)

class PaymentView(APIView):

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    
    def get(self, request, *args, **kwargs):

        return Response({})



    

# Pay
# Rent
# Bid
# Book Tour
