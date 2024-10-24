 import tkinter as tk
 from tkinter import messagebox
import random
import sympy as sp
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from funciones import generar_polinomio  # Importar la función desde funciones.py

# Definir la variable simbólica 'x'
x = sp.Symbol('x')
i
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

    # Botón para pasar al siguiente ejercicio
    btn_siguiente = tk.Button(ventana, text="Siguiente", command=lambda: [ventana.destroy()], font=("Arial", 12))
    btn_siguiente.pack(pady=20)


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
    ax.text(0.5, 0.5, f"${sp.latex(expresion)}$", fontsize=14, ha='center', va='center')
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
# Crear la ventana principal
#ventana = tk.Toplevel()
#ventana.title("Ejercicio de Derivadas")

# Función para crear la interfaz del ejercicio
def crear_ejercicio(ventana):
    # Generar un polinomio aleatorio usando la función del archivo funciones.py
    polinomio = generar_polinomio(3, 10)  # Polinomio de grado máximo 3 y coeficientes entre -10 y 10
    opciones, correcta = generar_opciones(polinomio)


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

    btn_salir = tk.Button(ventana, text="Siguiente", command=ventana.destroy, font=("Arial", 12))
    btn_salir.pack(pady=20)


def generar_ejercicio_derivada_sqrt():
    a = random.randint(1, 5)
    b = random.randint(1, 5)
    funcion = sp.sqrt(a * x + b )
    derivada_correcta = sp.diff(funcion, x)

    # Opciones incorrectas
    incorrecto_1 = x/sp.sqrt(a * x + (b + 1)  )
    incorrecto_2 = a/sp.sqrt(a * x + b  -  1)

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


# Función para crear la ventana del ejercicio de derivada
def mostrar_ejercicio_derivada_sqrt(ventana):
    funcion, derivada_correcta, opciones = generar_ejercicio_derivada_sqrt()


    # Instrucciones
    label_instruccion = tk.Label(ventana, text="¿Cuál es la derivada de la siguiente función?", font=("Arial", 14))
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
        if respuesta == str(derivada_correcta):
            messagebox.showinfo("Resultado", "¡Correcto! Esa es la derivada.")
        else:
            messagebox.showerror("Resultado", f"Incorrecto. La respuesta correcta era: ${sp.latex(derivada_correcta)}$.")

    # Botón para enviar la respuesta
    btn_verificar = tk.Button(ventana, text="Verificar respuesta", command=verificar_respuesta, font=("Arial", 12))
    btn_verificar.pack(pady=20)

    btn_salir = tk.Button(ventana, text="Siguiente", command=ventana.destroy, font=("Arial", 12))
    btn_salir.pack(pady=20)


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

    btn_salir = tk.Button(ventana, text="Siguiente", command=ventana.destroy, font=("Arial", 12))
    btn_salir.pack(pady=20)




