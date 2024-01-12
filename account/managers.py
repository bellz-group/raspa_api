from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    # print('User Manager')
        
    def create_user(self, email, password=None, **extra_fields):
        # print('User Manager: create user')
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()

        print('User created')
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Admin Users must have an email address")
        email = email
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_verified', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        if extra_fields.get('is_verified') is not True:
            raise ValueError('Superuser must have is_verified=True')

        print('SuperUser Validation complete')
        return self.create_user(email, password,  **extra_fields)
    

