import tkinter as tk
from tkinter import filedialog, messagebox
import ttkbootstrap as ttk

class Vista:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Extractor de Texto de PDFs")
        self.ventana.minsize(500, 400)

        self.frame_principal = tk.Frame(ventana, bg="lightgray")
        self.frame_principal.pack(fill=tk.BOTH, expand=True, pady=10, padx=10)

        self.label_seleccion = tk.Label(self.frame_principal, text="Selecciona los archivos PDF:", bg="lightgray", font=("Helvetica Neue", 12))
        self.label_seleccion.pack(fill=tk.X, padx=10, pady=5)

        self.boton_seleccionar_archivos = ttk.Button(self.frame_principal, text="Seleccionar Archivos", bootstyle="success", padding=(10,5))
        self.boton_seleccionar_archivos.pack(fill=tk.X, padx=10, pady=5)

        self.lista_archivos = tk.Listbox(self.frame_principal, height=10)
        self.lista_archivos.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.boton_procesar = ttk.Button(self.frame_principal, text="Procesar PDFs", bootstyle="primary", padding=(10,5))
        self.boton_procesar.pack(fill=tk.X, padx=10, pady=5)

    def mostrar_lista_archivos(self, archivos):
        self.lista_archivos.delete(0, tk.END)
        for archivo in archivos:
            self.lista_archivos.insert(tk.END, archivo)
