import tkinter as tk
from tkinter import ttk
from experta import *
import subprocess
import os
import platform
from tkinter import messagebox

# Importar los módulos personalizados
import cursodif
import grafpol
import derac
import derexp

import cursoint
import intrac
import intexp

def practica(opcion, ventana_ejercicio):
        match opcion:
                case 1:
                        for widget in ventana_ejercicio.winfo_children():
                                widget.destroy()
                        grafpol.mostrar_ejercicio_grafica(ventana_ejercicio)
                case 2:
                        for widget in ventana_ejercicio.winfo_children():
                                widget.destroy()
                        cursodif.crear_ejercicio(ventana_ejercicio)
                case 3:
                        for widget in ventana_ejercicio.winfo_children():
                                widget.destroy()
                        derac.mostrar_ejercicio_derivada_sqrt(ventana_ejercicio)
                case 4:
                        for widget in ventana_ejercicio.winfo_children():
                                widget.destroy()
                        derexp.mostrar_ejercicio_derivada_exp(ventana_ejercicio)
                case 5:
                        for widget in ventana_ejercicio.winfo_children():
                                widget.destroy()
                        cursoint.mostrar_ejercicio(ventana_ejercicio)
                case 6:
                        for widget in ventana_ejercicio.winfo_children():
                                widget.destroy()
                        intrac.mostrar_ejercicio_integral_sqrt(ventana_ejercicio)
                case 7:
                        for widget in ventana_ejercicio.winfo_children():
                                widget.destroy()
                        intexp.mostrar_ejercicio_integral_exp(ventana_ejercicio)
                case _:
                        print("Opción no válida")

# Función para cargar los ejercicios de gráficos de polinomios
def graficas_polinomios(eje):
    print(f"Ejecutando graficas_polinomios con eje={eje}")  # Verificar si se está ejecutando
    ventana_ejercicio = tk.Toplevel()  # Crear una nueva ventana
    practica(eje, ventana_ejercicio)
    # Agregar un botón "Siguiente" si hay más ejercicios
    if eje < 6:
        tk.Button(ventana_ejercicio, text="Siguiente", command=lambda: siguiente_grafica(eje)).pack()
    else:
        tk.Button(ventana_ejercicio, text="Finalizar", command=lambda: print("Formulario finalizado")).pack()

def siguiente_grafica(eje):
    eje += 1  # Incrementar el valor de eje
    graficas_polinomios(eje)

# Crear ventana principal
ventana_principal = tk.Tk()

# Botón para iniciar los ejercicios de gráficos de polinomios
boton_practica = tk.Button(ventana_principal, text="Practicar Gráficas de Polinomios",
                           command=lambda: graficas_polinomios(1))
boton_practica.pack(pady=20)

ventana_principal.mainloop()
