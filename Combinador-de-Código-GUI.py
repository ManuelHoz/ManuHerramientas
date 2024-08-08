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
        self.ventana.minsize(400, 300)
        
        self.lista_archivos = []
        self.widgets_archivos = {}
        self.mostrando_ruta_completa = {}

        # Configuración de estilo
        estilo = ttk.Style()
        estilo.configure('TButton', font=("Helvetica Neue", 12))

        # Frame principal con fondo gris claro
        self.frame_principal = tk.Frame(ventana, bg="lightgray")
        self.frame_principal.pack(fill=tk.BOTH, expand=True, pady=10)

        # Botones redondeados con estilo aplicado
        self.boton_seleccionar_directorio = ttk.Button(
            ventana, text="Seleccionar Directorio", 
            command=self.seleccionar_directorio, 
            bootstyle="success-round-outline", 
            padding=(10,5),
            style='TButton'
        )
        self.boton_seleccionar_directorio.pack(fill=tk.X, padx=10, pady=5)

        self.boton_añadir_archivo = ttk.Button(
            ventana, text="Añadir Archivo", 
            command=self.añadir_archivo, 
            bootstyle="success-round-outline", 
            padding=(10,5),
            style='TButton'
        )
        self.boton_añadir_archivo.pack(fill=tk.X, padx=10, pady=5)

        self.boton_combinar = ttk.Button(
            ventana, text="Combinar Archivos", 
            command=self.combinar_archivos, 
            bootstyle="success-round-outline", 
            padding=(10,5),
            style='TButton'
        )
        self.boton_combinar.pack(fill=tk.X, padx=10, pady=20)

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

    def actualizar_listbox(self):
        for archivo in self.lista_archivos:
            if archivo not in self.widgets_archivos:
                self.mostrando_ruta_completa[archivo] = False
                frame_archivo = tk.Frame(self.frame_principal, bg="lightgray")
                frame_archivo.pack(fill=tk.X, pady=2, padx=10)

                label_archivo = tk.Label(frame_archivo, text=os.path.basename(archivo), anchor="w", font=("Helvetica Neue", 12), bg="lightgray")
                label_archivo.pack(side=tk.LEFT, expand=True, fill=tk.X)

                boton_eliminar = ttk.Button(
                    frame_archivo, text="Eliminar", 
                    command=lambda archivo=archivo: self.eliminar_archivo(archivo), 
                    bootstyle="danger-round-outline", 
                    padding=(5,5),
                    style='TButton'
                )
                boton_eliminar.pack(side=tk.RIGHT)

                boton_mostrar_ruta = ttk.Button(
                    frame_archivo, text="Mostrar Ruta Completa", 
                    command=lambda archivo=archivo: self.mostrar_ruta_completa(archivo), 
                    bootstyle="info-round-outline", 
                    padding=(5,5),
                    style='TButton'
                )
                boton_mostrar_ruta.pack(side=tk.RIGHT)

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
