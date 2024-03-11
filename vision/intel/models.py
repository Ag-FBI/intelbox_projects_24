from django.db import models
from django.contrib.auth.models import User


class PersonInfo(models.Model):
    class Gender(models.TextChoices):
     MALE = 'M', 'Male'
     FEMALE = 'F', 'Female'
    
    name = models.TextField(max_length = 35)
    age = models.IntegerField()
    alias = models.TextField(max_length = 50)
    description = models.TextField(max_length=70)
    gender = models.CharField(max_length = 1, choices=Gender.choices)
    #user = models.ForeignKey(User, on_delete=models.CASCADE,)
    date_uploaded =  models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = "Person Info"

class Image(models.Model):
    image = models.FileField(upload_to = "info/")



class Info(models.Model):
    GENDER = (
        ("M", "Male"),
        ("F", "Female"),
    )
    name = models.TextField(max_length = 35)
    age = models.IntegerField()
    aliases = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='persons/')
    description = models.TextField(max_length=70)
    gender = models.CharField(max_length = 10, choices= GENDER)
    date_uploaded =  models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = "Info"