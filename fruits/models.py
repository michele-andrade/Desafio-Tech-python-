from tkinter import CASCADE
from django.db import models
#from uuid import uuid4

# Create your models here.
class Region(models.Model):
    region_name = models.CharField(max_length=50, primary_key=True, unique=True)

class Fruit(models.Model):
    fruit_name = models.CharField(max_length=70)
    region_name = models.ForeignKey(Region, on_delete=models.CASCADE)