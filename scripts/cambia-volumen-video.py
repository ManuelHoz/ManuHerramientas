import os
from moviepy.editor import VideoFileClip

def obtener_directorio_actual():
    # Obtener la ruta del directorio donde se encuentra el archivo de script
    return os.path.dirname(os.path.abspath(__file__))

def aumentar_volumen_video(ruta_video, factor_volumen):
    # Cargar el video
    clip = VideoFileClip(ruta_video)
    
    # Aumentar el volumen si el video tiene pista de audio
    if clip.audio:
        clip = clip.volumex(factor_volumen)
    
    return clip

def procesar_videos(directorio, factor_volumen):
    # Iterar sobre todos los archivos en el directorio
    for archivo in os.listdir(directorio):
        if archivo.endswith(('.mp4', '.avi', '.mov')):  # Puedes añadir más extensiones si es necesario
            ruta_video = os.path.join(directorio, archivo)
            
            # Aumentar el volumen del video
            clip_modificado = aumentar_volumen_video(ruta_video, factor_volumen)
            
            # Guardar el video modificado
            ruta_guardar = os.path.join(directorio, 'modificado_' + archivo)
            clip_modificado.write_videofile(ruta_guardar, codec='libx264')
            
            print(f'Video procesado y guardado como {ruta_guardar}')
    
    print('Procesamiento completo.')

if __name__ == "__main__":
    directorio = obtener_directorio_actual()
    factor_volumen = 3
    procesar_videos(directorio, factor_volumen)
