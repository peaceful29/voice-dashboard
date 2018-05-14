from django.shortcuts import render
import json
import logging
import os
import errno
import PyPDF2 as pyPdf
from django.http import JsonResponse, HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import UploadFileForm
from .models import Document
# Create your views here.
from django.core.files.storage import FileSystemStorage

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()
            handle_uploaded_file(request.FILES['docfile'])
            return HttpResponseRedirect(reverse('list'))
    else:
        form = UploadFileForm()
    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(
        request,
        'list.html',
        {'documents': documents, 'form': form}
    )
    # if request.method == 'POST' and request.FILES['myfile']:
    #     myfile = request.FILES['myfile']
    #     fs = FileSystemStorage()
    #     filename = fs.save(myfile.name, myfile)
    #     uploaded_file_url = fs.url(filename)
    #     return render(request, 'upload.html', {
    #         'uploaded_file_url': uploaded_file_url
    #     })
    # return render(request, 'upload.html')


def parse_pdf(request):
    if request.method == 'GET':
        return HttpResponse('Created')


def handle_uploaded_file(f):
    with open('name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def split_page(pdf_file):
    print (pdf_file)
    content = pyPdf.PdfFileReader(pdf_file)
    # filePath = os.path.join(DATA_PATH, fileName.split('.')[0])
    # if not os.path.exists(filePath):
    #     print ('vao 1')
    #     try:
    #         os.makedirs(filePath)
    #     except OSError as exc:  # Guard against race condition
    #         if exc.errno != errno.EEXIST:
    #             raise
    for page in range (content.getNumPages()):
        # content = pdfContent.getPage(page)
        # filePath = os.path.join(DATA_PATH, fileName, 'page', str(page))
        outputFile = pyPdf.PdfFileWriter()
        outputFile.addPage(content.getPage(page))
        # with open(os.path.join(filePath, 'page_' + str(page) + '.pdf'), "wb") as outputStream:
        with open('page_' + str(page) + '.pdf', "wb") as outputStream:
            outputFile.write(outputStream)
    # convert_to_csv(filePath)
