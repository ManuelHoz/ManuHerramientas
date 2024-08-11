import os
from PyPDF2 import PdfReader

def procesar_pdf(pdf_path):
    """Procesa un archivo PDF para extraer texto y crear archivos relacionados."""
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PdfReader(pdf_file)
            
            if pdf_reader.is_encrypted:
                print(f"El archivo {os.path.basename(pdf_path)} está encriptado y no se puede leer.")
                return

            texto_extraido = extraer_texto_de_pdf(pdf_reader)
            crear_archivo_texto(pdf_path, texto_extraido)
            crear_archivo_csv_vacio(pdf_path)
            crear_mazo_anki_vacio(pdf_path)
            
            print(f"Procesado: {os.path.basename(pdf_path)}")
    
    except Exception as e:
        print(f"Error al procesar el archivo {os.path.basename(pdf_path)}: {e}")

def extraer_texto_de_pdf(pdf_reader):
    """Extrae el texto de cada página de un archivo PDF."""
    texto = ''
    for pagina in pdf_reader.pages:
        texto += pagina.extract_text()
    return texto

def crear_archivo_texto(pdf_path, texto):
    """Crea un archivo de texto con el contenido extraído del PDF."""
    nombre_txt = f"{os.path.splitext(os.path.basename(pdf_path))[0]}.txt"
    ruta_txt = os.path.join(os.path.dirname(pdf_path), nombre_txt)
    
    with open(ruta_txt, 'w', encoding='utf-8') as txt_file:
        txt_file.write("En base al extracto del pdf de esta clase, crea un mazo anki de 40 preguntas, tanto de fórmulas, como conceptuales, con respuesta en un csv separado por ;. Este csv es para que yo lo copie y pegue y no para que lo descargue directamente.\n\n")
        txt_file.write(texto)

def crear_archivo_csv_vacio(pdf_path):
    """Crea un archivo CSV vacío en el mismo directorio que el PDF."""
    nombre_csv = f"{os.path.splitext(os.path.basename(pdf_path))[0]}.csv"
    ruta_csv = os.path.join(os.path.dirname(pdf_path), nombre_csv)
    
    with open(ruta_csv, 'w', encoding='utf-8') as csv_file:
        pass

def extraer_texto_de_pdfs_en_directorio(directorio_pdfs):
    """Recorre todos los archivos PDF en un directorio y los procesa."""
    for nombre_archivo in os.listdir(directorio_pdfs):
        if nombre_archivo.endswith('.pdf'):
            ruta_pdf = os.path.join(directorio_pdfs, nombre_archivo)
            procesar_pdf(ruta_pdf)

if __name__ == "__main__":
    directorio_pdfs = os.path.dirname(os.path.abspath(__file__))  # Obtener el directorio actual
    extraer_texto_de_pdfs_en_directorio(directorio_pdfs)

