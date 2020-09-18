from django.db import models

# Create your models here.

class SessionTest(models.Model):
    s_name = models.CharField(max_length=10,unique=True)
    s_password = models.CharField(max_length=20)
    s_token = models.CharField(max_length=256)