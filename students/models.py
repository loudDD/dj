from django.db import models

# Create your models here.
from django.db.models import AutoField







class Class_List(models.Model):

    c_name = models.CharField(max_length=100)

class Students(models.Model):

    s_name = models.CharField(max_length=30)
    s_class = models.ForeignKey(Class_List,on_delete=models.CASCADE)
