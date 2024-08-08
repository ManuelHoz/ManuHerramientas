import os
import csv

# Función para obtener los archivos CSV en el directorio actual
def obtener_archivos_csv():
    archivos_csv = [archivo for archivo in os.listdir() if archivo.endswith('.csv')]
    return archivos_csv

# Función para leer las primeras 10 filas de un archivo CSV
def leer_csv(archivo_csv):
    with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
        lector = csv.reader(csvfile)
        filas = []
        for i, fila in enumerate(lector):
            if i < 10:
                filas.append(fila)
            else:
                break
    return filas

# Función para escribir las primeras 10 filas en un archivo de texto
def escribir_txt(archivo_txt, nombre_csv, filas):
    with open(archivo_txt, 'a', encoding='utf-8') as txtfile:
        txtfile.write(f"Nombre del archivo CSV: {nombre_csv}\n")
        for fila in filas:
            txtfile.write(','.join(fila) + '\n')
        txtfile.write('\n')  # Añadir una línea en blanco entre cada archivo CSV

# Programa principal
def main():
    archivos_csv = obtener_archivos_csv()
    if not archivos_csv:
        print("No se encontraron archivos CSV en el directorio actual.")
        return

    archivo_txt = 'output_csv.txt'
    # Limpiar el archivo de texto si ya existe
    if os.path.exists(archivo_txt):
        os.remove(archivo_txt)

    for archivo_csv in archivos_csv:
        filas = leer_csv(archivo_csv)
        escribir_txt(archivo_txt, archivo_csv, filas)

    print(f"Las primeras 10 filas de cada archivo CSV han sido escritas en {archivo_txt}")

if __name__ == "__main__":
    main()
