from pdf2docx import Converter
pdf_file = 'CV - Letícia - Cabo Frio.pdf'
docx_file = 'CV - Letícia - Cabo Frio.docx'
cv= Converter(pdf_file)
cv.convert(docx_file)
cv.close()