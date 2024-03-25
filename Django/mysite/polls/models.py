import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_txt=models.CharField(max_length=200)
    pub_date=models.DateTimeField("Date published")

    # def __str__(self) -> str:
    #     return self.question_txt
    
    def was_published_recently(self):
        return self.pub_date-timezone.now() <=  datetime.timedelta(days=1)

class Choice(models.Model):
    choice_text=models.CharField(max_length=100)
    votes=models.IntegerField(default=0)
    question=models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.choice_text
