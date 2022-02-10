# pip install PyPDF2 --> in Terminal

# Move Terminal Cursor to the folder where the files exist
# >cd .\07_PDFMerger

from PyPDF2 import PdfFileMerger

pdf_list = ['T1.pdf', 'T2.pdf', 'T3.pdf']


# Instance
merger = PdfFileMerger()

for pdf in pdf_list:
    merger.append(pdf)

merger.write("result.pdf")

print("File merged successfully!")