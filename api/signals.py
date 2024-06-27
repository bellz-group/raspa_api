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
def set_rental_attrs(sender, instance, created, **kwargs):
    '''
    Update the amount, landlord and timestamp on a rental.
    Also create a payment instance for this rental
    
    '''
    if created:
        instance.amount  = instance.listing.price
        instance.landlord  = instance.listing.property.manager
        instance.datetime = datetime.datetime.now()

        if instance.tenant:
            payment = Payment.objects.create(
                                                payer=instance.tenant, 
                                                amount=instance.amount,
                                                payment_provider='flutterwave',
                                            )
            payment.save()
            instance.payment = payment 

        instance.save()


