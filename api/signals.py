from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from .models import *



@receiver(post_save, sender=Bid)
def bill_for_bid(sender, instance, created, **kwargs):
    '''
    Creates a Bid is made if created:
    
    '''
    


