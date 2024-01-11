from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, Group, Permission
import uuid




class BaseUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Details    
    email = models.EmailField(unique=True, null=False, blank=False)
    
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)


    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class BaseUserProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE, related_name="user_profile")
    
    display_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"P: {self.user}"
