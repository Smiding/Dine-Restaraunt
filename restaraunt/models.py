from django.db import models

from django.contrib.auth import get_user_model

class Reservation(models.Model):
    customer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    datetime = models.DateTimeField(max_length=200,blank = False, null= False)
    size = models.IntegerField(default=1,blank = False, null= False)

class Table(models.Model):
    TABLE_STATUS =(
    ("Available", "Available"),
    ("Reserved", "Reserved"),
    ("Occupied", "Occupied"),
    ("Out of Service", "Out of Service"),
    
)
    Name = models.CharField(max_length=200)
    Capacity = models.IntegerField(blank = False, null= False)
    status = models.CharField(max_length=15,
        choices=TABLE_STATUS,
        default="Available",)
    