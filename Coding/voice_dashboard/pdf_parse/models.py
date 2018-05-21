from django.db import models
from django.forms import ModelForm
# Create your models here.

class UploadFile(models.Model):
    file_name = models.CharField(max_length=1000)
    file_object = models.FileField()


class Metadata(models.Model):
    # number = models.IntegerField()
    datum = models.DateField()
    title = models.CharField(max_length=5000)
    sachstand = models.CharField(max_length=5000)
    file = models.ForeignKey(UploadFile, on_delete=models.CASCADE)
