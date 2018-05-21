from django.shortcuts import render
import json
import logging
import os
import errno
import PyPDF2 as pyPdf
import tabula
import pandas as pd
import datetime
from django.shortcuts import render
from voice_dashboard import settings
# Create your views here.
from django.core.files.storage import FileSystemStorage
from .models import Metadata
from .models import UploadFile
from pandas.io.common import EmptyDataError

pd.set_option('display.max_colwidth', -1)

check_arr = ['Sachstand', 'Bewertung', 'Empfehlung', 'Quellen']

def upload_form(request):
    query_meta = UploadFile.objects.all()
    return render(request, 'table-file-upload.html', {'query_meta': query_meta})


def upload_multi_file(request):
    if request.method == 'POST':
        files = request.FILES.getlist("files")
        for file in files:
            if (UploadFile.objects.filter(file_name=file.name).exists()):
                continue
            handle_uploaded_file(file)
    query_meta = UploadFile.objects.all()
    return render(request, 'table-file-upload.html', {'query_meta': query_meta})


def show_result(request):
    if request.method == 'GET':
        query_meta = Metadata.objects.all()
        return render(request, 'table-metadata.html', {'query_meta': query_meta})
        # return render(request, 'tables-advanced.html')


def handle_uploaded_file(f):
    fs = FileSystemStorage(location='document/')
    fs.save(f.name, f)
    file_object = UploadFile(file_name=f.name, file_object=f)
    file_object.save()
    split_page(f, file_object)


def split_page(file, file_object):
    content = pyPdf.PdfFileReader(file)
    sub_dir = file.name[0:8]
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
    data_report(file_path, file_object)


def data_report(file_path, file_object):
    for file in os.listdir(file_path):
        df = tabula.read_pdf(os.path.join(file_path, file), stream=True, guess=False,
                             output_format='dataFrame',
                             pandas_options={'header': None, 'error_bad_lines': False}, encoding='cp1252')
        txt_full = (df[0].to_string(index=False))
        if (all(x in txt_full for x in check_arr)):
            if('2018' in file_path):
                line_title = txt_full.split("Risiko")[0]
            else:
                line_title = txt_full.split("Titel")[0]
            count = line_title.count('\n')
            line_title = line_title.split('\n')[count - 1]
            if(': ' in line_title):
                title = line_title.split(': ')[1]
                if (line_title[10] == ':'):
                    datum = datetime.datetime.strptime(line_title[0:10], "%Y-%m-%d").date()
                elif (line_title[6] == ':'):
                    datum = datetime.datetime.strptime(line_title[0:6], "%Y-%m").date()
                elif (line_title[4] == ':'):
                    datum = datetime.datetime.strptime(line_title[0:4], "%Y").date()
            else:
                title = line_title
                datum = datetime.datetime.strptime(file_path[-8:], "%Y%m%d").date()
            sachstand = txt_full.split("Sachstand: ")[1].split('Bewertung:')[0].replace('\n', '').replace('  ', '')
            db_object = Metadata(datum=datum, title=title, sachstand=sachstand, file=file_object)
            db_object.save()
