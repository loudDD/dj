from django.db import models


# Create your models here.
class BookInfo(models.Model):
    '''
    1.主键 当前可以自动生成
    id,name,pub_data,commentcount,readcount
    '''
    name = models.CharField(max_length=10)
    pub_date = models.DateField(default='1990-01-01')
    commentcount = models.IntegerField(default=0)
    readcount = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    book = models.ForeignKey(BookInfo, on_delete=BookInfo)

    def __str__(self):
        return self.name


class CustomerInfo(models.Model):
    c_name = models.CharField(max_length=10)
    choices = ((0, "女"), (1, "男"))
    c_sex = models.SmallIntegerField(choices)
    c_cost = models.FloatField(default=10.0)

class Question(models.Model):
    quesion_test = models.CharField(max_length=50)
    pub_date = models.DateTimeField('data published')

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_test = models.CharField(max_length=20)
    votes = models.IntegerField(default=0)