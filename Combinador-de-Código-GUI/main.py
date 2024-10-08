from modelo import Modelo
from vista import Vista
from controlador import Controlador
import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES

if __name__ == "__main__":
    ventana = TkinterDnD.Tk()
    ventana.title("Combinar Archivos Python")
    ventana.tk.call("tk", "scaling", 1.5)

    modelo = Modelo()
    vista = Vista(ventana)
    controlador = Controlador(modelo, vista)

    ventana.mainloop()
