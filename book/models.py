from django.db import models

# Create your models here.
class BookInfo(models.Model):
    '''
    1.主键 当前可以自动生成

    '''
    name = models.CharField(max_length=10)

class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    book = models.ForeignKey(BookInfo,on_delete=BookInfo)