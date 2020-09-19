from django.db import models


# Create your models here.

class Person(models.Model):
    p_name = models.CharField(max_length=16)
    p_sex = models.BooleanField(default=False)


# class IDCard(models.Model):  # 1 : 1
#     id_num = models.CharField(max_length=18, unique=True)
#     id_person = models.OneToOneField(Person, null=True, blank=True, on_delete=models.SET_NULL)
    # id_person = models.ForeignKey(Person, unique=True);
    # id_person = models.OneToOneField(Person,null=True,blank = True , on_delete=models.CASCADE)
    # id_person = models.OneToOneField(Person,null=True,blank = True , on_delete=models.PROTECT)


class IDCard(models.Model):# 1:n
    id_num = models.CharField(max_length=18, unique=True)
    id_person = models.ForeignKey(Person,on_delete=models.CASCADE,null=True)
