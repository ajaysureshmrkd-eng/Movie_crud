from django.db import models

# Create your models here.

class Moive(models.Model):
    title =models.CharField(max_length=200)
    language =models.CharField(max_length=200)
    year =models.PositiveIntegerField()
    run_time =models.PositiveIntegerField()
    