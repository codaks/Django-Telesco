from django.db import models

# Create your models here.
class users(models.Model):
    username = models.CharField(max_length = 19)
    password = models.CharField(max_length = 18)
    email = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    zip_code = models.IntegerField()
