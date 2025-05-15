from pdf2docx import Converter
pdf_file = 'Currículo Saulo.pdf'
docx_file = 'Curriculo Saulo.docx'
cv= Converter(pdf_file)
cv.convert(docx_file)
cv.close()