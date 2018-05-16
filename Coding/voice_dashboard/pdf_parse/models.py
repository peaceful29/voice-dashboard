from django.db import models
from django.forms import ModelForm
# Create your models here.
def filePath(file_name):
    return 'uploads/{0}'.format(file_name)


class File(models.Model):
    doc_file = models.FileField(upload_to=filePath)


class Metadata(models.Model):
    # number = models.IntegerField()
    # datum = models.DateTimeField()
    themen = models.CharField(max_length=5000)
    vero =  models.CharField(max_length=5000)
    risko = models.CharField(max_length=5000)
    betro = models.CharField(max_length=5000)
    link = models.CharField(max_length=5000)
    sachstand = models.CharField(max_length=5000)
    # file = models.ForeignKey(File, on_delete=models.CASCADE)


class update_db(ModelForm):
    class Meta:
        model = Metadata
        fields = ['themen', 'vero', 'risko', 'betro', 'link', 'sachstand']