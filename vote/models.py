from django.db import models



class Question(models.Model):
    question_text = models.CharField(max_length=50,verbose_name="question_test")
    pub_date = models.DateTimeField(verbose_name="pub_date")

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE,verbose_name="question")
    choice_text = models.CharField(max_length=30,verbose_name="choice_test")
    votes = models.IntegerField(default=0,verbose_name="vote number")


