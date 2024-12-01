from django.db import models


# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=125)
    second_name = models.CharField(max_length=125)
    age = models.IntegerField()
    photo = models.ImageField(upload_to=True)
    date = models.DateTimeField(auto_now_add=True)