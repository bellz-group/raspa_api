from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from .models import BaseUserProfile



@receiver(post_save, sender=get_user_model())
def create_user_profile(sender, instance, created, **kwargs):
    '''
    Creates a BaseUserProfile for every user instance created or checks if it exists
    '''
    if created:
        try:
            base_profile = BaseUserProfile.objects.create(user=instance)
            print("Base user profile created")
        except Exception as e:
            print(f"Error creating Base user profile: {e}")
    else:
        # If the user instance was not created (probably updated), check if a profile exists
        try:
            base_profile = BaseUserProfile.objects.get(user=instance)
            print("Base user profile already exists")
        except BaseUserProfile.DoesNotExist:
            try:
                # If the profile does not exist, create a new one
                base_profile = BaseUserProfile.objects.create(user=instance)
                print("Base user profile created")
            except Exception as e:
                print(f"Error creating Base user profile: {e}")



