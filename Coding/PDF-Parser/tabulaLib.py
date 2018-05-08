import tabula
import pandas as pd
import numpy as np
import sys
import errno
import os
import PyPDF2 as pyPdf
import shutil

DATA_PATH = '../../Data/'
# Read pdf into DataFrame

# tabula.convert_into("../../Data/document-page3.pdf", "../../Data/page3.csv", output_format="csv", Lattice=True, pandas_options={'header':None}, guess = False, encoding = 'ISO-8859-1')
# tabula.convert_into("../../Data/document-page3.pdf", "../../Data/page3.json", output_format="json", encoding = 'ISO-8859-1')

# print (df)
# df = tabula.read_pdf("../../Data/document-page3.pdf", output_format="csv", encoding = 'ISO-8859-1', Lattice=True, pandas_options={'header':None, 'error_bad_lines':False}, guess = False)
# print (df[0])
# df.to_csv("../../Data/document-page3.csv")
# Read remote pdf into DataFrame
# df2 = tabula.read_pdf("document-page0.pdf")

# convert PDF into CSV
# tabula.convert_into("test.pdf", "output.csv", output_format="csv")

# convert all PDFs in a directory
# tabula.convert_into_by_batch("input_directory", output_format='csv')
header = ['Nr', 'Datum', 'Themen', 'Veröffentlicht', 'Risiko', 'Betroffene Systeme', 'Links', 'Tags', 'Sachstand']

def remove_dir(fileName):
    filePath = os.path.join(DATA_PATH, fileName.split('.')[0])
    if os.path.exists(filePath):
        shutil.rmtree(filePath)


def split_page(fileName):
    pdfContent = pyPdf.PdfFileReader(open(os.path.join(DATA_PATH, fileName), 'rb'))
    filePath = os.path.join(DATA_PATH, fileName.split('.')[0])
    if not os.path.exists(filePath):
        print ('vao 1')
        try:
            os.makedirs(filePath)
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    for page in range (pdfContent.getNumPages()):
        # content = pdfContent.getPage(page)
        # filePath = os.path.join(DATA_PATH, fileName, 'page', str(page))
        outputFile = pyPdf.PdfFileWriter()
        outputFile.addPage(pdfContent.getPage(page))
        with open(os.path.join(filePath, 'page_' + str(page) + '.pdf'), "wb") as outputStream:
            outputFile.write(outputStream)
    convert_to_csv(filePath)


def convert_to_csv(filePath):
    for file in os.listdir(filePath):
        print(file)
        # tabula.convert_into(os.path.join(filePath, file), os.path.join(filePath, file.replace('pdf', 'csv')), output_format="csv", Lattice=True, pandas_options={'header':None}, guess = False, encoding = 'ISO-8859-1')
        # tabula.convert_into(os.path.join(filePath, file), os.path.join(filePath, file.replace('pdf', 'csv')), output_format="csv", lattice=True, stream = False,  guess = True,  pandas_options={'header':None}, encoding = 'utf-8',
                            # kwargs='tabula.jar', spreadsheet = False)
        pd = tabula.read_pdf(os.path.join(filePath, file), lattice=True, stream=False, guess=False,
                            pandas_options={'header': None, 'error_bad_lines':False}, encoding='cp1252',
                            kwargs='tabula.jar')
        print(pd)



def main():
    fileName = '20180316 Lagebericht_DE.pdf'
    remove_dir(fileName)
    split_page(fileName)
    # pdfContent = pyPdf.PdfFileReader(open("../../Data/20180316 Lagebericht_DE.pdf", 'rb'))
    # print(pdfContent.pa)
    print ('Done!')


if __name__ == '__main__':
    main()