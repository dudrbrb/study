from django.db import models
from django.contrib import admin

# Create your models here.

class Works(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date = models.CharField(max_length=10)
    link = models.CharField(max_length=500)
    def __str__(self):
        return self.title


class Stacks(models.Model):
    skill = models.CharField(max_length=200)
    def __str__(self):
        return self.skill