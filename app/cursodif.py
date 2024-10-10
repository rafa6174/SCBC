import tkinter as tk
import random
import sympy as sp
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from funciones import generar_polinomio  # Importar la función desde funciones.py

# Definir la variable simbólica 'x'
x = sp.Symbol('x')

# Función para generar opciones de respuesta (una correcta y dos incorrectas)
def generar_opciones(polinomio):
    derivada_correcta = sp.diff(polinomio, x)  # Derivada correcta
    opciones = [derivada_correcta]  # Lista de opciones con la correcta

    # Generar dos respuestas incorrectas
    for _ in range(2):
        incorrecta = derivada_correcta + sp.Rational(random.randint(-5, 5), random.randint(1, 5))
        while incorrecta in opciones:  # Asegurar que la opción incorrecta sea única
            incorrecta = derivada_correcta + sp.Rational(random.randint(-5, 5), random.randint(1, 5))
        opciones.append(incorrecta)

    random.shuffle(opciones)  # Mezclar las opciones
    return opciones, derivada_correcta

# Función para mostrar el polinomio y opciones en formato LaTeX usando matplotlib
def mostrar_latex_lienzo(ventana, expresion, pos_y):
    # Crear una figura para matplotlib
    fig, ax = plt.subplots(figsize=(5, 1))  # Tamaño pequeño
    ax.text(0.5, 0.5, f"${sp.latex(expresion)}$", fontsize=18, ha='center', va='center')
    ax.axis('off')  # Ocultar ejes

    # Integrar la figura en la ventana Tkinter
    canvas = FigureCanvasTkAgg(fig, master=ventana)
    canvas.get_tk_widget().pack(pady=pos_y)
    canvas.draw()

# Función para verificar la respuesta seleccionada
def verificar_respuesta(seleccion, correcta, ventana):
    if seleccion == str(correcta):
        resultado = "¡Correcto!"
    else:
        resultado = f"Incorrecto. La respuesta correcta era: {correcta}"

    # Mostrar el resultado
    resultado_label = tk.Label(ventana, text=resultado, font=("Arial", 14))
    resultado_label.pack(pady=10)

# Función para crear la interfaz del ejercicio
def crear_ejercicio():
    # Generar un polinomio aleatorio usando la función del archivo funciones.py
    polinomio = generar_polinomio(3, 10)  # Polinomio de grado máximo 3 y coeficientes entre -10 y 10
    opciones, correcta = generar_opciones(polinomio)

    # Crear la ventana principal
    ventana = tk.Toplevel()
    ventana.title("Ejercicio de Derivadas")

    # Mostrar el polinomio en formato LaTeX
    texx = tk.Label(ventana, text="Seleccione la derivada de:",font=("Arial",14))
    texx.pack(pady=10)
    mostrar_latex_lienzo(ventana, polinomio, pos_y=10)

    # Variable para almacenar la opción seleccionada
    seleccion = tk.StringVar()

    # Mostrar las opciones de respuesta en formato LaTeX
    for opcion in opciones:
        mostrar_latex_lienzo(ventana, opcion, pos_y=10)
        tk.Radiobutton(ventana, text="Seleccionar", variable=seleccion, value=str(opcion), font=("Arial", 12)).pack(anchor=tk.W)

    # Botón para verificar la respuesta
    verificar_btn = tk.Button(ventana, text="Verificar respuesta", command=lambda: verificar_respuesta(seleccion.get(), correcta, ventana))
    verificar_btn.pack(pady=10)

# Probar la función
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sistema Tutorial Inteligente - Ejercicio de Derivadas")
    tk.Button(root, text="Generar Ejercicio", command=crear_ejercicio).pack(pady=20)
    root.mainloop()
