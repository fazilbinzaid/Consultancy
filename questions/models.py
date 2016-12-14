from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.TextField()

    def get_absolute_url(self):
        return "questions/"

    def __str__(self):
        return self.question_text
