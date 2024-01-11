from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, Group, Permission
import uuid




class BaseUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Details    
    email = models.EmailField(unique=True, null=False, blank=False)
    
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)


     # Add related_name to avoid clashes
    # groups = models.ManyToManyField(Group, related_name='baseuser_groups')
    # user_permissions = models.ManyToManyField(Permission, related_name='baseuser_perms')


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class BaseUserProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE, related_name="user_profile")


