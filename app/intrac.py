import tkinter as tk
from tkinter import messagebox
import sympy as sp
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

x = sp.Symbol('x')

# Función para generar un ejercicio de integral con una función del tipo sqrt(ax^2 + bx + c)
def generar_ejercicio_integral_sqrt():
    a = random.randint(1, 5)
    b = random.randint(1, 5)
    funcion = sp.sqrt(a * x + b )
    integral_correcta = sp.integrate(funcion, x)

    # Opciones incorrectas
    incorrecto_1 = sp.sqrt(a * x + (b + 1) )
    incorrecto_2 = sp.sqrt((a+1) * x + b+ 2)

    opciones = [integral_correcta, incorrecto_1, incorrecto_2]
    random.shuffle(opciones)  # Mezclamos las opciones

    return funcion, integral_correcta, opciones

# Función para renderizar LaTeX en una ventana de Tkinter usando matplotlib
def renderizar_latex_en_tkinter(expresion, ventana, fontsize=12):
    fig, ax = plt.subplots(figsize=(3, 0.5))  # Ajustar el tamaño del área de la figura
    ax.text(0.5, 0.5, f"${sp.latex(expresion)}$", fontsize=fontsize, ha='center', va='center')
    ax.axis('off')

    canvas = FigureCanvasTkAgg(fig, master=ventana)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Crear la ventana de Tkinter
ventana = tk.Tk()
ventana.title("Ejercicio de Integral de sqrt(ax + b)")

# Función para crear la ventana del ejercicio de integral
def mostrar_ejercicio_integral_sqrt(ventana):
    funcion, integral_correcta, opciones = generar_ejercicio_integral_sqrt()


    # Instrucciones
    label_instruccion = tk.Label(ventana, text="¿Cuál es la integral de la siguiente función?", font=("Arial", 14))
    label_instruccion.pack(pady=10)

    # Renderizar la función en LaTeX
    renderizar_latex_en_tkinter(funcion, ventana, fontsize=20)

    # Variable para almacenar la opción seleccionada
    seleccion = tk.StringVar()
    seleccion.set(None)  # Ninguna opción seleccionada inicialmente

    # Mostrar las opciones en LaTeX
    for i, opcion in enumerate(opciones):
        renderizar_latex_en_tkinter(opcion, ventana, fontsize=12)
        radio_btn = tk.Radiobutton(ventana, text=f"Opción {i+1}", variable=seleccion, value=str(opcion), font=("Arial", 10))
        radio_btn.pack(pady=5)


    # Función para verificar la respuesta
    def verificar_respuesta():
        respuesta = seleccion.get()
        if respuesta == str(integral_correcta):
            messagebox.showinfo("Resultado", "¡Correcto! Esa es la integral.")
        else:
            messagebox.showerror("Resultado", f"Incorrecto. La respuesta correcta era: ${sp.latex(integral_correcta)}$.")

    # Botón para enviar la respuesta
    btn_verificar = tk.Button(ventana, text="Verificar respuesta", command=verificar_respuesta, font=("Arial", 12))
    btn_verificar.pack(pady=20)

    # Iniciar el loop de la ventana
    ventana.mainloop()

# Ejecutar el ejercicio
if __name__ == "__main__":
    mostrar_ejercicio_integral_sqrt(ventana)
