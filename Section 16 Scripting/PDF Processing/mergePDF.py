import PyPDF2
import sys
import os

inputs = sys.argv[2:]
watermark = sys.argv[1]

def pdf_combine(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')

def pdf_watermark(pdf_list, my_watermark):
    # with open(f'{my_watermark}', 'rb') as file:
    #     watermark = PyPDF2.PdfFileReader(file)
    watermark = PyPDF2.PdfFileReader(open(f'{my_watermark}', 'rb'))

    for pdf in pdf_list:
        writer = PyPDF2.PdfFileWriter()
        # with open(f'{pdf}', 'rb') as file:
        #     merger = PyPDF2.PdfFileReader(file)
        merger = PyPDF2.PdfFileReader(open(f'{pdf}', 'rb'))

        for i in range(merger.getNumPages()):
            page = merger.getPage(i)
            page.mergePage(watermark.getPage(0))
            writer.addPage(page)

        clean_name = os.path.splitext(pdf)[0]
        with open(f'{clean_name}_marked.pdf', 'wb') as new_file:
            writer.write(new_file)

pdf_watermark(inputs, watermark)