import os
from tkinter import filedialog, messagebox, simpledialog
from gestor_archivos import GestorArchivos
from gestor_dialogos import GestorDialogos

class Controlador:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.gestor_archivos = GestorArchivos()
        self.gestor_dialogos = GestorDialogos()

        self.vista.boton_seleccionar_directorio.config(command=self.seleccionar_directorio)
        self.vista.boton_anadir_archivo.config(command=self.anadir_archivo)
        self.vista.boton_agregar_texto.config(command=self.agregar_texto)
        self.vista.boton_combinar.config(command=self.combinar_archivos)
        self.vista.boton_copiar.config(command=self.copiar_portapapeles)
        self.vista.frame_principal.dnd_bind('<<Drop>>', self.archivos_arrastrados)
        
        self.widgets_archivos = {}
        self.mostrando_ruta_completa = {}

    def seleccionar_directorio(self):
        directorio = self.gestor_dialogos.seleccionar_directorio()
        if directorio:
            try:
                tipos_archivo = self.vista.get_tipos_archivo()
                archivos = self.gestor_archivos.obtener_archivos_directorio(directorio, tipos_archivo)
                for archivo in archivos:
                    if os.path.exists(archivo):
                        self.modelo.agregar_archivo(archivo)
                self.actualizar_listbox()
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo acceder al directorio o a los archivos: {str(e)}")

    def anadir_archivo(self):
        archivos = self.gestor_dialogos.seleccionar_archivos(self.vista.get_tipos_archivo())
        if archivos:
            for archivo in archivos:
                self.modelo.agregar_archivo(archivo)
                self.vista.crear_widget_archivo(archivo, eliminar_func=lambda: self.eliminar_archivo(archivo), mostrar_ruta_func=lambda: self.mostrar_ruta(archivo))

    def agregar_texto(self):
        texto_cabecera = self.gestor_dialogos.obtener_texto_cabecera()
        self.modelo.agregar_texto_cabecera(texto_cabecera)
        self.mostrar_texto_cabecera()

    def mostrar_texto_cabecera(self):
        palabras = self.modelo.obtener_texto_cabecera().split()
        texto_mostrado = ' '.join(palabras[:100])
        if len(palabras) > 100:
            texto_mostrado += "..."
        self.vista.mostrar_texto_cabecera(texto_mostrado)

    def eliminar_archivo(self, archivo):
        self.modelo.eliminar_archivo(archivo)
        self.vista.limpiar_listbox()
        self.actualizar_listbox()

    def mostrar_ruta_completa(self, archivo):
        if archivo in self.widgets_archivos:
            frame_archivo = self.widgets_archivos[archivo]
            label_archivo = frame_archivo.nametowidget(frame_archivo.winfo_children()[0])
            if self.mostrando_ruta_completa[archivo]:
                label_archivo.config(text=os.path.basename(archivo))
                self.mostrando_ruta_completa[archivo] = False
            else:
                label_archivo.config(text=archivo)
                self.mostrando_ruta_completa[archivo] = True
                label_archivo.config(wraplength=400)

    def actualizar_listbox(self):
        self.vista.limpiar_listbox()
        for archivo in self.modelo.obtener_archivos():
            frame_archivo = self.vista.crear_widget_archivo(
                archivo, 
                lambda archivo=archivo: self.eliminar_archivo(archivo),
                lambda archivo=archivo: self.mostrar_ruta_completa(archivo)
            )
            self.widgets_archivos[archivo] = frame_archivo
            self.mostrando_ruta_completa[archivo] = False

    def archivos_arrastrados(self, event):
        archivos = self.vista.ventana.tk.splitlist(event.data)
        for archivo in archivos:
            self.modelo.agregar_archivo(archivo)
        self.actualizar_listbox()

    def combinar_archivos(self):
        nombre_archivo_salida = self.gestor_dialogos.obtener_nombre_archivo_salida()
        if nombre_archivo_salida:
            self.modelo.combinar_archivos(nombre_archivo_salida)
            messagebox.showinfo("Completado", f"Archivos combinados en {nombre_archivo_salida}")

    def copiar_portapapeles(self):
        contenido_combinado = self.modelo.copiar_portapapeles()
        self.vista.ventana.clipboard_clear()
        self.vista.ventana.clipboard_append(contenido_combinado)
        messagebox.showinfo("Copiado", "El contenido combinado ha sido copiado al portapapeles.")
