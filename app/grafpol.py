import tkinter as tk
from tkinter import messagebox
import random
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from funciones import generar_polinomio

x = sp.Symbol('x')

# Función para generar un ejercicio con un polinomio aleatorio y opciones incorrectas
def generar_ejercicio_grafica():
    polinomio_correcto = generar_polinomio(2, 5)  # Polinomio de grado a lo más 3
    incorrecto_1 = generar_polinomio(2, 5)  # Otra opción incorrecta
    incorrecto_2 = generar_polinomio(2, 5)  # Otra opción incorrecta

    # Nos aseguramos de que las opciones incorrectas no sean iguales al polinomio correcto
    while incorrecto_1 == polinomio_correcto:
        incorrecto_1 = generar_polinomio(2, 5)
    while incorrecto_2 == polinomio_correcto or incorrecto_2 == incorrecto_1:
        incorrecto_2 = generar_polinomio(2, 5)

    opciones = [polinomio_correcto, incorrecto_1, incorrecto_2]
    random.shuffle(opciones)  # Mezclamos las opciones

    return polinomio_correcto, opciones

# Función para graficar el polinomio en la interfaz de Tkinter sin mostrar la fórmula en la gráfica
def graficar_polinomio(polinomio, ventana):
    f_lambdified = sp.lambdify(x, polinomio, 'numpy')  # Convertimos la expresión de sympy a función de numpy
    x_vals = np.linspace(-10, 10, 400)
    y_vals = f_lambdified(x_vals)

    # Graficar en matplotlib sin mostrar el polinomio
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.plot(x_vals, y_vals, label="Gráfica de polinomio")
    ax.axhline(0, color='black',linewidth=0.5)
    ax.axvline(0, color='black',linewidth=0.5)
    ax.grid(True)

    # Insertar la gráfica en Tkinter
    canvas = FigureCanvasTkAgg(fig, master=ventana)
    canvas.draw()
    canvas.get_tk_widget().pack()



# Función para crear la ventana del ejercicio
def mostrar_ejercicio_grafica(ventana):
    polinomio_correcto, opciones = generar_ejercicio_grafica()


    # Mostrar la gráfica del polinomio correcto sin revelar la fórmula
    label_instruccion = tk.Label(ventana, text="¿A cuál de los siguientes polinomios pertenece la gráfica?", font=("Arial", 14))
    label_instruccion.pack(pady=10)

    graficar_polinomio(polinomio_correcto, ventana)

    # Variable para almacenar la opción seleccionada
    seleccion = tk.StringVar()
    seleccion.set(None)  # Ninguna opción seleccionada inicialmente

    # Mostrar las opciones como LaTeX en un tamaño más pequeño
    for i, opcion in enumerate(opciones):
        radio_btn = tk.Radiobutton(ventana, text=f"Opción {i+1}: ${sp.latex(opcion)}$", variable=seleccion, value=str(opcion), font=("Arial", 10))  # Tamaño de fuente más pequeño
        radio_btn.pack(pady=5)

    # Función para verificar la respuesta
    def verificar_respuesta():
        respuesta = seleccion.get()
        if respuesta == str(polinomio_correcto):
            messagebox.showinfo("Resultado", "¡Correcto! El polinomio pertenece a la gráfica.")
        else:
            messagebox.showerror("Resultado", f"Incorrecto. El polinomio correcto era: ${sp.latex(polinomio_correcto)}$.")

    # Botón para enviar la respuesta
    btn_verificar = tk.Button(ventana, text="Verificar respuesta", command=verificar_respuesta, font=("Arial", 12))
    btn_verificar.pack(pady=20)

    # Iniciar el loop de la ventana
    ventana.mainloop()

# Ejecutar el ejercicio
if __name__ == "__main__":
    # Crear una ventana de Tkinter
    ventana = tk.Tk()
    ventana.title("Ejercicio de Gráficas de Polinomios")
    mostrar_ejercicio_grafica(ventana)
