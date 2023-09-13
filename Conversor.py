from pdf2docx import Converter
from docx2pdf import convert

# Definición de función para convertir un archivo PDF a Word.


def pdf_to_docx(pdf_file, docx_file):
    # Crea un objeto 'Converter' para convertir el PDF en Word.
    cv = Converter(pdf_file)
    # Realiza la conversión y guarda el resultado en un archivo Word.
    cv.convert(docx_file, start=0, end=None)
    # Cierra el objeto Converter después de la conversión.
    cv.close()

# Definición de función para convertir un archivo Word a PDF.


def docx_to_pdf(docx_file, pdf_file):
    # Utiliza la función 'convert' de 'docx2pdf' para realizar la conversión.
    convert(docx_file, pdf_file)
