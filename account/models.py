from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, Group, Permission
import uuid
from .managers import UserManager



class BaseUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Details    
    email = models.EmailField(unique=True, null=False, blank=False)
    
    username = models.CharField(max_length=100, null=True, blank=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)

    # Verification
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.is_verified = True
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.email}"


class BaseUserProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE, related_name="user_profile")
    
    display_name = models.CharField(max_length=100, null=True, blank=True)


    def save(self, *args, **kwargs):
        '''
        Sets user profile ID to the same as the user ID
        '''
        self.id = self.user.id
        super().save(*args, **kwargs)

    def __str__(self):
        name = f"{self.user.first_name} {self.user.last_name}"
        # print(f"Name: {name}")
        # print(len(name))
        if len(name) < 2:
            return f'{self.user}'
        return f"{self.user.first_name} {self.user.last_name}"

