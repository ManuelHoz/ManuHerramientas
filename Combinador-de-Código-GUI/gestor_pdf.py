from PyPDF2 import PdfReader

class GestorPDF:
    def __init__(self, archivo):
        self.archivo = archivo

    def extraer_texto(self):
        texto = ""
        try:
            with open(self.archivo, "rb") as file:
                reader = PdfReader(file)
                num_pages = len(reader.pages)
                if num_pages == 0:
                    print("El archivo PDF está vacío o no tiene páginas.")
                for i, page in enumerate(reader.pages):
                    page_text = page.extract_text()
                    if page_text:
                        texto += page_text
                    else:
                        print(f"No se pudo extraer texto de la página {i}.")
        except Exception as e:
            print(f"Error al leer el archivo PDF {self.archivo}: {e}")
        return texto
