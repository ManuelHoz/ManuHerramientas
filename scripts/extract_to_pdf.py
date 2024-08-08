import os
from PyPDF2 import PdfReader

def extract_text_from_pdfs(pdf_directory, base_output_file, max_lines_per_file=500):
    # Función auxiliar para obtener el nombre del siguiente archivo de salida
    def get_next_output_filename(base_output_file, file_index):
        directory, basename = os.path.split(base_output_file)
        name, ext = os.path.splitext(basename)
        return os.path.join(directory, f"{name}_{file_index}{ext}")
    
    # Inicializa el archivo de salida y el contador de líneas
    file_index = 1
    output_file = get_next_output_filename(base_output_file, file_index)
    outfile = open(output_file, 'w', encoding='utf-8')
    lines_written = 0

    # Recorre todos los archivos en el directorio dado
    for filename in os.listdir(pdf_directory):
        # Verifica si el archivo es un PDF
        if filename.endswith('.pdf'):
            # Construye la ruta completa al archivo PDF
            pdf_path = os.path.join(pdf_directory, filename)
            
            try:
                # Abre el archivo PDF
                with open(pdf_path, 'rb') as pdf_file:
                    # Crea un objeto de lectura de PDF
                    pdf_reader = PdfReader(pdf_file)
                    
                    # Verifica si el PDF se puede leer
                    if pdf_reader.is_encrypted:
                        print(f"El archivo {filename} está encriptado y no se puede leer.")
                        continue
                    
                    # Extrae texto de cada página del PDF
                    pdf_text = ''
                    for page in pdf_reader.pages:
                        pdf_text += page.extract_text()
                    
                    # Divide el texto extraído en líneas
                    pdf_lines = pdf_text.split('\n')
                    
                    # Escribe el nombre del archivo y su contenido en el archivo de salida
                    for line in pdf_lines:
                        if lines_written >= max_lines_per_file:
                            outfile.close()
                            file_index += 1
                            output_file = get_next_output_filename(base_output_file, file_index)
                            outfile = open(output_file, 'w', encoding='utf-8')
                            lines_written = 0
                        
                        outfile.write(f"{line}\n")
                        lines_written += 1
                    
                    # Asegurarse de que el nombre del archivo se escribe antes del contenido
                    if lines_written >= max_lines_per_file:
                        outfile.close()
                        file_index += 1
                        output_file = get_next_output_filename(base_output_file, file_index)
                        outfile = open(output_file, 'w', encoding='utf-8')
                        lines_written = 0
                        
                    outfile.write(f"Nombre del archivo: {filename}\n")
                    lines_written += 1

            except Exception as e:
                print(f"Error al procesar el archivo {filename}: {e}")

    outfile.close()

# Directorio donde están los archivos PDF y donde se ejecuta el programa
pdf_directory = os.path.dirname(os.path.abspath(__file__))
# Nombre base del archivo de salida
base_output_file = os.path.join(pdf_directory, 'output_pdf.txt')

# Llama a la función para extraer el texto de los PDFs
extract_text_from_pdfs(pdf_directory, base_output_file)
