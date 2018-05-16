from django.shortcuts import render
import json
import logging
import os
import errno
import PyPDF2 as pyPdf
import tabula
from django.http import JsonResponse, HttpResponse
import pandas as pd
from django.http import HttpResponseRedirect
from django.shortcuts import render
from voice_dashboard import settings
# Create your views here.
from django.core.files.storage import FileSystemStorage
from .models import Metadata


def upload_form(request):
    return render(request, "upload.html", {})


def upload_multi_file(request):
    if request.method == 'POST':
        files = request.FILES.getlist("files")
        for file in files:
            handle_uploaded_file(file)
    return HttpResponse("File(s) uploaded!")


def parse_pdf(request):
    if request.method == 'GET':
        return HttpResponse('Created')


def handle_uploaded_file(f):
    fs = FileSystemStorage(location='document/')
    fs.save(f.name, f)
    split_page(f)


def split_page(file):
    content = pyPdf.PdfFileReader(file)
    sub_dir = file.name.split(' ')[0]
    file_path = os.path.join(settings.BASE_DIR, 'document\\' + sub_dir)
    if not os.path.exists(file_path):
        try:
            os.makedirs(file_path)
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise
    for page in range (content.getNumPages()):
        output_file = pyPdf.PdfFileWriter()
        output_file.addPage(content.getPage(page))
        with open(os.path.join(file_path, 'page_' + str(page) + '.pdf'), "wb+") as outputStream:
            output_file.write(outputStream)
            save_to_db()


def save_to_db():
    # pd = tabula.read_pdf(file, lattice=True, stream=False, guess=False,
    #                      pandas_options={'header': None, 'error_bad_lines': False}, encoding='cp1252',
    #                      kwargs='tabula.jar')
    themen = '1'
    vero = '2'
    risko = '3'
    betro = '4'
    link = '5'
    sachstand = '6'
    db_object = Metadata(themen=themen, vero=vero, risko=risko, betro=betro, link=link, sachstand=sachstand)
    db_object.save()