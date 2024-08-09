import os
from PyPDF2 import PdfReader
import genanki

class Modelo:
    def __init__(self):
        self.archivos = []

    def agregar_archivos(self, archivos):
        self.archivos.extend(archivos)

    def obtener_archivos(self):
        return self.archivos

    def procesar_pdfs(self):
        for archivo in self.archivos:
            self._procesar_pdf(archivo)

    def _procesar_pdf(self, pdf_path):
        try:
            with open(pdf_path, 'rb') as pdf_file:
                pdf_reader = PdfReader(pdf_file)
                if pdf_reader.is_encrypted:
                    print(f"El archivo {os.path.basename(pdf_path)} está encriptado y no se puede leer.")
                    return

                texto_extraido = self._extraer_texto_de_pdf(pdf_reader)
                self._crear_archivo_texto(pdf_path, texto_extraido)
                self._crear_archivo_csv_vacio(pdf_path)

                print(f"Procesado: {os.path.basename(pdf_path)}")

        except Exception as e:
            print(f"Error al procesar el archivo {os.path.basename(pdf_path)}: {e}")

    def _extraer_texto_de_pdf(self, pdf_reader):
        texto = ''
        for pagina in pdf_reader.pages:
            texto += pagina.extract_text()
        return texto

    def _crear_archivo_texto(self, pdf_path, texto):
        nombre_txt = f"{os.path.splitext(os.path.basename(pdf_path))[0]}.txt"
        ruta_txt = os.path.join(os.path.dirname(pdf_path), nombre_txt)

        with open(ruta_txt, 'w', encoding='utf-8') as txt_file:
            txt_file.write("En base al extracto del pdf de esta clase, crea un mazo anki de 40 preguntas, tanto de fórmulas, como conceptuales, con respuesta en un csv separado por ;.\n\n")
            txt_file.write(texto)

    def _crear_archivo_csv_vacio(self, pdf_path):
        nombre_csv = f"{os.path.splitext(os.path.basename(pdf_path))[0]}.csv"
        ruta_csv = os.path.join(os.path.dirname(pdf_path), nombre_csv)

        with open(ruta_csv, 'w', encoding='utf-8') as csv_file:
            pass
