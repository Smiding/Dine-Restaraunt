from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
import datetime
from django.utils import timezone

class Table(models.Model):
    TABLE_STATUS =(
    ("Available", "Available"),
    ("Out of Service", "Out of Service"),
    
)
    Name = models.CharField(max_length=200, unique=True)
    Capacity = models.IntegerField(blank = False, null= False)
    status = models.CharField(max_length=15,
        choices=TABLE_STATUS,
        default="Available",)
    def __str__(self):
        return f'{self.Name}'
  
class Booking(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    time = models.TimeField()
    date = models.DateField(null=False, blank=False)
    person=models.IntegerField(null=False,blank=False)
    table = models.ForeignKey(Table,null=False, blank=False,on_delete=models.CASCADE)
    def save(self,*args, **kwargs):
        available_tables = Table.objects.filter(status='Available').order_by('Capacity')
        for table in available_tables:
            if table.Capacity >= self.person:
                # Check if the table is already booked within one hour of the same day
                existing_bookings = Booking.objects.filter(
                    table=table,
                    date=self.date,
                    time__gte=datetime.datetime.combine(self.date,self.time) - datetime.timedelta(hours=1),
                    time__lt=datetime.datetime.combine(self.date,self.time) + datetime.timedelta(hours=1)
                ).exclude(pk=self.pk)  # Exclude the current booking if it's being updated

                if not existing_bookings:
                    self.table = table
                    break
        else:
            raise ValidationError("No available table found at the specified time")
        super(Booking, self).save(*args,**kwargs)

    