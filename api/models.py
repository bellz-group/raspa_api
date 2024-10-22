from typing import Any
from django.db import models
import uuid
from account.models import BaseUserProfile
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import timedelta
#from django.contrib.gis.db import models


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

    
#  -------- MULTI UNIT PROPERTIES --------
#  -------- SINGLE UNIT PROPERTIES --------

    
class Amenity(models.Model):
    """
    A representation of the basic amenities, finishings and vanity metrics
    users use in rating and making decisions about acquiring properties.
    
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
    type = models.CharField(max_length=150, default="Amenity", null=True, blank=True)
    name = models.CharField(max_length=60, unique=True)

    
    def __str__(self):
        return f"{self.type}: {self.name}"
    

# WholeLandedProperty
# -- id - owner - manager - name - description - address - type
# -- size - amenities - longitude - latitude - border(poly) 
# -- is_verified - built_at - created_at - updated_at

# UnitProperty | Space
# -- id - manager - parentProperty - name - description - address(exact) - type 
# -- size - amenities - created_at - updated_at - is_verified


class Property(models.Model):
    """
    A representation of a real estate landed property in form of; 
    a developed(buildings, sheds, ) or an undeveloped(land plot) landed asset
    """
    PURPOSE = [
        ("residential", "residential"),
        ("industrial", "industrial"),
        ("commercial", "commercial"),
        ("land", "land"),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Management & Ownership
    #parent = models.ForeignKey(Property, null=True, blank=True)
    manager = models.ForeignKey(BaseUserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name="buildings_i_listed")
    owner = models.ForeignKey(BaseUserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name="my_buildings")


    # Buildi property) Info
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    type = models.CharField(max_length=12, choices=PURPOSE, default="residential")
    description = models.TextField()
    images = models.ManyToManyField('PropertyImage', related_name='properties', blank=True)
    actions = models.CharField(max_length=3, choices=ACTIONS, default="101", null=False)

    # Add ons
    amenities = models.ManyToManyField(Amenity, blank=True)
    is_verified = models.BooleanField(default=False, null=True)

    # Features   
    ## features = models.ManyToManyField(Feature)


    size = models.FloatField(("size"), default=0, null=False, blank=True,
                               help_text=(
            "Size in meter square: 1 plot is 120ft x 6ft : 668.901m2"
        ),)


    # Shape(GIS) : Poly shape of the land plot
    #border = models.MultiPolygonField(null=True, )

    # Center Coordinates 
    latitude = models.DecimalField(max_digits=18, decimal_places=15, validators=[MinValueValidator(-90), MaxValueValidator(90)])
    longitude = models.DecimalField(max_digits=18, decimal_places=15, validators=[MinValueValidator(-180), MaxValueValidator(180)])
    # Timestamp
    built_at = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.type}: {self.name}"
    
    def save(self, *args, **kwargs):
        if not self.manager: 
            self.manager = self.owner
        
        super().save(*args, **kwargs)

    def my_images(self):
        return PropertyImage.objects.filter(property=self.id)

class PropertyListing(models.Model):
    LISTING_TYPES = [
        ('rent', 'Rent'),
        ('sale', 'Sale'),
        ('investment', 'Investment')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    address = models.CharField(max_length=450, null=True, blank=True) # The exact address of this listng in this property e.g apartment number
    listing_type = models.CharField(max_length=20, choices=LISTING_TYPES)
    price = models.FloatField()
    avaliability = models.BooleanField(default=False, blank=True) 
    contract = models.FileField(upload_to="rental-contracts/", default="rental-contracts/default_contract.docx", blank=True)
    
    def __str__(self):
            return f"{self.listing_type} on {self.property}"
    

    def save(self, *args, **kwargs):
        self.address = self.address + self.property.address
        super().save(*args, **kwargs)
    

    
    
class Feature(models.Model):
    """
    A representation for a group of features of a typical building 
    EXAMPLES:
        
        "bdr", "bedroom"
        "btr", "bathroom"
        "flr", "floors"
        
    """
    FEATURES = [
        ("blg", "buildings"),
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
    size = models.FloatField(("size"), default=0, null=False, blank=True,
                               help_text=(
            "Size in meter square: 1 plot is 120ft x 6ft : 668.901m2"
        ),)

    def __str__(self):
        return f"{self.count} {self.name}(s)"

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, null=True, related_name='propertyImages')
    image = models.ImageField(upload_to='property-images/')

    def __str__(self):
        return self.image.url

class FeatureImage(models.Model):
    image = models.ImageField(upload_to='features/')

    def __str__(self):
        return self.image.url


#  -------- UTILS -------
class PropertyTour(models.Model):

    TYPE = [
        ("virtual", "virtual"),
        ("in-person", "in-person"),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, null=False, related_name="property_tours")
    tour_type = models.CharField(max_length=12, choices=TYPE, default="in-person")
    duration = models.DurationField()
    datetime = models.DateTimeField()

class Booking(models.Model):

    user = models.ForeignKey(BaseUserProfile, on_delete=models.CASCADE)
    property_tour = models.ForeignKey(PropertyTour, on_delete=models.CASCADE)
    

#  -------- PAYMENTS --------

class Payment(models.Model):

    STATUS = [
        ("pending", "pending"),
        ("failed", "failed"),
        ("successfull", "successfull"),
        ("denied", "denied"),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    payer = models.ForeignKey(BaseUserProfile, on_delete=models.CASCADE, null=False, blank=False)
    amount = models.FloatField(default=1)
    status = models.CharField(max_length=12, choices=STATUS, default="pending")
    payment_provider = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):  
        return f"{self.amount}: {self.payer}"
    


#  -------- CORE --------

def get_first_user():
    first = BaseUserProfile.objects.first()
    return first.id


class Rental(models.Model):
    """
    A representation of a request to t=rent a property. Would be used to 
    keep track of the parties involved in the transaction.

    """
    STATUS = [
        ("pending", "pending"),
        ("cancelled", "cancelled"),
        ("active", "active"),
        ("complete", "complete"),

    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    tenant = models.ForeignKey(BaseUserProfile, on_delete=models.SET_NULL, null=True, related_name="rentals")
    landlord =  models.ForeignKey(BaseUserProfile, on_delete=models.SET_NULL, null=True, related_name="rented_out")
    listing = models.ForeignKey(PropertyListing, on_delete=models.CASCADE, default="f55470e2-aeed-4f5f-a329-6ddc37b83455", null=False, blank=False)
    
    status = models.CharField(max_length=9, choices=STATUS, default="pending")
    amount = models.FloatField(default=999999999.0, null=False, blank=True)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True, blank=True)

    duration = models.DurationField(default=timedelta(seconds=31536000), null=False, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rental: ({self.tenant.display_name}) : ({self.listing}) "


class Purchase(models.Model):
    """

    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    buyer = models.ForeignKey(BaseUserProfile, on_delete=models.SET_NULL, null=True, related_name="have_bought")
    seller =  models.ForeignKey(BaseUserProfile, on_delete=models.SET_NULL, null=True, related_name="have_sold")
    property = models.ForeignKey(Property, on_delete=models.CASCADE, null=False, blank=False)
    

    amount = models.FloatField(null=False, blank=False)
    contract = models.FileField(upload_to="purchase-contracts/", storage= None ) # Add link to soft agreement
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True, blank=True)

    datetime = models.DateTimeField()


class Invest(models.Model):
    """

    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    investor = models.ForeignKey(BaseUserProfile, on_delete=models.CASCADE, null=False, blank=False)
    property = models.ForeignKey(Property,  on_delete=models.CASCADE, null=False, blank=False)
    
    amount = models.FloatField(null=False, blank=False)
    payment = models.ForeignKey(Payment,  on_delete=models.SET_NULL, null=True)
    
    duration = models.DurationField(null=False, blank=False)
    datetime = models.DateTimeField()






















#  -------- V2 --------

class Bid(models.Model):

    bidder = models.ForeignKey(BaseUserProfile, on_delete=models.CASCADE, null=False, blank=False)
    property = models.ForeignKey(Property, on_delete=models.SET_NULL, null=True, related_name="property_bids")
    price_tag = models.FloatField(default=0)
    payment = models.ForeignKey(Payment,  on_delete=models.CASCADE)


