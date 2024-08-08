import os
import nbformat

def extraer_contenido_notebook(archivo_notebook):
    """Extraer celdas de tipo markdown y código de un notebook Jupyter."""
    with open(archivo_notebook, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    contenido_extraido = []
    for celda in nb.cells:
        if celda.cell_type in ['markdown', 'code']:
            contenido_extraido.append(celda.source)
    
    return '\n\n'.join(contenido_extraido)

def procesar_notebooks_en_directorio(directorio, archivo_salida):
    """Procesar todos los notebooks en el directorio y guardar el contenido extraído."""
    with open(archivo_salida, 'w', encoding='utf-8') as output:
        for nombre_archivo in os.listdir(directorio):
            if nombre_archivo.endswith('.ipynb'):
                output.write(f"## {nombre_archivo}\n\n")
                contenido = extraer_contenido_notebook(nombre_archivo)
                output.write(contenido)
                output.write("\n\n" + "#" * 80 + "\n\n")
    print(f"Contenido extraído y guardado en {archivo_salida}")

def main():
    """Función principal para extraer y guardar el contenido de los notebooks."""
    directorio_actual = os.getcwd()  # Obtener el directorio actual
    archivo_salida = 'contenido_notebooks.txt'
    procesar_notebooks_en_directorio(directorio_actual, archivo_salida)

if __name__ == "__main__":
    main()
