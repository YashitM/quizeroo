# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username + ": " + str(self.score)

CATEGORY_CHOICES =( 
    ("1", "Sports"), 
    ("2", "Technology"), 
    ("3", "Space"), 
    ("4", "Geography"),
    ("5", "Food"),
) 

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Create your models here.
class Quiz(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)

    def __str__(self):
        return self.question


class Option(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    correct = models.BooleanField()

    def __str__(self):
        return self.text