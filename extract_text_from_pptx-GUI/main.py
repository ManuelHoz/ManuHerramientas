from tkinter import Tk
from modelo import Modelo
from vista import Vista
from controlador import Controlador

if __name__ == "__main__":
    ventana = Tk()
    ventana.title("Extractor de Texto de PDFs")
    ventana.tk.call("tk", "scaling", 1.5)

    modelo = Modelo()
    vista = Vista(ventana)
    controlador = Controlador(modelo, vista)

    ventana.mainloop()
