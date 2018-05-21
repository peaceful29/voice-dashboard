from django.contrib import admin

# Register your models here.
from .models import UploadFile
from .models import Metadata

admin.site.register(UploadFile)
admin.site.register(Metadata)