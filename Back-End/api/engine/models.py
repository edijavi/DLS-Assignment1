from django.db import models

# Create your models here.

class File(models.Model):
    path = models.CharField(max_length = 500)
    name = models.CharField(max_length = 50)
    nchars = models.IntegerField()
    nlines = models.IntegerField()

class Word(models.Model):
    value = models.CharField(max_length = 500)
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    line = models.IntegerField()