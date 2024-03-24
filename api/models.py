from django.db import models
import uuid
from account.models import BaseUserProfile
from django.core.validators import MinValueValidator, MaxValueValidator
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
    
class DevelopedProperty(models.Model):
    """
    A representation of a landed property in form of a building
    """
    PURPOSE = [
        ("residential", "residential"),
        ("industrial", "industrial"),
        ("commercial", "commercial"),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    listed_by = models.ForeignKey(BaseUserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name="buildings_i_listed")

    # Building(property) Info
    property_name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    type = models.CharField(max_length=12, choices=PURPOSE, default="residential")
    description = models.TextField()
    owner = models.ForeignKey(BaseUserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name="my_building")
    images = models.ManyToManyField('PropertyImage', related_name='properties', blank=True)
    actions = models.CharField(max_length=3, choices=ACTIONS, default="101", null=False)

    # Add ons
    amenities = models.ManyToManyField(Amenity)
    


    # Features  --------- 
    # #features = models.ManyToManyField(Feature)
    size = models.IntegerField(("size"), default=0, null=False, blank=True,
                               help_text=(
            "Size in meter square: 1 plot is 120ft x 6ft : 668.901m2"
        ),)

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
    property = models.ForeignKey(DevelopedProperty, on_delete=models.CASCADE, null=True, blank=True, related_name="features")
    name = models.CharField(max_length=10, choices=FEATURES, null=False, blank=False)
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


#  -------- UNDEVELOPED PROPERTIES --------
class Land(models.Model):
    """
    A representation of a undeveloped land plots
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    area = models.DecimalField(("area"), max_digits=18, decimal_places=3, 
                               help_text=(
            "Size of the land plot in meters square"
        ),)
    
    # Coordinates : The exact location of the land plot
    latitude = models.DecimalField(max_digits=18, decimal_places=15)
    longitude = models.DecimalField(max_digits=18, decimal_places=15)

    # Shape(GIS) : Poly shape of the land plot
    #border = models.MultiPolygonField()
    
    # Ownerships
    listed_by = models.ForeignKey(BaseUserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name="land_listed_by_me")
    owner = models.ForeignKey(BaseUserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name="my_land_plots")
    

    def __str__(self):
        return f"{self.owner}'s {self.area} land"

#  -------- MULTI UNIT PROPERTIES --------