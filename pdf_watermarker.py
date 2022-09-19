import sys
import PyPDF2

name_content_file = sys.argv[1]
name_watermark_file = sys.argv[2]
name_output_file = sys.argv[3]

content_file = PyPDF2.PdfFileReader(open(name_content_file, 'rb'))
watermark_file = PyPDF2.PdfFileReader(open(name_watermark_file, 'rb'))
watermark = watermark_file.getPage(0)
output_file = PyPDF2.PdfFileWriter()

for i in range(content_file.numPages):
    page = content_file.getPage(i)
    page.mergePage(watermark)
    output_file.addPage(page)

with open(name_output_file, 'wb') as file:
    output_file.write(file)
