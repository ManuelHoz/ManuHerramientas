import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import os  # Agrega esta línea para importar el módulo os
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinterdnd2 import DND_FILES, TkinterDnD

class Vista:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Combinar Archivos Python")
        self.ventana.minsize(600, 400)

        self.frame_principal = tk.Frame(ventana, bg="lightgray")
        self.frame_principal.pack(fill=tk.BOTH, expand=True, pady=10, padx=10)

        self.canvas = tk.Canvas(self.frame_principal, bg="lightgray")
        self.scrollbar = tk.Scrollbar(self.frame_principal, orient="vertical", command=self.canvas.yview)
        self.frame_canvas = tk.Frame(self.canvas, bg="lightgray")

        self.canvas.create_window((0, 0), window=self.frame_canvas, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.frame_canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.label_texto_cabecera = tk.Label(self.frame_principal, text="", anchor="w", justify="left", bg="lightgray", wraplength=580, font=("Helvetica Neue", 12, "italic"))
        self.label_texto_cabecera.pack(fill=tk.X, padx=10, pady=5)

        self.frame_botones = tk.Frame(self.frame_principal, bg="lightgray")
        self.frame_botones.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

        self.boton_seleccionar_directorio = ttk.Button(self.frame_botones, text="Seleccionar Directorio", bootstyle="success", padding=(10,5))
        self.boton_seleccionar_directorio.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        self.boton_añadir_archivo = ttk.Button(self.frame_botones, text="Añadir Archivo", bootstyle="success", padding=(10,5))
        self.boton_añadir_archivo.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        self.boton_agregar_texto = ttk.Button(self.frame_botones, text="Agregar Texto de Cabecera", bootstyle="info", padding=(10,5))
        self.boton_agregar_texto.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        self.boton_combinar = ttk.Button(self.frame_botones, text="Combinar Archivos", bootstyle="success", padding=(10,5))
        self.boton_combinar.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        self.boton_copiar = ttk.Button(self.frame_botones, text="Copiar al Portapapeles", bootstyle="warning", padding=(10,5))
        self.boton_copiar.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        self.frame_principal.drop_target_register(DND_FILES)
    
    def mostrar_texto_cabecera(self, texto_mostrado):
        self.label_texto_cabecera.config(text=texto_mostrado)

    def crear_widget_archivo(self, archivo, eliminar_func, mostrar_ruta_func):
        frame_archivo = tk.Frame(self.frame_canvas, bg="lightgray", padx=10, pady=5)
        frame_archivo.pack(fill=tk.X, pady=2)

        label_archivo = tk.Label(frame_archivo, text=os.path.basename(archivo), anchor="w", font=("Helvetica Neue", 12), bg="lightgray", wraplength=400)
        label_archivo.pack(side=tk.LEFT, expand=True, fill=tk.X)

        boton_eliminar = ttk.Button(frame_archivo, text="Eliminar", command=eliminar_func, bootstyle="danger", padding=(5,5))
        boton_eliminar.pack(side=tk.RIGHT, padx=5)

        boton_mostrar_ruta = ttk.Button(frame_archivo, text="Mostrar Ruta Completa", command=mostrar_ruta_func, bootstyle="info", padding=(5,5))
        boton_mostrar_ruta.pack(side=tk.RIGHT, padx=5)

        return frame_archivo

    def limpiar_listbox(self):
        for widget in self.frame_canvas.winfo_children():
            widget.destroy()
