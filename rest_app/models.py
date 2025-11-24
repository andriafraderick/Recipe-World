from django.db import models

# Create your models here.

from datetime import timedelta

class Recipe(models.Model):

    name = models.CharField(max_length= 200)
    Prep_time = models.DurationField(default= (timedelta(minutes = 120)))
    DIFFICULTY_CHOICE= [
        (1,"EASY"),
        (2,'MEDIUM'),
        (3,'HARD')
    ]

    difficulty = models.IntegerField(choices= DIFFICULTY_CHOICE)
    vegetarian = models.BooleanField()
    recipe_img = models.ImageField(upload_to='recipe/')
    description = models.CharField(max_length=5000)

