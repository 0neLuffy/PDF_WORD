from flask import Flask, request, render_template
from pdf2docx import Converter
from docx2pdf import convert
import os

# Importar las funciones desde Conversor.py
from Conversor import pdf_to_docx, docx_to_pdf

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        opcion = request.form['opcion']
        archivo = request.files['archivo']  # Obtener el archivo seleccionado.

        if archivo:
            # Obtener el nombre del archivo original.
            archivo_nombre = archivo.filename

            if opcion == 'pdf_to_docx':
                # Guardar el archivo temporalmente en el directorio actual.
                archivo_guardado = f"temp_{archivo_nombre}"
                archivo.save(archivo_guardado)

                # Realizar la conversión.
                pdf_to_docx(archivo_guardado,
                            f"{os.path.splitext(archivo_guardado)[0]}.docx")

                # Eliminar el archivo temporal.
                os.remove(archivo_guardado)

                return f'Se ha convertido el archivo {archivo_nombre} a Word.'

            elif opcion == 'docx_to_pdf':
                # Guardar el archivo temporalmente en el directorio actual.
                archivo_guardado = f"temp_{archivo_nombre}"
                archivo.save(archivo_guardado)

                # Realizar la conversión.
                docx_to_pdf(archivo_guardado,
                            f"{os.path.splitext(archivo_guardado)[0]}.pdf")

                # Eliminar el archivo temporal.
                os.remove(archivo_guardado)

                return f'Se ha convertido el archivo {archivo_nombre} a PDF.'

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
