import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class VistaPDF:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Agregar PDFs")
        self.ventana.geometry("300x200")

        self.frame_principal = ttk.Frame(self.ventana, padding=20)
        self.frame_principal.pack(fill=tk.BOTH, expand=True)

        self.boton_procesar = ttk.Button(self.frame_principal, text="Seleccionar y Procesar PDFs", bootstyle="primary")
        self.boton_procesar.pack(pady=20)
