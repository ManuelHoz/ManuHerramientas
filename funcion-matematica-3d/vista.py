import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Importa Axes3D para gráficos 3D

class VistaGraficadora:
    def __init__(self, callback_generar):
        self.root = tk.Tk()
        self.root.title("Generador de Gráficos")

        self.funcion_var = tk.StringVar(value="x**2 + y**2 - 9")  # Valor por defecto: esfera con radio 3
        self.xmin_var = tk.DoubleVar(value=-10)
        self.xmax_var = tk.DoubleVar(value=10)
        self.ymin_var = tk.DoubleVar(value=-10)
        self.ymax_var = tk.DoubleVar(value=10)
        self.zmin_var = tk.DoubleVar(value=-10)
        self.zmax_var = tk.DoubleVar(value=10)

        # Configuración de los widgets
        ttk.Label(self.root, text="Función").grid(row=0, column=0)
        ttk.Entry(self.root, textvariable=self.funcion_var).grid(row=0, column=1, columnspan=3)

        ttk.Button(self.root, text="Generar Gráficos", command=callback_generar).grid(row=0, column=4)

        self._crear_entrada_rango("Xmin", self.xmin_var, 1, 0)
        self._crear_entrada_rango("Xmax", self.xmax_var, 1, 1)
        self._crear_entrada_rango("Ymin", self.ymin_var, 1, 2)
        self._crear_entrada_rango("Ymax", self.ymax_var, 1, 3)
        self._crear_entrada_rango("Zmin", self.zmin_var, 1, 4)
        self._crear_entrada_rango("Zmax", self.zmax_var, 1, 5)

        # Configuración de los gráficos
        self.fig = plt.figure(figsize=(12, 4))
        self.axs = []
        self.axs.append(self.fig.add_subplot(131))  # Gráfico 2D
        self.axs.append(self.fig.add_subplot(132, projection='3d'))  # Gráfico 3D
        self.axs.append(self.fig.add_subplot(133))  # Gráfico 2D

        self.fig.tight_layout(pad=3.0)

    def _crear_entrada_rango(self, texto, variable, row, col):
        ttk.Label(self.root, text=texto).grid(row=row, column=col)
        ttk.Entry(self.root, textvariable=variable).grid(row=row+1, column=col)

    def plot_graficos(self, X, Y, Z):
        self.axs[0].cla()
        self.axs[1].cla()
        self.axs[2].cla()

        self.axs[0].contourf(X, Y, Z, cmap='rainbow')  # Gráfico de contorno 2D
        self.axs[1].plot_surface(X, Y, Z, cmap='viridis')  # Gráfico de superficie 3D
        self.axs[2].plot_wireframe(X, Y, Z)  # Gráfico de armazón de alambre 3D

        self.fig.canvas.draw()

    def get_funcion(self):
        return self.funcion_var.get()

    def get_xmin(self):
        return self.xmin_var.get()

    def get_xmax(self):
        return self.xmax_var.get()

    def get_ymin(self):
        return self.ymin_var.get()

    def get_ymax(self):
        return self.ymax_var.get()

    def get_zmin(self):
        return self.zmin_var.get()

    def get_zmax(self):
        return self.zmax_var.get()

    def iniciar(self):
        self.root.mainloop()
