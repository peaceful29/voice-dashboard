from django.shortcuts import render
import json
import logging
from django.http import JsonResponse, HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import UploadFileForm
# Create your views here.


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


def parse_pdf(request):
    if request.method == 'GET':
        return HttpResponse('Created')
