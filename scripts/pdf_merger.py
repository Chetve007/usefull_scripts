from PyPDF2 import PdfMerger


merger = PdfMerger()
for pdf in ["file1.pdf", "file2.pdf"]:
    merger.append(pdf)
merger.write("merged.pdf")
