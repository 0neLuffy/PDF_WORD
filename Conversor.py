from pdf2docx import Converter
from docx2pdf import convert


def pdf_to_docx(pdf_file, docx_file):
    """
    Convierte un archivo PDF en un archivo Word (.docx).

    Args:
        pdf_file (str): Ruta al archivo PDF de origen.
        docx_file (str): Ruta al archivo Word (.docx) de destino.

    Raises:
        Exception: Se lanza si ocurre un error durante la conversión.
    """
    try:
        # Crea un objeto 'Converter' para convertir el PDF en Word.
        cv = Converter(pdf_file)
        # Realiza la conversión y guarda el resultado en un archivo Word.
        cv.convert(docx_file, start=0, end=None)
    except Exception as e:
        raise e
    finally:
        # Cierra el objeto Converter después de la conversión.
        cv.close()


def docx_to_pdf(docx_file, pdf_file):
    """
    Convierte un archivo Word (.docx) en un archivo PDF.

    Args:
        docx_file (str): Ruta al archivo Word (.docx) de origen.
        pdf_file (str): Ruta al archivo PDF de destino.
    """
    try:
        # Utiliza la función 'convert' de 'docx2pdf' para realizar la conversión.
        convert(docx_file, pdf_file)
    except Exception as e:
        raise e
