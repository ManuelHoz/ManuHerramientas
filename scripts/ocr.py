import os
from PIL import Image
import pytesseract

# Asegúrate de que pytesseract pueda encontrar el ejecutable de Tesseract
# Si estás en Windows, puede que necesites especificar la ruta completa:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def realizar_ocr_en_imagen(ruta_imagen):
    """Realiza OCR en una imagen y devuelve el texto extraído."""
    # Abrir la imagen
    img = Image.open(ruta_imagen)
    
    # Configuración adicional para fórmulas matemáticas si es posible
    configuracion_personalizada = r'--oem 3 --psm 3'
    
    # Usar pytesseract para hacer OCR en la imagen
    texto_extraido = pytesseract.image_to_string(img, config=configuracion_personalizada)
    
    return texto_extraido

def procesar_imagenes_en_directorio(ruta_directorio, archivo_salida):
    """Procesa todas las imágenes en un directorio, realiza OCR y guarda el texto en un archivo de salida."""
    # Listar todos los archivos en el directorio
    archivos = os.listdir(ruta_directorio)
    
    # Filtrar solo las imágenes (puedes agregar más extensiones si lo necesitas)
    archivos_imagenes = [archivo for archivo in archivos if archivo.lower().endswith(('png', 'jpg', 'jpeg', 'tiff', 'bmp'))]
    
    # Abre el archivo de salida para escribir los resultados
    with open(archivo_salida, 'w', encoding='utf-8') as archivo:
        for archivo_imagen in archivos_imagenes:
            ruta_imagen = os.path.join(ruta_directorio, archivo_imagen)
            print(f"Procesando imagen: {ruta_imagen}")
            
            # Realiza OCR en la imagen
            texto_extraido = realizar_ocr_en_imagen(ruta_imagen)
            
            # Escribe el texto extraído en el archivo de salida
            archivo.write(f"Texto extraído de {archivo_imagen}:\n{texto_extraido}\n\n")
            print(f"Texto extraído de {archivo_imagen}:\n{texto_extraido}\n")
    
    print(f"Resultados guardados en {archivo_salida}")

def main():
    """Función principal que coordina la extracción de texto de imágenes en un directorio."""
    # Obtener el directorio donde se encuentra este script
    ruta_directorio = os.path.dirname(os.path.abspath(__file__))
    
    # Nombre del archivo de salida
    archivo_salida = 'resultados_ocr.txt'
    
    # Procesa las imágenes en el directorio
    procesar_imagenes_en_directorio(ruta_directorio, archivo_salida)

if __name__ == "__main__":
    main()
