from django.db import models

# Create your models here.

class Quiz(models.Model):
    questionID = models.AutoField(primary_key=True)
    question = models.CharField(max_length=500)
    correctAnswer = models.CharField(max_length=500)
    answers = models.CharField(max_length=500)