from django.db import models
import uuid
from account.models import BaseUserProfile
from django.contrib.gis.db import models

#  -------- SINGLE UNIT PROPERTIES --------

class Feature(models.Model):
    """
    A representation for the features of a typical building 
    EXAMPLES:
        
        "bdr", "bedroom"
        "btr", "bathroom"
        "flr", "floors"
        
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=25)
    icon = models.ImageField(upload_to='icons/features/', blank=True, null=True)
    count = models.IntegerField(default=0)


    def __str__(self):
        return f"{self.count} {self.name}(s)"
    
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
    name = models.CharField(max_length=40)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name}"
    
class Building(models.Model):
    """
    A representation of a landed property in form of a building
    """
    PURPOSE = [
        ("residential", "residential"),
        ("industrial", "industrial"),
        ("commercial", "commercial"),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    listed_by = models.ForeignKey(BaseUserProfile, on_delete=models.SET_NULL, null=True, blank=True)

    # Building(property) Info
    property_name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    type = models.CharField(max_length=12, choices=PURPOSE, default="residential")
    description = models.TextField()
    owner = models.ForeignKey(BaseUserProfile, on_delete=models.SET_NULL, null=True, blank=True)


    # Add ons
    features = models.ManyToManyField(Feature)
    amenities = models.ManyToManyField(Amenity)

    # Coordinates
    latitude = models.DecimalField(max_digits=18, decimal_places=15)
    longitude = models.DecimalField(max_digits=18, decimal_places=15)

    # Timestamp
    built_at = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.type}: {self.property_name}"
    


#  -------- UNDEVELOPED PROPERTIES --------
class Land(models.Model):
    """
    A representation of a undeveloped land plots
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    size = models.DecimalField(("size"), max_digits=18, decimal_places=3, 
                               help_text=(
            "Size of the land plot in meters square"
        ),)
    
    # Coordinates : The exact location of the land plot
    latitude = models.DecimalField(max_digits=18, decimal_places=15)
    longitude = models.DecimalField(max_digits=18, decimal_places=15)

    # Shape(GIS) : Poly shape of the land plot
    border = models.PolygonField()
    
    # Ownerships
    listed_by = models.ForeignKey(BaseUserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    owner = models.ForeignKey(BaseUserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    

    def __str__(self):
        return f"{self.owner}'s {self.size} land"

#  -------- MULTI UNIT PROPERTIES --------