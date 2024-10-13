import tkinter as tk
from tkinter import messagebox
import sympy as sp
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

x = sp.Symbol('x')

# Función para generar un ejercicio de derivada con una función exponencial
def generar_ejercicio_derivada_exp():
    a = random.randint(1, 5)  # Coeficiente de la exponencial
    b = random.randint(1, 5)  # Exponente
    funcion = a * sp.exp(b * x)  # Función exponencial
    derivada_correcta = sp.diff(funcion, x)  # Derivada correcta

    # Opciones incorrectas
    incorrecto_1 = a * sp.exp((b + 1) * x)
    incorrecto_2 = a * sp.exp((b - 1) * x)

    opciones = [derivada_correcta, incorrecto_1, incorrecto_2]
    random.shuffle(opciones)  # Mezclamos las opciones

    return funcion, derivada_correcta, opciones

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
ventana.title("Ejercicio de Derivada de Función Exponencial")

# Función para crear la ventana del ejercicio de derivada
def mostrar_ejercicio_derivada_exp(ventana):
    funcion, derivada_correcta, opciones = generar_ejercicio_derivada_exp()



    # Instrucciones
    label_instruccion = tk.Label(ventana, text="¿Cuál es la derivada de la siguiente función?", font=("Arial", 14))
    label_instruccion.pack(pady=10)

    # Renderizar la función en LaTeX (en tamaño más grande)
    renderizar_latex_en_tkinter(funcion, ventana, fontsize=20)

    # Variable para almacenar la opción seleccionada
    seleccion = tk.StringVar()
    seleccion.set(None)  # Ninguna opción seleccionada inicialmente

    # Mostrar las opciones en LaTeX con fuente pequeña
    for i, opcion in enumerate(opciones):
        renderizar_latex_en_tkinter(opcion, ventana, fontsize=20)
        radio_btn = tk.Radiobutton(ventana, text=f"Opción {i+1}", variable=seleccion, value=str(opcion), font=("Arial", 10))
        radio_btn.pack(pady=5)


    # Función para verificar la respuesta
    def verificar_respuesta():
        respuesta = seleccion.get()
        if respuesta == str(derivada_correcta):
            messagebox.showinfo("Resultado", "¡Correcto! Esa es la derivada.")
        else:
            messagebox.showerror("Resultado", f"Incorrecto. La respuesta correcta era: ${sp.latex(derivada_correcta)}$.")

    # Botón para enviar la respuesta
    btn_verificar = tk.Button(ventana, text="Verificar respuesta", command=verificar_respuesta, font=("Arial", 12))
    btn_verificar.pack(pady=20)

    # Iniciar el loop de la ventana
    ventana.mainloop()

# Ejecutar el ejercicio
if __name__ == "__main__":
    mostrar_ejercicio_derivada_exp(ventana)
