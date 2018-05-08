from io import StringIO
import PyPDF2 as pyPdf
# import docx2txt
import pdfminer
import os
# import xlrd
# from xlrd import open_workbook
from bs4 import BeautifulSoup as bs
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
# from tabula import re
import pandas as pd
import numpy as np


import mammoth
def readFile():
    pdfContent = pyPdf.PdfFileReader(open("../../Data/20140911 Lagebericht.pdf", 'rb'))
    # for page in range(0, pdfContent.getNumPages()):
    #     pageObj = pdfContent.getPage(page)
    #     print (str(page) + "=========================================================================== Page")
    #     print(pageObj.extractText())
    writeFile = open("write.txt", "w")
    for page in range(0, pdfContent.getNumPages()):
        outputFile = pyPdf.PdfFileWriter()
        outputFile.addPage(pdfContent.getPage(page))
        with open("../../Data/1/document-page%s.pdf" % page, "wb") as outputStream:
            outputFile.write(outputStream)
        # if (page == 4):
        #     print (pdfContent.xmpMetadata)
        #     print  (pdfContent.getPage(page).extractText() + "\n")
        #     writeFile.write(pdfContent.getPage(page).extractText() + "\n")
            # print (pdfContent.getPageNumber(2))
            # print (pdfContent.getPage(2).getPageNumber())
    # docFile = docx2txt.process("document-page4.docx")
    print ('Done!')

# def parserDocFile():
    # with open("document-page0.pdf", "rb") as file:
    #     parser = PDFParser(file)
    #     document = PDFDocument(parser)
    #     outline = document.get_outlines()
    #     for (level, title, des, a, se) in outline:
    #         print(level, title)
        # result = mammoth.convert_to_html(doc_file)
        # html = result.value
        # soup = bs(html)
        # prettyHTML = soup.prettify()
        # print(prettyHTML)
        # html_file = open("document-page0.html", "w")
        # html_file.write(prettyHTML)
        # html_file.close()
    # df = tabula.read_pdf("document-page0.pdf", encoding='utf-8', spreadsheet=True)
    # print (df)


# from pdfminer.pdfparser import PDFParser
# from pdfminer.pdfdocument import PDFDocument
# from pdfminer.pdfpage import PDFPage
# from pdfminer.pdfpage import PDFTextExtractionNotAllowed
# from pdfminer.pdfinterp import PDFResourceManager
# from pdfminer.pdfinterp import PDFPageInterpreter
# from pdfminer.pdfdevice import PDFDevice
#
# # Open a PDF file.
# fp = open('20140911 Lagebericht.pdf', 'rb')
# # Create a PDF parser object associated with the file object.
# parser = PDFParser(fp)
# # Create a PDF document object that stores the document structure.
# # Supply the password for initialization.
# document = PDFDocument(parser)
# print(document)
# # Check if the document allows text extraction. If not, abort.
# if not document.is_extractable:
#     raise PDFTextExtractionNotAllowed
# # Create a PDF resource manager object that stores shared resources.
# rsrcmgr = PDFResourceManager()
# # Create a PDF device object.
# device = PDFDevice(rsrcmgr)
# # Create a PDF interpreter object.
# interpreter = PDFPageInterpreter(rsrcmgr, device)
# # Process each page contained in the document.
# for page in PDFPage.create_pages(document):
#     print (interpreter.process_page(page))

def main():
    readFile()
    print ('Done!')
if __name__ == '__main__':
    main()