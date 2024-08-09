from tkinterdnd2 import TkinterDnD
from modelo import Modelo
from vista import Vista
from controlador import Controlador

if __name__ == "__main__":
    ventana = TkinterDnD.Tk()
    ventana.title("Combinar Archivos Python")
    ventana.tk.call("tk", "scaling", 1.5)

    modelo = Modelo()
    vista = Vista(ventana)
    controlador = Controlador(modelo, vista)

    ventana.mainloop()
