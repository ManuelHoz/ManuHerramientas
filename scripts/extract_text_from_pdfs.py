import os
from PyPDF2 import PdfReader
import genanki

def extract_text_from_pdfs(pdf_directory):
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
                    
                    # Crea el archivo de salida de texto
                    txt_filename = f"{os.path.splitext(filename)[0]}.txt"
                    txt_path = os.path.join(pdf_directory, txt_filename)
                    with open(txt_path, 'w', encoding='utf-8') as txt_file:
                        # Escribe la instrucción inicial en el archivo de texto
                        txt_file.write("En base al extracto del pdf de esta clase, crea un mazo anki de 40 preguntas, tanto de fórmulas, como conceptuales, con respuesta en un csv separado por ;. Este csv es para que yo lo copie y pegue y no para que lo descargue directamente.\n\n")
                        txt_file.write(pdf_text)
                    
                    # Crea un archivo CSV en blanco
                    csv_filename = f"{os.path.splitext(filename)[0]}.csv"
                    csv_path = os.path.join(pdf_directory, csv_filename)
                    with open(csv_path, 'w', encoding='utf-8') as csv_file:
                        pass
                    
                    # Crea un mazo Anki vacío
                    deck_name = os.path.splitext(filename)[0]
                    my_deck = genanki.Deck(
                        deck_id=hash(deck_name),
                        name=deck_name
                    )
                    
                    # Guarda el mazo Anki en un archivo .apkg
                    apkg_filename = f"{deck_name}.apkg"
                    apkg_path = os.path.join(pdf_directory, apkg_filename)
                    genanki.Package(my_deck).write_to_file(apkg_path)
                    
                    print(f"Procesado: {filename}")
            
            except Exception as e:
                print(f"Error al procesar el archivo {filename}: {e}")

# Directorio donde están los archivos PDF y donde se ejecuta el programa
pdf_directory = os.path.dirname(os.path.abspath(__file__))

# Llama a la función para extraer el texto de los PDFs
extract_text_from_pdfs(pdf_directory)
