from PyPDF2 import PdfFileMerger
from glob import glob
try:
    PDF_raw_files = glob("*.pdf")
    print(PDF_raw_files)
    pdfs = PDF_raw_files
    name = input("Filename: ")+str(".pdf")
    merger = PdfFileMerger()
except:
    pass

try:
    for pdf in pdfs:
        merger.append(pdf)
except:
    print('There is some error with one of your *.pdf file or used library cannot merge ithem that is inside the file.')

try:
    merger.write(name)
    merger.close()
except:
    pass
input("Press enter to exit")
