import numpy as np
import sympy as sp

class ModeloGraficadora:
    def calcular_puntos(self, funcion_str, xmin, xmax, ymin, ymax, zmin, zmax):
        x, y, z = sp.symbols('x y z')
        expr = sp.sympify(funcion_str)

        X = np.linspace(xmin, xmax, 100)
        Y = np.linspace(ymin, ymax, 100)
        X, Y = np.meshgrid(X, Y)

        Z = sp.lambdify((x, y), expr, modules=['numpy'])(X, Y)
        return X, Y, Z
