import os

def procesar_archivo(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()

    # Contar los caracteres del archivo original
    caracteres_original = len(contenido)

    # Eliminar saltos de línea y reemplazar múltiples espacios por uno solo
    contenido_procesado = ' '.join(contenido.splitlines())
    contenido_procesado = ' '.join(contenido_procesado.split())

    # Contar los caracteres después del procesamiento
    caracteres_procesado = len(contenido_procesado)

    # Dividir el contenido procesado en partes de máximo 30,000 caracteres
    partes = [contenido_procesado[i:i+30000] for i in range(0, len(contenido_procesado), 15000)]

    # Guardar cada parte en un archivo nuevo
    base_nombre, ext = os.path.splitext(nombre_archivo)
    for indice, parte in enumerate(partes):
        nuevo_nombre = f"{base_nombre}_parte{indice+1}{ext}"
        with open(nuevo_nombre, 'w', encoding='utf-8') as archivo:
            archivo.write(parte)

    # Imprimir el informe de caracteres
    print(f"{nombre_archivo}:")
    print(f"  Caracteres originales: {caracteres_original}")
    print(f"  Caracteres procesados: {caracteres_procesado}")
    print(f"  Archivos procesados guardados como:")
    for indice in range(len(partes)):
        print(f"    {base_nombre}_parte{indice+1}{ext}")

def procesar_archivos_txt():
    # Obtener la lista de archivos en el directorio actual
    archivos = [archivo for archivo in os.listdir() if archivo.endswith('.txt')]

    for archivo in archivos:
        print(f"Procesando {archivo}...")
        procesar_archivo(archivo)
        print(f"{archivo} procesado correctamente.")

if __name__ == "__main__":
    procesar_archivos_txt()
