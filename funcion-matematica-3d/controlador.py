import tkinter as tk
from tkinter import ttk
from vista import VistaGraficadora
from modelo import ModeloGraficadora

class Controlador:
    def __init__(self):
        self.modelo = ModeloGraficadora()
        self.vista = VistaGraficadora(self.generar_graficos)

    def generar_graficos(self):
        funcion = self.vista.get_funcion()
        xmin = self.vista.get_xmin()
        xmax = self.vista.get_xmax()
        ymin = self.vista.get_ymin()
        ymax = self.vista.get_ymax()
        zmin = self.vista.get_zmin()
        zmax = self.vista.get_zmax()
        
        if funcion == "":
            funcion = "x**2 + y**2 - 9"  # Valor por defecto: esfera con radio 3
        
        X, Y, Z = self.modelo.calcular_puntos(funcion, xmin, xmax, ymin, ymax, zmin, zmax)
        self.vista.plot_graficos(X, Y, Z)

    def iniciar(self):
        self.vista.iniciar()

if __name__ == "__main__":
    controlador = Controlador()
    controlador.iniciar()
