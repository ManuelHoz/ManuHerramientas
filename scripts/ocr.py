import os
from PIL import Image
import pytesseract

# Asegúrate de que pytesseract pueda encontrar el ejecutable de Tesseract
# Si estás en Windows, puede que necesites especificar la ruta completa:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_from_image(image_path):
    # Abrir la imagen
    img = Image.open(image_path)
    
    # Configuración adicional para fórmulas matemáticas si es posible
    custom_config = r'--oem 3 --psm 3'
    
    # Usar pytesseract para hacer OCR en la imagen
    text = pytesseract.image_to_string(img, config=custom_config)
    
    return text

def process_images_in_directory(directory_path, output_file):
    # Listar todos los archivos en el directorio
    files = os.listdir(directory_path)
    
    # Filtrar solo las imágenes (puedes agregar más extensiones si lo necesitas)
    image_files = [f for f in files if f.lower().endswith(('png', 'jpg', 'jpeg', 'tiff', 'bmp'))]
    
    with open(output_file, 'w', encoding='utf-8') as f:
        for image_file in image_files:
            image_path = os.path.join(directory_path, image_file)
            print(f"Procesando imagen: {image_path}")
            text = ocr_from_image(image_path)
            f.write(f"Texto extraído de {image_file}:\n{text}\n\n")
            print(f"Texto extraído de {image_file}:\n{text}\n")
    
    print(f"Resultados guardados en {output_file}")

if __name__ == "__main__":
    # Obtener el directorio donde se encuentra este script
    directory_path = os.path.dirname(os.path.abspath(__file__))
    
    # Nombre del archivo de salida
    output_file = 'resultados_ocr.txt'
    
    process_images_in_directory(directory_path, output_file)
