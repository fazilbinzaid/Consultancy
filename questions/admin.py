from django.contrib import admin
from .models import Question, Language, Framework

admin.site.register(Language)
admin.site.register(Framework)
admin.site.register(Question)
