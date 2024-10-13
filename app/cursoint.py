import tkinter as tk
from tkinter import messagebox
import sympy as sp
import random
from funciones import generar_polinomio  # Importamos la función de generar polinomios
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

x = sp.Symbol('x')

# Función para generar la integral y las opciones
def generar_ejercicio_integral():
    polinomio = generar_polinomio(3, 5)  # Generamos un polinomio de grado a lo más 3
    integral_correcta = sp.integrate(polinomio, x)  # Calculamos la integral correcta

    # Generamos dos opciones incorrectas (sumando o restando un valor arbitrario)
    incorrecta_1 = integral_correcta + generar_polinomio(2,5)
    incorrecta_2 = integral_correcta - generar_polinomio(2,5)

    opciones = [integral_correcta, incorrecta_1, incorrecta_2]
    random.shuffle(opciones)  # Mezclamos las opciones

    return polinomio, integral_correcta, opciones

# Función para renderizar ecuaciones LaTeX en una imagen con matplotlib
def mostrar_latex_en_tkinter(expr, ventana, pos_y=0):
    fig, ax = plt.subplots(figsize=(5, 1))
    ax.text(0.5, 0.5, f"${sp.latex(expr)}$", fontsize=20, ha='center', va='center')
    ax.axis('off')

    # Mostrar el gráfico en la ventana de Tkinter
    canvas = FigureCanvasTkAgg(fig, master=ventana)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=pos_y)

    return canvas

# Crear una ventana
ventana = tk.Tk()
ventana.title("Ejercicio de Cálculo Integral")

# Función para crear la ventana del ejercicio
def mostrar_ejercicio(ventana):
    polinomio, integral_correcta, opciones = generar_ejercicio_integral()


    # Mostrar el polinomio a integrar como LaTeX
    pregunta_label = tk.Label(ventana, text="¿Cuál es la integral de?", font=("Arial", 14))
    pregunta_label.pack(pady=10)

    mostrar_latex_en_tkinter(polinomio, ventana, pos_y=10)

    # Variable para almacenar la opción seleccionada
    seleccion = tk.StringVar()
    seleccion.set(None)  # Ninguna opción seleccionada inicialmente

    # Mostrar las opciones como LaTeX
    widgets_opciones = []
    for i, opcion in enumerate(opciones):
        label = tk.Label(ventana, text=f"Opción {i+1}:", font=("Arial", 12))
        label.pack(pady=5)
        widgets_opciones.append(mostrar_latex_en_tkinter(opcion, ventana, pos_y=5))

        radio_btn = tk.Radiobutton(ventana, variable=seleccion, value=str(opcion))
        radio_btn.pack()

    # Función para verificar la respuesta
    def verificar_respuesta():
        respuesta = seleccion.get()
        if respuesta == str(integral_correcta):
            messagebox.showinfo("Resultado", "¡Correcto! La integral es correcta.")
        else:
            messagebox.showerror("Resultado", "Incorrecto. La respuesta correcta era: " + str(sp.latex(integral_correcta)))

    # Botón para enviar la respuesta
    btn_verificar = tk.Button(ventana, text="Verificar respuesta", command=verificar_respuesta, font=("Arial", 12))
    btn_verificar.pack(pady=20)

    # Iniciar el loop de la ventana
    ventana.mainloop()

# Ejecutar el ejercicio
if __name__ == "__main__":
    mostrar_ejercicio(ventana)
