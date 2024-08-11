import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import Listbox, Scrollbar, END
import ttkbootstrap as ttk
from PyPDF2 import PdfReader

class ProcesadorPDF:
    def __init__(self, root):
        self.root = root
        self.root.title("Procesador de PDFs")
        self.root.geometry("600x400")
        self.root.resizable(True, True)  # Permite redimensionar la ventana
        
        self.archivos_seleccionados = []
        self.archivos_procesados = []  # Lista para almacenar los nombres de archivos procesados

        # Crear componentes de la interfaz
        self.label = ttk.Label(root, text="Seleccione archivos PDF para procesar:", font=("Helvetica", 12))
        self.label.pack(pady=10)

        self.frame_lista = ttk.Frame(root)
        self.frame_lista.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.lista_archivos = Listbox(self.frame_lista, selectmode=tk.SINGLE)
        self.lista_archivos.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = Scrollbar(self.frame_lista)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.lista_archivos.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.lista_archivos.yview)

        self.boton_agregar_archivos = ttk.Button(root, text="Agregar Archivos", command=self.seleccionar_archivos, bootstyle="primary-outline")
        self.boton_agregar_archivos.pack(fill=tk.X, padx=10, pady=5)

        self.boton_eliminar_archivo = ttk.Button(root, text="Eliminar Archivo", command=self.eliminar_archivo, bootstyle="danger-outline")
        self.boton_eliminar_archivo.pack(fill=tk.X, padx=10, pady=5)

        self.boton_extraer_archivo = ttk.Button(root, text="Extraer Seleccionado", command=self.extraer_seleccionado, bootstyle="success-outline")
        self.boton_extraer_archivo.pack(fill=tk.X, padx=10, pady=5)

        self.boton_extraer_todo = ttk.Button(root, text="Extraer Todo", command=self.extraer_todo, bootstyle="success")
        self.boton_extraer_todo.pack(fill=tk.X, padx=10, pady=20)

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)  # Llama a `on_close` cuando se cierra la ventana

    def seleccionar_archivos(self):
        archivos = filedialog.askopenfilenames(title="Seleccionar Archivos PDF", filetypes=[("Archivos PDF", "*.pdf")])
        for archivo in archivos:
            if archivo not in self.archivos_seleccionados:
                self.archivos_seleccionados.append(archivo)
                self.lista_archivos.insert(END, archivo)

    def eliminar_archivo(self):
        seleccion = self.lista_archivos.curselection()
        if seleccion:
            archivo = self.lista_archivos.get(seleccion)
            self.archivos_seleccionados.remove(archivo)
            self.lista_archivos.delete(seleccion)

    def extraer_seleccionado(self):
        seleccion = self.lista_archivos.curselection()
        if seleccion:
            archivo = self.lista_archivos.get(seleccion)
            self.procesar_pdf(archivo)
            self.archivos_seleccionados.remove(archivo)
            self.lista_archivos.delete(seleccion)

    def extraer_todo(self):
        total_archivos = len(self.archivos_seleccionados)
        while self.archivos_seleccionados:
            archivo = self.archivos_seleccionados.pop(0)
            self.procesar_pdf(archivo)
            self.lista_archivos.delete(0)
        
        # Preguntar al usuario si desea finalizar después de procesar todos los archivos
        if total_archivos > 0 and not self.archivos_seleccionados:
            if messagebox.askyesno("Finalizar", "¿Desea finalizar el procesamiento?"):
                self.on_close()  # Llama a `on_close` para guardar los archivos y cerrar la aplicación

    def procesar_pdf(self, pdf_path):
        try:
            output_dir = os.path.join(os.path.dirname(pdf_path), "pdf_extraidos")
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)

            with open(pdf_path, 'rb') as pdf_file:
                pdf_reader = PdfReader(pdf_file)

                if pdf_reader.is_encrypted:
                    messagebox.showwarning("Archivo Encriptado", f"El archivo {os.path.basename(pdf_path)} está encriptado y no se puede leer.")
                    return

                texto_extraido = self.extraer_texto_de_pdf(pdf_reader)
                ruta_txt = self.crear_archivo_texto(pdf_path, texto_extraido, output_dir)
                self.archivos_procesados.append(ruta_txt)  # Añadir la ruta del archivo procesado
                
                messagebox.showinfo("Procesado", f"Procesado: {os.path.basename(pdf_path)}")

        except Exception as e:
            messagebox.showerror("Error", f"Error al procesar el archivo {os.path.basename(pdf_path)}: {e}")

    def extraer_texto_de_pdf(self, pdf_reader):
        texto = ''
        for pagina in pdf_reader.pages:
            texto += pagina.extract_text()
        return texto

    def crear_archivo_texto(self, pdf_path, texto, output_dir):
        nombre_txt = f"{os.path.splitext(os.path.basename(pdf_path))[0]}.txt"
        ruta_txt = os.path.join(output_dir, nombre_txt)

        with open(ruta_txt, 'w', encoding='utf-8') as txt_file:
            txt_file.write("En base al extracto del pdf de esta clase, crea un mazo anki de 40 preguntas, tanto de fórmulas, como conceptuales, con respuesta en un csv separado por ;. Este csv es para que yo lo copie y pegue y no para que lo descargue directamente.\n\n")
            txt_file.write(texto)
        
        return ruta_txt

    def on_close(self):
        """Función que se ejecuta al cerrar la ventana. Guarda las rutas de los archivos procesados y los pasa al programa principal."""
        with open("archivos_procesados.txt", 'w') as f:
            for ruta in self.archivos_procesados:
                f.write(f"{ruta}\n")
        self.root.destroy()  # Cierra la ventana

def crear_interfaz():
    root = ttk.Window(themename="flatly")
    app = ProcesadorPDF(root)
    root.mainloop()

if __name__ == "__main__":
    crear_interfaz()
