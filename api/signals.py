from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from .models import *
import datetime


@receiver(post_save, sender=Bid)
def bill_for_bid(sender, instance, created, **kwargs):
    '''
    Creates a Bid is made if created:
    
    '''
    




@receiver(post_save, sender=Rental)
def bill_for_bid(sender, instance, created, **kwargs):
    '''
    Update the amount, landlord and timestamp on a rental
    
    '''
    if created:
        instance.amount  = instance.listing.price
        instance.datetime = datetime.datetime.now()
        instance.save()

