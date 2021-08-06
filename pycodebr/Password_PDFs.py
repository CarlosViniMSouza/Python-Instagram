# pip install pypdf2

from PyPDF2 import PdfFileWriter, PdfFileReader
import sys

def secure_pdf(file, pwd):
    parser = PdfFileWriter()
    pdf = PdfFileReader(file)

    for pg in range(pdf.numPages):
        parser.addPage(pdf.getPage(pg))

    parser.encrypt(pwd)

    with open(f"secure_{file}", "wb") as mark:
        parser.write(mark)
        mark.close()
    print(f"secure_{file} Created !")

if __name__ == "__main__":
    file = sys.argv[1]
    pwd = sys.argv[2]
    secure_pdf(file, pwd)
