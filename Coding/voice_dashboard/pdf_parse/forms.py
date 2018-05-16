from django import forms
from pdf_parse import models

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    docfile  = forms.FileField()


# class update_db(forms.ModelForm):
#     class Meta:
#         model = models.Metadata
#         fields = ['themen', 'vero', 'risko', 'betro', 'link', 'sachstand']