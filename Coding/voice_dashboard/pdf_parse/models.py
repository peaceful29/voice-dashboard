from django.db import models

# Create your models here.
def filePath(file_name):
    return 'uploads/{0}'.format(file_name)


class FileUpload(models.Model):
    docfile = models.FileField(upload_to=filePath)


class Document(models.Model):
    # number = models.IntegerField()
    # datum = models.DateTimeField()
    themen = models.CharField(max_length=5000)
    vero =  models.CharField(max_length=5000)
    risko = models.CharField(max_length=5000)
    betro = models.CharField(max_length=5000)
    link = models.CharField(max_length=1000)
    sachstand = models.CharField(max_length=5000)
    file = models.ForeignKey(FileUpload, on_delete=models.CASCADE)