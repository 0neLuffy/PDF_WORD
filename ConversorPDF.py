# Importa la biblioteca 'os' para trabajar con funciones del sistema operativo,
# 'pdf2docx' para convertir PDF a Word y 'docx2pdf' para convertir Word a PDF.
import os
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


# Entrada principal del programa.
if __name__ == "__main__":
    # Muestra las opciones al usuario.
    print("1. Convertir todos los PDF a Word en la carpeta")
    print("2. Convertir todos los Word a PDF en la carpeta")
    # Solicita la elección del usuario (1 o 2).
    choice = input("Selecciona una opción (1/2): ")

    # Si el usuario elige 1, realizar conversión de PDF a Word.
    if choice == "1":
        # Itera sobre los archivos en el directorio actual.
        for filename in os.listdir('.'):
            # Verifica si el nombre del archivo termina con '.pdf'.
            if filename.endswith('.pdf'):
                # Llama a la función 'pdf_to_docx' para realizar la conversión.
                pdf_to_docx(filename, f"{os.path.splitext(filename)[0]}.docx")
                # Muestra un mensaje indicando que la conversión ha sido completada.
                print(f"¡Conversión de {filename} completada!")

    # Si el usuario elige 2, realizar conversión de Word a PDF.
    elif choice == "2":
        # Itera sobre los archivos en el directorio actual.
        for filename in os.listdir('.'):
            # Verifica si el nombre del archivo termina con '.docx'.
            if filename.endswith('.docx'):
                # Llama a la función 'docx_to_pdf' para realizar la conversión.
                docx_to_pdf(filename, f"{os.path.splitext(filename)[0]}.pdf")
                # Muestra un mensaje indicando que la conversión ha sido completada.
                print(f"¡Conversión de {filename} completada!")

    # Si el usuario elige otra opción, muestra un mensaje de error.
    else:
        print("Opción no válida. Por favor, selecciona 1 o 2.")
