from django.db import models


# Create your models here.

class RegisterInfo(models.Model):
    name = models.CharField(max_length=10)
    password = models.CharField(max_length=10)

class Deltest(models.Model):

    testmanager = models.Manager
    d_name = models.CharField(max_length=10)
    d_cost = models.IntegerField(null=True,blank=True)

