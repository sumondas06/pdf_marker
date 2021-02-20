import sys
import os
import PyPDF2

input1 = sys.argv[1]
input2 = sys.argv[2]

template = PyPDF2.PdfFileReader(open(input1, 'rb'))
watermark = PyPDF2.PdfFileReader(open(input2, 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    if not os.path.exists('new.pdf'):
        with open('new.pdf', 'wb') as new:
            output.write(new)
        print('done!')
    else:
        print('it exists!')
