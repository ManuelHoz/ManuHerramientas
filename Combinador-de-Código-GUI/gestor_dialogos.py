from tkinter import filedialog, simpledialog, messagebox
import os

class GestorDialogos:
    def seleccionar_directorio(self):
        directorio_inicial = os.getcwd()
        return filedialog.askdirectory(initialdir=directorio_inicial)

    def seleccionar_archivos(self, tipos_archivo):
        tipos_formato = [f"Archivos ({tipo})|{tipo}" for tipo in tipos_archivo]
        tipos_formato_str = " ".join(tipos_formato)
        return filedialog.askopenfilenames(
            title="Seleccionar Archivo(s)",
            filetypes=[(tipos_formato_str, tipos_archivo)]
        )

    def obtener_texto_cabecera(self):
        opcion = messagebox.askyesno("Texto de Cabecera", "¿Deseas escribir el texto manualmente?")
        if opcion:
            return simpledialog.askstring("Texto de Cabecera", "Introduce el texto de cabecera:")
        else:
            archivo_texto = filedialog.askopenfilename(filetypes=[("Archivos de Texto", "*.txt")], initialdir=os.getcwd())
            if archivo_texto:
                with open(archivo_texto, 'r') as archivo:
                    return archivo.read()
        return ""

    def obtener_nombre_archivo_salida(self):
        return simpledialog.askstring("Nombre del archivo", "Introduce el nombre del archivo de salida:")
