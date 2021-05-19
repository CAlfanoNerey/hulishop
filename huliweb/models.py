from django.db import models

# Create your models here.

class Inquiry(models.Model):
    name= models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    inquiry = models.CharField(max_length=400)
    phone = models.CharField(max_length=100,blank=True)
