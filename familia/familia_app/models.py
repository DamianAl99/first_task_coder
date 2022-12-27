from django.db import models

class familia(models.Model):
    name= models.CharField(max_length=100)
    surname= models.CharField(max_length=100)
    age= models.FloatField()
    have_a_dog= models.BooleanField()
    

# Create your models here.
