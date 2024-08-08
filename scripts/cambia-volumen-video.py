import os
from PIL import Image
from moviepy.editor import VideoFileClip

# Definir ANTIALIAS para compatibilidad
Image.Resampling = Image.Resampling if hasattr(Image, 'Resampling') else Image
Image.ANTIALIAS = Image.Resampling.LANCZOS if hasattr(Image.Resampling, 'LANCZOS') else Image.ANTIALIAS

# Obtener la ruta del directorio donde se encuentra el archivo de script
directorio = os.path.dirname(os.path.abspath(__file__))

# Factor de aumento del volumen (por ejemplo, 1.5 aumenta el volumen en un 50%)
factor_volumen = 3

# Iterar sobre todos los archivos en el directorio
for archivo in os.listdir(directorio):
    if archivo.endswith(('.mp4', '.avi', '.mov')):  # Puedes añadir más extensiones si es necesario
        ruta_video = os.path.join(directorio, archivo)
        
        # Cargar el video
        clip = VideoFileClip(ruta_video)
        
        # Aumentar el volumen
        if clip.audio:  # Asegurarse de que el video tenga pista de audio
            clip = clip.volumex(factor_volumen)
        
        # Guardar el video modificado
        ruta_guardar = os.path.join(directorio, 'modificado_' + archivo)
        clip.write_videofile(ruta_guardar, codec='libx264')
        
        print(f'Video procesado y guardado como {ruta_guardar}')

print('Procesamiento completo.')
