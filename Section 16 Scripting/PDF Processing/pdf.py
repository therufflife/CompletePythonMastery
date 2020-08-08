# PDF Processing
import PyPDF2

with open('dummy.pdf', 'rb') as file:       # 'rb' = read as binary
    reader = PyPDF2.PdfFileReader(file)
    # print(reader.getPage(1))
    # print(reader.numPages)
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)