from django.db import models
from django.contrib.auth.models import User

class PersonInfo(models.Model):
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_uploaded =  models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = "Person Info"


class ItemInfo(models.Model):
# A list of vehicle types to be defined as more information is given

#     TYPE = (
#         ('SUV', "SUV"),
#         ("HB", "Hatchback"),
#         ("CV", "Convertible"),
#         ("SD", "Sedan"),
#         ("MV", "Minivan"),
#         ("TR", "Truck"),
#         ("BK", "Motorcycle"),
#         ("OT", "Other"),
#    )
    vehicle = models.ForeignKey(PersonInfo,
                                blank = True,
                                null = True,
                                on_delete = models.CASCADE)
    plate = models.CharField(max_length = 15)
    type = models.CharField(max_length = 20) #choices = TYPE),
    maker = models.TextField(max_length = 15)
    colour = models.TextField(max_length = 15)
    image = models.ImageField(upload_to='vehicles/')

    class Meta:
        verbose_name_plural = "Item Info"
 

