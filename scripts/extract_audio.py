import os
from moviepy.editor import AudioFileClip, ColorClip

def convertir_audio_a_video(audio_file, output_dir, max_duration=20*60):
    try:
        print(f"Procesando archivo: {audio_file}")
        audio = AudioFileClip(audio_file)
        duracion = audio.duration

        if duracion > max_duration:
            dividir_y_guardar_audio_en_partes(audio, audio_file, output_dir, duracion, max_duration)
        else:
            crear_video_con_audio(audio, audio_file, output_dir, duracion)
    except Exception as e:
        print(f"Fallo al procesar {audio_file}: {e}")

def dividir_y_guardar_audio_en_partes(audio, audio_file, output_dir, duracion, max_duration):
    partes = int(duracion // max_duration) + 1
    for parte in range(partes):
        tiempo_inicio = parte * max_duration
        tiempo_final = min((parte + 1) * max_duration, duracion)
        audio_parte = audio.subclip(tiempo_inicio, tiempo_final)
        
        video = crear_video_con_audio(audio_parte, audio_file, output_dir, tiempo_final - tiempo_inicio, parte + 1)
        print(f"Creado video parte {parte + 1} para {audio_file} en {video}")

def crear_video_con_audio(audio, audio_file, output_dir, duracion, parte=None):
    video = ColorClip(size=(640, 480), color=(0, 0, 0), duration=duracion)
    video = video.set_audio(audio)
    
    if parte is not None:
        nombre_salida = f"{os.path.splitext(os.path.basename(audio_file))[0]}_parte{parte}.mp4"
    else:
        nombre_salida = f"{os.path.splitext(os.path.basename(audio_file))[0]}.mp4"
    
    archivo_salida = os.path.join(output_dir, nombre_salida)
    video.write_videofile(archivo_salida, codec='libx264', fps=24)
    return archivo_salida

def procesar_audios_en_directorio(directorio):
    try:
        print(f"Directorio: {directorio}")
        for nombre_archivo in os.listdir(directorio):
            print(f"Archivo encontrado: {nombre_archivo}")
            if nombre_archivo.lower().endswith(('.mp3', '.wav', '.ogg', '.flac', '.m4a')):
                ruta_audio = os.path.join(directorio, nombre_archivo)
                convertir_audio_a_video(ruta_audio, directorio)
            else:
                print(f"Archivo omitido: {nombre_archivo} (no es un archivo de audio)")
    except Exception as e:
        print(f"Error al procesar el directorio {directorio}: {e}")

if __name__ == "__main__":
    directorio = os.path.dirname(os.path.realpath(__file__))  # Obtener el directorio del script
    print(f"Directorio del script: {directorio}")
    procesar_audios_en_directorio(directorio)
