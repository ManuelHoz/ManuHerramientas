import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import os
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinterdnd2 import DND_FILES, TkinterDnD

class Vista:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Combinar Archivos")
        self.ventana.minsize(600, 500)

        # Colores y fuentes para la estética
        self.color_fondo = "lightgray"
        self.color_acento = "dodgerblue"
        self.fuente_titulo = ("Helvetica Neue", 16, "bold")
        self.fuente_normal = ("Helvetica Neue", 12)

        self.frame_principal = ttk.Frame(ventana, bootstyle="secondary", padding=10)
        self.frame_principal.pack(fill=tk.BOTH, expand=True, pady=10, padx=10)

        self.canvas = tk.Canvas(self.frame_principal, bg=self.color_fondo)
        self.scrollbar = ttk.Scrollbar(self.frame_principal, orient="vertical", command=self.canvas.yview)
        self.frame_canvas = ttk.Frame(self.canvas, bootstyle="secondary", padding=10)

        self.canvas.create_window((0, 0), window=self.frame_canvas, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.frame_canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Sección de texto de cabecera con tamaño fijo y scrollbar
        self.frame_texto_cabecera = ttk.Frame(self.frame_principal)
        self.frame_texto_cabecera.pack(fill=tk.X, padx=10, pady=5)

        self.canvas_texto_cabecera = tk.Canvas(self.frame_texto_cabecera, height=100, bg=self.color_fondo)
        self.scrollbar_texto_cabecera = ttk.Scrollbar(
            self.frame_texto_cabecera, orient="vertical", command=self.canvas_texto_cabecera.yview
        )
        self.frame_interior_texto_cabecera = ttk.Frame(self.canvas_texto_cabecera)

        self.canvas_texto_cabecera.create_window((0, 0), window=self.frame_interior_texto_cabecera, anchor="nw")
        self.canvas_texto_cabecera.configure(yscrollcommand=self.scrollbar_texto_cabecera.set)

        self.texto_cabecera = tk.Text(
            self.frame_interior_texto_cabecera,
            height=5,
            font=self.fuente_normal,
            wrap="word",
            bg=self.color_fondo,
            foreground="#333333",
            relief=tk.FLAT
        )
        self.texto_cabecera.pack(fill=tk.BOTH, expand=True)

        self.frame_interior_texto_cabecera.bind(
            "<Configure>", lambda e: self.canvas_texto_cabecera.configure(scrollregion=self.canvas_texto_cabecera.bbox("all"))
        )
        self.canvas_texto_cabecera.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar_texto_cabecera.pack(side=tk.RIGHT, fill=tk.Y)

        # Sección de botones principales
        self.frame_botones = ttk.Frame(self.frame_principal, padding=10)
        self.frame_botones.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

        self.boton_seleccionar_directorio = ttk.Button(
            self.frame_botones, text="Seleccionar Directorio", bootstyle="success-outline", padding=(10, 5)
        )
        self.boton_seleccionar_directorio.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
        self.boton_anadir_archivo = ttk.Button(
            self.frame_botones, text="Añadir Archivos", bootstyle="success-outline", padding=(10, 5)
        )
        self.boton_anadir_archivo.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        self.boton_agregar_texto = ttk.Button(
            self.frame_botones, text="Agregar Texto de Cabecera", bootstyle="info-outline", padding=(10, 5)
        )
        self.boton_agregar_texto.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
        self.boton_agregar_pdfs = ttk.Button(
            self.frame_botones, text="Agregar PDFs", bootstyle="info-outline", padding=(10, 5)
        )   
        self.boton_agregar_pdfs.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)


        self.boton_combinar = ttk.Button(
            self.frame_botones, text="Combinar Archivos", bootstyle="primary-outline", padding=(10, 5)
        )
        self.boton_combinar.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        self.boton_copiar = ttk.Button(
            self.frame_botones, text="Copiar al Portapapeles", bootstyle="warning-outline", padding=(10, 5)
        )
        self.boton_copiar.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        # Inicialización de frame_checkboxes antes de crear las checkboxes
        self.frame_checkboxes = ttk.Frame(self.frame_botones, padding=10)
        self.frame_checkboxes.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

        self.checkbox_pdf_var = tk.BooleanVar(value=False)
        self.checkbox_pdf = ttk.Checkbutton(self.frame_checkboxes, text="*.pdf", variable=self.checkbox_pdf_var, bootstyle="primary")
        self.checkbox_pdf.pack(side=tk.LEFT, padx=5)

        self.checkbox_py_var = tk.BooleanVar(value=True)
        self.checkbox_py = ttk.Checkbutton(self.frame_checkboxes, text="*.py", variable=self.checkbox_py_var, bootstyle="primary")
        self.checkbox_py.pack(side=tk.LEFT, padx=5)

        self.checkbox_txt_var = tk.BooleanVar(value=False)
        self.checkbox_txt = ttk.Checkbutton(self.frame_checkboxes, text="*.txt", variable=self.checkbox_txt_var, bootstyle="primary")
        self.checkbox_txt.pack(side=tk.LEFT, padx=5)

        self.checkbox_md_var = tk.BooleanVar(value=False)
        self.checkbox_md = ttk.Checkbutton(self.frame_checkboxes, text="*.md", variable=self.checkbox_md_var, bootstyle="primary")
        self.checkbox_md.pack(side=tk.LEFT, padx=5)

        self.checkbox_m_var = tk.BooleanVar(value=False)
        self.checkbox_m = ttk.Checkbutton(self.frame_checkboxes, text="*.m", variable=self.checkbox_m_var, bootstyle="primary")
        self.checkbox_m.pack(side=tk.LEFT, padx=5)

        # Registro de la ventana para Drag and Drop
        self.ventana.drop_target_register(DND_FILES)

    def get_tipos_archivo(self):
        tipos_archivo = []
        if self.checkbox_py_var.get():
            tipos_archivo.append("*.py")
        if self.checkbox_txt_var.get():
            tipos_archivo.append("*.txt")
        if self.checkbox_md_var.get():
            tipos_archivo.append("*.md")
        if self.checkbox_m_var.get():
            tipos_archivo.append("*.m")
        if self.checkbox_pdf_var.get():
            tipos_archivo.append("*.pdf")
        return tipos_archivo
        
    def mostrar_texto_cabecera(self, texto_mostrado):
        self.texto_cabecera.delete(1.0, tk.END)  # Borra el contenido actual del Text widget
        self.texto_cabecera.insert(tk.END, texto_mostrado)  # Inserta el nuevo texto

    def crear_widget_archivo(self, archivo, eliminar_func, mostrar_ruta_func, modificar_cabecera_func):
        frame_archivo = ttk.Frame(self.frame_canvas, bootstyle="secondary", padding=5)
        frame_archivo.pack(fill=tk.X, pady=2)

        label_archivo = ttk.Label(frame_archivo, text=os.path.basename(archivo), anchor="w", font=self.fuente_normal)
        label_archivo.pack(side=tk.LEFT, fill=tk.X, expand=True)
        label_archivo.bind("<Button-1>", lambda e: mostrar_ruta_func())

        boton_modificar_cabecera = ttk.Button(frame_archivo, text="Modificar Cabecera", command=modificar_cabecera_func, bootstyle="info-outline", padding=(5, 2))
        boton_modificar_cabecera.pack(side=tk.RIGHT)

        boton_eliminar = ttk.Button(frame_archivo, text="Eliminar", command=eliminar_func, bootstyle="danger-outline", padding=(5, 2))
        boton_eliminar.pack(side=tk.RIGHT)

        return frame_archivo

    def limpiar_listbox(self):
        for widget in self.frame_canvas.winfo_children():
            widget.destroy()
