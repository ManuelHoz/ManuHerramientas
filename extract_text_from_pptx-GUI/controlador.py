import os
from tkinter import filedialog, messagebox

class Controlador:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

        self.vista.boton_seleccionar_archivos.config(command=self.seleccionar_archivos)
        self.vista.boton_procesar.config(command=self.procesar_pdfs)

    def seleccionar_archivos(self):
        archivos = filedialog.askopenfilenames(filetypes=[("Archivos PDF", "*.pdf")], initialdir=os.getcwd())
        if archivos:
            self.modelo.agregar_archivos(archivos)
            self.vista.mostrar_lista_archivos(self.modelo.obtener_archivos())

    def procesar_pdfs(self):
        if not self.modelo.obtener_archivos():
            messagebox.showerror("Error", "Por favor selecciona al menos un archivo PDF.")
            return

        self.modelo.procesar_pdfs()
        messagebox.showinfo("Completado", "Se ha completado el procesamiento de los PDFs.")
