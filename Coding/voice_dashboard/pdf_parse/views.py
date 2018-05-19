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
from pandas.io.common import EmptyDataError

pd.set_option('display.max_colwidth', -1)

file_name = []
file_type_1 = ['2014', '2015', '2016', '2017']
file_type_2 = ['2018']

def upload_form(request):
    return render(request, "upload.html", {})


def upload_multi_file(request):
    if request.method == 'POST':
        files = request.FILES.getlist("files")
        file_name.clear()
        for file in files:
            handle_uploaded_file(file)
            file_name.append(file.name)
    return render(request, 'uploaded.html', {'content':file_name})


def parse_to_db(request):
    if request.method == 'POST':
        for file in file_name:
            sub_dir = file[0:8]
            file_path = os.path.join(settings.BASE_DIR, 'document\\' + sub_dir)
            save_to_db(file_path)
        return HttpResponse('Saved to Database!!!')


def show_result(request):
    if request.method == 'GET':
        query_meta = Metadata.objects.all()
        return render(request, 'table-template.html', {'query_meta': query_meta})
        # return render(request, 'tables-advanced.html')

def handle_uploaded_file(f):
    fs = FileSystemStorage(location='document/')
    fs.save(f.name, f)
    split_page(f)


def split_page(file):
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
        parse_to_csv(file_path)


def parse_to_csv(file_path):
    for file in os.listdir(file_path):
        if('.pdf' in file):
            tabula.convert_into(os.path.join(file_path, file), os.path.join(file_path, file.replace('pdf', 'csv')),
                            output_format="csv", lattice=True, stream=False, guess=False,
                            pandas_options={'header': None, 'error_bad_lines': False}, encoding='ISO-8859-1')
    # save_to_db(file_path)


def save_to_db(file_path):
    file_type = check_type(file_path)
    quellen_row = 0
    sachstand_row = 0
    if (file_type == 'TYPE_1'):
        sachstand_row = 2
        quellen_row = 5
    elif (file_type == 'TYPE_2'):
        sachstand_row = 1
        quellen_row = 4
    for file in os.listdir(file_path):
        if (('.csv' in file) and ('page_0' not in file)):
            try:
                df = pd.read_csv(os.path.join(file_path, file), encoding='ISO-8859-1', error_bad_lines=False)
            except EmptyDataError:
                df = pd.DataFrame()
            if ((df.empty == False) and (df.shape[0] > 4)):
                themen = '1'
                vero = '2'
                risko = 'risko'
                betro = ' '
                link = string_clean(str(df.iloc[[quellen_row][0]]))
                sachstand = string_clean(str(df.iloc[[sachstand_row][0]]))
                db_object = Metadata(themen=themen, vero=vero, risko=risko, betro=betro, link=link, sachstand=sachstand)
                db_object.save()


def string_clean(str):
    if ('Risiko' in str):
        return str.split('Risiko')[1].replace('\\r', ' ').replace('dtype: object', '').split('Name:')[0].replace('  ', '').replace('\\n', ' ')
    else:
        return str.replace('\\r', ' ').replace('dtype: object', '').split('Name:')[0].replace('  ', '').replace('\\n', ' ')


def check_type(file_path):
    year = file_path[-8:][:4]
    if year in file_type_1:
        return 'TYPE_1'
    elif year in file_type_2:
        return 'TYPE_2'
