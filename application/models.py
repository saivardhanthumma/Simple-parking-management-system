from django.db import models
from datetime import datetime

class Category(models.Model):
    
    parking_area_no=models.CharField(max_length=100)
    vehicle_type=models.CharField(max_length=100,unique=True)
    vehicle_limit=models.CharField(max_length=100)
    parking_charge = models.DecimalField(max_digits=3, decimal_places=2)
    doc = models.DateTimeField(default=datetime.now)
    status = models.BooleanField(default=True)
    class Meta:
        db_table="Category"

class Add_Vehicle(models.Model):
  
    vehicle_no=models.CharField(max_length=100)
    parking_area_no=models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=200, null=False)
    parking_charge = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.BooleanField(default=True)
    arrival_time = models.DateTimeField(default=datetime.now)
    class Meta:
        db_table="Add_Vehicle"


