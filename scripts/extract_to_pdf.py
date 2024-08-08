import os
from PyPDF2 import PdfReader

def obtener_nombre_siguiente_archivo(base_output_file, indice_archivo):
    """Genera el nombre del siguiente archivo de salida basado en el índice."""
    directorio, nombre_base = os.path.split(base_output_file)
    nombre, extension = os.path.splitext(nombre_base)
    return os.path.join(directorio, f"{nombre}_{indice_archivo}{extension}")

def procesar_archivo_pdf(pdf_path, outfile, max_lines_per_file, lines_written):
    """Procesa un archivo PDF, extrayendo su texto y escribiéndolo en el archivo de salida."""
    try:
        with open(pdf_path, 'rb') as archivo_pdf:
            lector_pdf = PdfReader(archivo_pdf)
            
            if lector_pdf.is_encrypted:
                print(f"El archivo {os.path.basename(pdf_path)} está encriptado y no se puede leer.")
                return lines_written
            
            texto_pdf = ''
            for pagina in lector_pdf.pages:
                texto_pdf += pagina.extract_text()

            lineas_pdf = texto_pdf.split('\n')

            for linea in lineas_pdf:
                if lines_written >= max_lines_per_file:
                    outfile.close()
                    return lines_written  # Retornar las líneas escritas para abrir un nuevo archivo
                
                outfile.write(f"{linea}\n")
                lines_written += 1

            outfile.write(f"Nombre del archivo: {os.path.basename(pdf_path)}\n")
            lines_written += 1

    except Exception as e:
        print(f"Error al procesar el archivo {os.path.basename(pdf_path)}: {e}")
    
    return lines_written

def extraer_texto_de_pdfs_en_directorio(pdf_directory, base_output_file, max_lines_per_file=500):
    """Extrae el texto de todos los archivos PDF en un directorio y lo guarda en archivos de salida."""
    indice_archivo = 1
    output_file = obtener_nombre_siguiente_archivo(base_output_file, indice_archivo)
    outfile = open(output_file, 'w', encoding='utf-8')
    lines_written = 0

    for filename in os.listdir(pdf_directory):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(pdf_directory, filename)
            lines_written = procesar_archivo_pdf(pdf_path, outfile, max_lines_per_file, lines_written)

            if lines_written >= max_lines_per_file:
                outfile.close()
                indice_archivo += 1
                output_file = obtener_nombre_siguiente_archivo(base_output_file, indice_archivo)
                outfile = open(output_file, 'w', encoding='utf-8')
                lines_written = 0

    outfile.close()
    
if __name__ == "__main__":
    pdf_directory = os.path.dirname(os.path.abspath(__file__))  # Obtener el directorio actual
    base_output_file = os.path.join(pdf_directory, 'output_pdf.txt')  # Nombre base del archivo de salida
    extraer_texto_de_pdfs_en_directorio(pdf_directory, base_output_file)  # Ejecutar la extracción de texto
