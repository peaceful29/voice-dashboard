import tabula
import pandas as pd
import numpy as np
import sys
import errno
import os
import PyPDF2 as pyPdf
import shutil
from pandas.io.common import EmptyDataError
import datetime

pd.set_option('display.max_colwidth', -1)

# DATA_PATH = '../../Data/'
# # Read pdf into DataFrame
#
# # tabula.convert_into("../../Data/document-page3.pdf", "../../Data/page3.csv", output_format="csv", Lattice=True, pandas_options={'header':None}, guess = False, encoding = 'ISO-8859-1')
# # tabula.convert_into("../../Data/document-page3.pdf", "../../Data/page3.json", output_format="json", encoding = 'ISO-8859-1')
#
# # print (df)
# # df = tabula.read_pdf("../../Data/document-page3.pdf", output_format="csv", encoding = 'ISO-8859-1', Lattice=True, pandas_options={'header':None, 'error_bad_lines':False}, guess = False)
# # print (df[0])
# # df.to_csv("../../Data/document-page3.csv")
# # Read remote pdf into DataFrame
# # df2 = tabula.read_pdf("document-page0.pdf")
#
# # convert PDF into CSV
# # tabula.convert_into("test.pdf", "output.csv", output_format="csv")
#
# # convert all PDFs in a directory
# # tabula.convert_into_by_batch("input_directory", output_format='csv')
# header = ['Nr', 'Datum', 'Themen', 'Veröffentlicht', 'Risiko', 'Betroffene Systeme', 'Links', 'Tags', 'Sachstand']
#
# def remove_dir(fileName):
#     filePath = os.path.join(DATA_PATH, fileName.split('.')[0])
#     if os.path.exists(filePath):
#         shutil.rmtree(filePath)
#
#
# def split_page(fileName):
#     pdfContent = pyPdf.PdfFileReader(open(os.path.join(DATA_PATH, fileName), 'rb'))
#     filePath = os.path.join(DATA_PATH, fileName.split('.')[0])
#     if not os.path.exists(filePath):
#         print ('vao 1')
#         try:
#             os.makedirs(filePath)
#         except OSError as exc:  # Guard against race condition
#             if exc.errno != errno.EEXIST:
#                 raise
#     for page in range (pdfContent.getNumPages()):
#         # content = pdfContent.getPage(page)
#         # filePath = os.path.join(DATA_PATH, fileName, 'page', str(page))
#         outputFile = pyPdf.PdfFileWriter()
#         outputFile.addPage(pdfContent.getPage(page))
#         with open(os.path.join(filePath, 'page_' + str(page) + '.pdf'), "wb") as outputStream:
#             outputFile.write(outputStream)
#     convert_to_csv(filePath)
#
#
# def convert_to_csv(filePath):
#     for file in os.listdir(filePath):
#         print(file)
#         tabula.convert_into(os.path.join(filePath, file), os.path.join(filePath, file.replace('pdf', 'csv')), output_format="csv", lattice=True, stream=False, guess=False,
#                              pandas_options={'header': None, 'error_bad_lines': False}, encoding='ISO-8859-1',
#                              kwargs='tabula.jar')
#         # tabula.convert_into(os.path.join(filePath, file), os.path.join(filePath, file.replace('pdf', 'csv')), output_format="csv", lattice=True, stream = False,  guess = False,
#         #                     pandas_options={'header': None, 'error_bad_lines':False}, encoding = 'cp1252',
#         #                     kwargs='tabula.jar')
#         # pd = tabula.read_pdf(os.path.join(filePath, file), lattice=False, guess=True,
#         #                     pandas_options={'header': None, 'error_bad_lines':False}, encoding='cp1252', kwargs='tabula.jar')
#         # pd = tabula.read_pdf(os.path.join(filePath, file), output_format="csv", encoding='ISO-8859-1', Lattice=True,
#         #                 pandas_options={'header': None,'error_bad_lines': False}, guess=False, spreadsheet = False)
#         # df = tabula.read_pdf(os.path.join(filePath, file), lattice=True, stream=False, guess=False, output_format='dataFrame',
#         #                      pandas_options={'header': None, 'error_bad_lines': False}, encoding='ISO-8859-1',
#         #                      kwargs='tabula.jar')
#         # df_1 = pd.DataFrame(df)
#         # print(df_1.iloc[[0][0]])
#         # print(df.iloc[[2][0]])
#         # pd.savetxt(os.path.join(filePath, file + '.txt'), pd.values)
#         # pd.to_csv(os.path.join(filePath, file + '1.csv'), index=False, sep=' ', header=None)
#
#
#
#
# def main():
#     fileName = '20150109_lagebericht.pdf'
#     remove_dir(fileName)
#     split_page(fileName)
#     # pdfContent = pyPdf.PdfFileReader(open("../../Data/20180316 Lagebericht_DE.pdf", 'rb'))
#     # print(pdfContent.pa)
#     print ('Done!')
#
#
# if __name__ == '__main__':
#     main()
#

# def string_clean(str):
#     return str.split('Risiko')[1].replace('\\r', ' ').replace('dtype: object', '').split('Name:')[0].replace('  ', '').replace('\\n', ' ')
# 
# for file in os.listdir('../../Data/20150109_lagebericht'):
#     print('page_0' not in file)
#     if (('.csv' in file) and ('page_0' not in file) and ('page_1' not in file)):
#         print(file)
#         print(os.path.join('../../Data/20150109_lagebericht',file))
#         try:
#             df_1 = pd.read_csv(os.path.join('../../Data/20150109_lagebericht', file), encoding='ISO-8859-1',
#                                error_bad_lines=False)
#         except EmptyDataError:
#             df_1 = pd.DataFrame()
#         print (df_1.shape)
#         if ((df_1.empty == False) and (df_1.shape[0] > 4)):
#             print(string_clean(str(df_1.iloc[[2][0]])))
    # if ((df_1.empty == False) and ('Quellen:' in str(df_1.iloc[[5][0]])) and ('Sachstand:' in str(df_1.iloc[[2][0]]))):
    #         print(string_clean(str(df_1.iloc[[5][0]]).split('Quellen:')[1]))
            # print(str(df_1.iloc[[2][0]]).split('Bewertung:')[1].split('Risiko')[1].replace('\\r', ' ').replace('dtype: object', ''))
            # print(str(df_1.iloc[[3][0]]).split('Empfehlung:')[1].split('Risiko')[1].replace('\\r', ' ').replace('dtype: object', ''))
            # print(string_clean(str(df_1.iloc[[2][0]]).split('Sachstand:')[1]))


pd = tabula.read_pdf('../../Data/20150109_lagebericht/page_3.pdf', stream=True, guess=False, output_format='dataFrame',
                             pandas_options={'header': None, 'error_bad_lines': False}, encoding='cp1252')
# print (pd[0].to_string(index=False))
txt_full = (pd[0].to_string(index=False))
# print (txt_full)

title = txt_full.split("Risiko")[0]
count = title.count('\n')
title = title.split('\n')[count-1]
sachstand = txt_full.split("Sachstand: ")[1].split('Bewertung:')[0].replace('\n','').replace('  ','')
# print(txt_full)

datum = title[0:10][:-1]
print (title[10])
dt = datetime.datetime.strptime('20120209', "%Y%m%d").date()
print(dt)
check_arr = ['Titel', 'Sachstand', 'Bewertung', 'Empfehlung', 'Quellen']
print (all(x in txt_full for x in check_arr))
# for txt, line in title:
#     print(line)
# sachstand = pd.to_string(index=False).split("Sachstand: ")[1].split('Bewertung:')[0]
# print(sachstand)
