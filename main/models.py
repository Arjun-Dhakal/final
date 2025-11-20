from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)
    

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return self.email
    


class Slide(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    message=models.TextField()
    image=models.ImageField(upload_to='slides/')

    def __str__(self):
        return self.title

class Client(models.Model):
    name=models.CharField(max_length=200,null=True,blank=True) 
    logo=models.ImageField(upload_to='clients/')

    def __str__(self):
        return self.name
    
class About(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    image=models.ImageField(upload_to='about/')
    
    def __str__(self):
        return self.title
    
class Service(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    icon=models.ImageField(upload_to='services/')

    def __str__(self):
        return self.title

class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    subject=models.CharField(max_length=200)
    message=models.TextField()
    maps=models.TextField()

    def __str__(self):
        return self.name
    

class Media(models.Model):
    office_description = models.CharField(max_length=255)
    office_phone = models.IntegerField()
    office_address = models.CharField(max_length=100)
    office_email = models.EmailField()
    facebook=models.URLField(max_length=200,null=True,blank=True)
    twitter=models.URLField(max_length=200,null=True,blank=True)
    instagram=models.URLField(max_length=200,null=True,blank=True)
    linkedin=models.URLField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.office_email
