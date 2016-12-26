from django.db import models

# Create your models here.

class Language(models.Model):
    tag = models.CharField(max_length=20)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return "languages/%i/" % self.id


class Framework(models.Model):
    language = models.ForeignKey(Language, related_name='frameworks')
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "frameworks/%i/" % self.id


class Question(models.Model):
    framework = models.ForeignKey(Framework, related_name='questions')
    question_text = models.TextField()

    def get_absolute_url(self):
        return "questions/%i/" % self.id

    def __str__(self):
        return self.question_text
