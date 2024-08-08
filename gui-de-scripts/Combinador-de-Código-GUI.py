import os
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinterdnd2 import DND_FILES, TkinterDnD

class Aplicacion:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Combinar Archivos Python")

        # Configurar tamaño mínimo de la ventana
        self.ventana.minsize(600, 400)

        self.lista_archivos = []
        self.widgets_archivos = {}
        self.mostrando_ruta_completa = {}
        self.texto_cabecera = ""

        # Configuración de estilo
        estilo = ttk.Style()
        estilo.configure('TButton', font=("Helvetica Neue", 12))

        # Frame principal con fondo gris claro
        self.frame_principal = tk.Frame(ventana, bg="lightgray")
        self.frame_principal.pack(fill=tk.BOTH, expand=True, pady=10, padx=10)

        # Crear Canvas y Scrollbar para la lista de archivos
        self.canvas = tk.Canvas(self.frame_principal, bg="lightgray")
        self.scrollbar = tk.Scrollbar(self.frame_principal, orient="vertical", command=self.canvas.yview)
        self.frame_canvas = tk.Frame(self.canvas, bg="lightgray")

        self.canvas.create_window((0, 0), window=self.frame_canvas, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Empaquetar los widgets de Canvas y Scrollbar
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Configurar el Frame dentro del Canvas
        self.frame_canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Label para mostrar el texto de cabecera
        self.label_texto_cabecera = tk.Label(self.frame_principal, text="", anchor="w", justify="left", bg="lightgray", wraplength=580, font=("Helvetica Neue", 12, "italic"))
        self.label_texto_cabecera.pack(fill=tk.X, padx=10, pady=5)

        # Frame para los botones que estarán en la parte inferior
        self.frame_botones = tk.Frame(self.frame_principal, bg="lightgray")
        self.frame_botones.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

        # Botones redondeados con estilo aplicado
        self.boton_seleccionar_directorio = ttk.Button(
            self.frame_botones, text="Seleccionar Directorio", 
            command=self.seleccionar_directorio, 
            bootstyle="success-round-outline", 
            padding=(10,5),
            style='TButton'
        )
        self.boton_seleccionar_directorio.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        self.boton_añadir_archivo = ttk.Button(
            self.frame_botones, text="Añadir Archivo", 
            command=self.añadir_archivo, 
            bootstyle="success-round-outline", 
            padding=(10,5),
            style='TButton'
        )
        self.boton_añadir_archivo.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        self.boton_agregar_texto = ttk.Button(
            self.frame_botones, text="Agregar Texto de Cabecera", 
            command=self.agregar_texto, 
            bootstyle="info-round-outline", 
            padding=(10,5),
            style='TButton'
        )
        self.boton_agregar_texto.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        self.boton_combinar = ttk.Button(
            self.frame_botones, text="Combinar Archivos", 
            command=self.combinar_archivos, 
            bootstyle="success-round-outline", 
            padding=(10,5),
            style='TButton'
        )
        self.boton_combinar.pack(side=tk.TOP, fill=tk.X, padx=10, pady=20)

        # Habilitar DnD en el frame principal
        self.frame_principal.drop_target_register(DND_FILES)
        self.frame_principal.dnd_bind('<<Drop>>', self.archivos_arrastrados)

    def seleccionar_directorio(self):
        directorio_inicial = os.getcwd()
        directorio = filedialog.askdirectory(initialdir=directorio_inicial)
        if directorio:
            archivos = [os.path.join(directorio, f) for f in os.listdir(directorio) if f.endswith('.py')]
            self.lista_archivos.extend(archivos)
            self.actualizar_listbox()

    def añadir_archivo(self):
        archivo = filedialog.askopenfilename(filetypes=[("Archivos Python", "*.py")], initialdir=os.getcwd())
        if archivo:
            self.lista_archivos.append(archivo)
            self.actualizar_listbox()

    def agregar_texto(self):
        opcion = messagebox.askyesno("Texto de Cabecera", "¿Deseas escribir el texto manualmente?")
        if opcion:
            self.texto_cabecera = simpledialog.askstring("Texto de Cabecera", "Introduce el texto de cabecera:")
        else:
            archivo_texto = filedialog.askopenfilename(filetypes=[("Archivos de Texto", "*.txt")], initialdir=os.getcwd())
            if archivo_texto:
                with open(archivo_texto, 'r') as archivo:
                    self.texto_cabecera = archivo.read()

        # Mostrar las primeras 100 palabras del texto de cabecera
        self.mostrar_texto_cabecera()

    def mostrar_texto_cabecera(self):
        palabras = self.texto_cabecera.split()
        texto_mostrado = ' '.join(palabras[:100])
        if len(palabras) > 100:
            texto_mostrado += "..."
        self.label_texto_cabecera.config(text=texto_mostrado)

    def eliminar_archivo(self, archivo):
        if archivo in self.lista_archivos:
            self.lista_archivos.remove(archivo)
            self.widgets_archivos[archivo].destroy()
            del self.widgets_archivos[archivo]
            del self.mostrando_ruta_completa[archivo]

    def mostrar_ruta_completa(self, archivo):
        # Alternar entre mostrar la ruta completa y solo el nombre del archivo
        if archivo in self.widgets_archivos:
            frame_archivo = self.widgets_archivos[archivo]
            label_archivo = frame_archivo.nametowidget(frame_archivo.winfo_children()[0])
            if self.mostrando_ruta_completa[archivo]:
                label_archivo.config(text=os.path.basename(archivo))
                self.mostrando_ruta_completa[archivo] = False
            else:
                label_archivo.config(text=archivo)
                self.mostrando_ruta_completa[archivo] = True
                # Asegurar que el texto largo se ajuste al ancho del label
                label_archivo.config(wraplength=400)  # Ajustar según sea necesario

    def actualizar_listbox(self):
        # Eliminar todos los widgets existentes en el frame canvas
        for widget in self.frame_canvas.winfo_children():
            widget.destroy()

        for archivo in self.lista_archivos:
            if archivo not in self.widgets_archivos:
                self.mostrando_ruta_completa[archivo] = False
                frame_archivo = tk.Frame(self.frame_canvas, bg="lightgray", padx=10, pady=5)
                frame_archivo.pack(fill=tk.X, pady=2)

                label_archivo = tk.Label(frame_archivo, text=os.path.basename(archivo), anchor="w", font=("Helvetica Neue", 12), bg="lightgray", wraplength=400)
                label_archivo.pack(side=tk.LEFT, expand=True, fill=tk.X)

                boton_eliminar = ttk.Button(
                    frame_archivo, text="Eliminar", 
                    command=lambda archivo=archivo: self.eliminar_archivo(archivo), 
                    bootstyle="danger-round-outline", 
                    padding=(5,5),
                    style='TButton'
                )
                boton_eliminar.pack(side=tk.RIGHT, padx=5)

                boton_mostrar_ruta = ttk.Button(
                    frame_archivo, text="Mostrar Ruta Completa", 
                    command=lambda archivo=archivo: self.mostrar_ruta_completa(archivo), 
                    bootstyle="info-round-outline", 
                    padding=(5,5),
                    style='TButton'
                )
                boton_mostrar_ruta.pack(side=tk.RIGHT, padx=5)

                self.widgets_archivos[archivo] = frame_archivo

    def archivos_arrastrados(self, event):
        archivos = self.ventana.tk.splitlist(event.data)
        for archivo in archivos:
            if archivo.endswith('.py'):
                self.lista_archivos.append(archivo)
        self.actualizar_listbox()

    def combinar_archivos(self):
        nombre_archivo_salida = simpledialog.askstring("Nombre del archivo", "Introduce el nombre del archivo de salida:")
        if nombre_archivo_salida:
            with open(nombre_archivo_salida, 'w') as archivo_salida:
                if self.texto_cabecera:
                    archivo_salida.write(self.texto_cabecera + '\n\n')  # Escribe el texto de cabecera
                for archivo in self.lista_archivos:
                    archivo_salida.write(f'=== {os.path.basename(archivo)} ===\n')
                    with open(archivo, 'r') as archivo_py:
                        archivo_salida.write(archivo_py.read())
                        archivo_salida.write('\n\n')  # Separador entre archivos
            messagebox.showinfo("Completado", f"Archivos combinados en {nombre_archivo_salida}")

# Crear la ventana principal
ventana = TkinterDnD.Tk()
ventana.title("Combinar Archivos Python")  # Agregar título a la ventana
ventana.tk.call("tk", "scaling", 1.5)  # Para pantallas con alta DPI
app = Aplicacion(ventana)

# Ejecutar el bucle principal de la interfaz gráfica
ventana.mainloop()
