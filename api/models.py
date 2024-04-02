from typing import Any
from django.db import models
import uuid
from account.models import BaseUserProfile
from django.core.validators import MinValueValidator, MaxValueValidator
#from django.contrib.gis.db import models
from shortuuid.django_fields import ShortUUIDField

# Invest Sale  Rent 
ACTIONS = [
    ("000", "NoActions"),
    ("001", "Rent"),
    ("010", "Sale"),
    ("100", "Invest"),
    ("011", "Sale-Rent"),
    ("101", "Invest-Rent"),
    ("110", "Sale-Invest"),
    ("111", "Invest-Sale-Rent")
]

#  -------- SINGLE UNIT PROPERTIES --------

    
class Amenity(models.Model):
    """
    A representation of the basic amenities, finishing and vanity metrics users 
    use in rating and making decisions about properties
    EXAMPLES:
        
        POP/PVC
        Gated 
        Water running
        Fenced
        Tiled
        Prepaid meter
        Interlock/ Compound floor finish
        Road Facing
        
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=60, unique=True)

    
    def __str__(self):
        return f"{self.name}"
    
class Property(models.Model):
    """
    A representation of a real estate landed property in form of; a building, land plot ...
    """
    PURPOSE = [
        ("residential", "residential"),
        ("industrial", "industrial"),
        ("commercial", "commercial"),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Management & Ownership
    manager = models.ForeignKey(BaseUserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name="buildings_i_listed")
    owner = models.ForeignKey(BaseUserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name="my_buildings")


    # Building(property) Info
    property_name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    type = models.CharField(max_length=12, choices=PURPOSE, default="residential")
    description = models.TextField()
    images = models.ManyToManyField('PropertyImage', related_name='properties', blank=True)
    actions = models.CharField(max_length=3, choices=ACTIONS, default="101", null=False)

    # Add ons
    amenities = models.ManyToManyField(Amenity)

    # Features   
    ## features = models.ManyToManyField(Feature)


    size = models.IntegerField(("size"), default=0, null=False, blank=True,
                               help_text=(
            "Size in meter square: 1 plot is 120ft x 6ft : 668.901m2"
        ),)
    area = models.DecimalField(("area"), max_digits=18, decimal_places=3, 
                               help_text=(
            "Size of the land plot in meters square"
        ),)

    # Shape(GIS) : Poly shape of the land plot
    #border = models.MultiPolygonField(null=True, )

    # Center Coordinates 
    latitude = models.DecimalField(max_digits=18, decimal_places=15, validators=[MinValueValidator(-90), MaxValueValidator(90)])
    longitude = models.DecimalField(max_digits=18, decimal_places=15, validators=[MinValueValidator(-180), MaxValueValidator(180)])
    # Timestamp
    built_at = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.type}: {self.property_name}"

class Feature(models.Model):
    """
    A representation for a group of features of a typical building 
    EXAMPLES:
        
        "bdr", "bedroom"
        "btr", "bathroom"
        "flr", "floors"
        
    """
    FEATURES = [
        ("bdr", "bedroom"),
        ("btr", "bathroom"),
        ("flr", "floors"),
        ("ktc", "kitchen"),
        ("rms", "rooms")
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, null=True, blank=True, related_name="features")
    name = models.CharField(max_length=10, choices=FEATURES, null=True, blank=False)
    images = models.ManyToManyField('FeatureImage', related_name='features', blank=True)
    count = models.IntegerField(default=0)
    size = models.IntegerField(("size"), default=0, null=False, blank=True,
                               help_text=(
            "Size in meter square: 1 plot is 120ft x 6ft : 668.901m2"
        ),)




    def __str__(self):
        return f"{self.count} {self.name}(s)"


class PropertyImage(models.Model):
    image = models.ImageField(upload_to='property-images/')

    def __str__(self):
        return self.image.url

class FeatureImage(models.Model):
    image = models.ImageField(upload_to='features/')

    def __str__(self):
        return self.image.url

    



#  -------- MULTI UNIT PROPERTIES --------



#  -------- UTILS -------


#  -------- PAYMENTS --------

class Payment(models.Model):

    payer = models.ForeignKey(BaseUserProfile, on_delete=models.CASCADE, null=False, blank=False)
    amount = models.FloatField(default=0)
    provider = models.CharField(max_length=100)
    cleared = models.BooleanField(default=False)



class PropertyTour(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, null=False, related_name="property_tours")
    booked_by = models.ManyToManyField(BaseUserProfile, blank=True)
    date = models.DateTimeField()




#  -------- CORE --------

class Rent(models.Model):

    tenant = models.ForeignKey(BaseUserProfile, on_delete=models.SET_NULL, null=True, related_name="rented")
    landlord =  models.ForeignKey(BaseUserProfile, on_delete=models.SET_NULL, null=True, related_name="rented_out")
    property = models.ForeignKey(Property, on_delete=models.CASCADE, null=False, blank=False)
    amount = models.FloatField(null=False, blank=False)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, null=False, blank=False)
    agreement = models.FileField(upload_to="", storage= None )
    duration = models.DurationField(null=False, blank=False)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True)

class Sale(models.Model):
    """
    Represents an instance of a sale. Keeps track of the all the information 
    about the sale. 
    """
    buyer = models.ForeignKey(BaseUserProfile, on_delete=models.SET_NULL, null=True, related_name="have_bought")
    seller =  models.ForeignKey(BaseUserProfile, on_delete=models.SET_NULL, null=True, related_name="have_sold")
    property = models.ForeignKey(Property, on_delete=models.CASCADE, null=False, blank=False)
    amount = models.FloatField(null=False, blank=False)
    property = models.ForeignKey(Property,  on_delete=models.CASCADE, null=False, blank=False)
    agreement = models.FileField(upload_to="", storage= None )
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)


class Invest(models.Model):

    investor = models.ForeignKey(BaseUserProfile, on_delete=models.CASCADE, null=False, blank=False)
    amount = models.FloatField(null=False, blank=False)
    property = models.ForeignKey(Property,  on_delete=models.CASCADE, null=False, blank=False)
    agreement = models.FileField(upload_to="", storage= None )
    duration = models.DurationField(null=False, blank=False)
    payment = models.ForeignKey(Payment,  on_delete=models.SET_NULL, null=True)
    




#  -------- BID --------

class Bid(models.Model):

    bidder = models.ForeignKey(BaseUserProfile, on_delete=models.CASCADE, null=False, blank=False)
    property = models.ForeignKey(Property, on_delete=models.SET_NULL, null=True, related_name="property_bids")
    price_tag = models.FloatField(default=0)
    payment = models.ForeignKey(Payment,  on_delete=models.CASCADE)


