import sympy as sp
import random
import numpy as np
import matplotlib.pyplot as plt

# Definir la variable simbólica 'x' globalmente
x = sp.Symbol('x')

# Función para generar un polinomio de grado n con coeficientes aleatorios entre -m y m
def generar_polinomio(n, m):
    coeficientes = [random.randint(-m, m) for _ in range(n+1)]  # Coeficientes aleatorios
    polinomio = sum(coeficientes[i] * x**i for i in range(n+1))  # Construir el polinomio
    return sp.simplify(polinomio)  # Simplificamos el polinomio

# Función para graficar cualquier expresión simbólica de sympy
def graficar_funcion(funcion, x_range=(-10, 10), num_puntos=400):
    f_lambdified = sp.lambdify(x, funcion, 'numpy')  # Convertir la expresión sympy a función numpy
    x_vals = np.linspace(x_range[0], x_range[1], num_puntos)  # Rango de x para la gráfica
    y_vals = f_lambdified(x_vals)  # Evaluar la función en los valores de x

    # Graficar
    plt.plot(x_vals, y_vals, label=str(funcion))
    plt.title('Gráfica de la función')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(True)
    plt.legend()
    plt.show()


