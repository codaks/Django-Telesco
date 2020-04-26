from django.db import models

# Create your models here.

class Destinations(models.Model):
    
    name = models.CharField(max_length = 100)
    img =  models.ImageField(upload_to = "dest_pics")
    desc = models.TextField()
    price = models.IntegerField()