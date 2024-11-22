import tkinter as tk
from PIL import Image, ImageTk  # Necesario para manejar imágenes en tkinter
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

from chatbot import mostrar_chatbot

# Función para abrir archivos PDF
def abrir_pdf(ruta_pdf):
        if platform.system() == "Windows":
                os.startfile(ruta_pdf)  # Abre el archivo en Windows
        elif platform.system() == "Darwin":  # macOS
                subprocess.Popen(["open", ruta_pdf])
        else:  # Linux
                subprocess.Popen(["xdg-open", ruta_pdf])

# Función que destruye los widgets actuales y carga el nuevo ejercicio
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
        print(f"Ejecutando graficas_polinomios con eje={eje}")
        ventana_ejercicio = tk.Toplevel()
        practica(eje, ventana_ejercicio)

        # Frame para botones
        boton_frame = tk.Frame(ventana_ejercicio)
        boton_frame.pack(pady=20)

        # Botón siguiente o finalizar según el número de ejercicios
        if eje < 7:
                tk.Button(boton_frame, text="Siguiente", font=("Arial", 12), command=lambda: siguiente_grafica(eje, ventana_ejercicio)).pack(side=tk.RIGHT, padx=10)
        else:
                tk.Button(boton_frame, text="Finalizar", font=("Arial", 12), command=finalizar_formulario).pack(side=tk.RIGHT, padx=10)

# Función que maneja la navegación al siguiente ejercicio
def siguiente_grafica(eje, ventana_ejercicio):
        eje = eje + 1
        ventana_ejercicio.destroy()  # Cierra la ventana actual antes de cargar el siguiente ejercicio
        graficas_polinomios(eje)



# Función para crear el formulario con las preguntas
def abrir_nuevo_formulario():
        nueva_ventana = tk.Toplevel()
        nueva_ventana.title("Examen diagnóstico")
        nueva_ventana.geometry("800x650")

        # Cargar la imagen de fondo
        fondo_img = Image.open("ptofondo.png")
        fondo_img = fondo_img.resize((800, 650), Image.LANCZOS)  # Ajusta el tamaño de la imagen
        fondo_photo = ImageTk.PhotoImage(fondo_img)

        # Crear un Label con la imagen de fondo
        fondo_label = tk.Label(nueva_ventana, image=fondo_photo)
        fondo_label.image = fondo_photo  # Necesario para evitar que la imagen sea recolectada por el GC
        fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Lista de preguntas y opciones por página
        preguntas = [
                [
                        ("¿Qué teorema te garantiza que si una función continua en un cerrado cambia de signo, entonces tiene un cero?",
                                ["Teorema del valor medio", "Teorema del valor intermedio", "Teorema fundamental"]),
                        ("¿Cuál es la derivada de una constante?",
                                ["Cero", "Uno", "Infinito"]),
                        ("¿Qué significa que una función sea diferenciable en un punto?",
                                ["Que es continua", "Que tiene al menos una derivada en ese punto", "Que tiene una asíntota"]),
                        ("Si una función es derivable, ¿es continua?",
                                ["Sí", "No"]),
                        ("¿Qué relación existe entre la derivada y la velocidad instantánea?",
                                ["La derivada es la velocidad instantánea", "La derivada es la aceleración", "No hay relación"])
                ],
                [
                        ("¿Para qué sirve es la regla de la cadena?",
                                ["Derivar productos", "Derivar Convoluciones", "Derivar composiciones"]),
                        ("Si una función tiene derivada segunda positiva, ¿qué significa?",
                                ["Concavidad hacia arriba", "Concavidad hacia abajo", "Es constante"]),
                        ("¿Qué significa que una función sea creciente?",
                                ["Que su derivada es positiva", "Que su derivada es negativa", "Que su derivada es cero"]),
                        ("¿Qué teorema describe la relación entre la derivada y la pendiente de una tangente?",
                                ["Teorema del valor intermedio", "Teorema del valor medio", "Teorema fundamental"]),
                        ("¿Qué es un punto crítico?",
                                ["Donde la derivada es cero", "Donde la función no es continua", "Donde la función es derivable"])
                ],
                [
                        ("¿Cómo se representa gráficamente la integral definida?",
                                ["El área bajo la curva", "La pendiente de la tangente", "El cambio de signo"]),
                        ("¿Qué es una integral indefinida?",
                                ["Una función", "Un número", "Una constante"]),
                        ("¿Qué es una integral impropia?",
                                ["Integrar algo no acotado o sobre algo  no compacto", "Una integral mal calculada", "Una integral que no tiene solución"]),
                        ("¿Cuál es el método de integración por partes?",
                                ["Dividir la integral en dos partes", "Usar una derivada dentro de la integral", "Usar un producto de funciones"]),
                        ("¿Cómo se calcula la integral definida?",
                                ["Usando el teorema fundamental del cálculo", "Derivando la función", "Multiplicando por una constante"])
                ]
        ]

        # Lista de respuestas correctas (mismo orden que las preguntas)
        respuestas_correctas = [
                ["Teorema del valor intermedio", "Cero", "Que tiene al menos una derivada en ese punto", "Sí", "La derivada es la velocidad instantánea"],
                ["Derivar composiciones", "Concavidad hacia arriba", "Que su derivada es positiva", "Teorema del valor medio", "Donde la derivada es cero"],
                ["El área bajo la curva", "Una función", "Integrar algo no acotado o sobre algo  no compacto", "Usar un producto de funciones", "Usando el teorema fundamental del cálculo"]
        ]

        # Crear una lista para almacenar las respuestas de cada página
        respuestas = {}

        # Crear variable de control de página actual
        pagina_actual = 0

        # Función para mostrar preguntas de la página actual
        def mostrar_pagina(pagina):
                # Limpiar el contenido actual de la ventana
                for widget in nueva_ventana.winfo_children():
                        widget.destroy()
                nueva_ventana.geometry("800x650")

                # Cargar la imagen de fondo
                fondo_img = Image.open("ptofondo.png")
                fondo_img = fondo_img.resize((800, 650), Image.LANCZOS)  # Ajusta el tamaño de la imagen
                fondo_photo = ImageTk.PhotoImage(fondo_img)

                # Crear un Label con la imagen de fondo
                fondo_label = tk.Label(nueva_ventana, image=fondo_photo)
                fondo_label.image = fondo_photo  # Necesario para evitar que la imagen sea recolectada por el GC
                fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

                # Mostrar las preguntas de la página correspondiente
                for i, (pregunta, opciones) in enumerate(preguntas[pagina]):
                        tk.Label(nueva_ventana, text=pregunta, font=("Arial", 12)).pack(pady=5)

                        # Crear una variable para la respuesta seleccionada
                        seleccion = tk.StringVar(value=respuestas.get((pagina, i)))
                        # Mostrar las opciones de respuesta
                        for opcion in opciones:
                                tk.Radiobutton(nueva_ventana, text=opcion, variable=seleccion, value=opcion, font=("Arial", 12)).pack(anchor=tk.W)

                        seleccion.trace("w", lambda *args, p=pagina, q=i, v=seleccion: respuestas.update({(p, q): v.get()}))

                # Botones de navegación
                btn_frame = tk.Frame(nueva_ventana)
                btn_frame.pack(pady=10)

                if pagina > 0:
                        tk.Button(btn_frame, text="Anterior", font=("Arial", 12), command=lambda: cambiar_pagina(pagina - 1)).pack(side=tk.LEFT, padx=10)

                if pagina < len(preguntas) - 1:
                        tk.Button(btn_frame, text="Siguiente", font=("Arial", 12), command=lambda: cambiar_pagina(pagina + 1)).pack(side=tk.RIGHT, padx=10)
                else:
                        tk.Button(btn_frame, text="Finalizar", font=("Arial", 12), command=finalizar_formulario).pack(side=tk.RIGHT, padx=10)

                # Mostrar el número de página en la esquina inferior derecha
                tk.Label(nueva_ventana, text=f"Página {pagina + 1}", font=("Arial", 10)).place(relx=0.95, rely=0.95, anchor=tk.SE)

        # Función para cambiar la página
        def cambiar_pagina(nueva_pagina):
                mostrar_pagina(nueva_pagina)
                                              

        # Función para finalizar el formulario, calcular el puntaje y mostrar las respuestas
        def finalizar_formulario():
                # Limpiar la ventana
                for widget in nueva_ventana.winfo_children():
                        widget.destroy()
                nueva_ventana.geometry("800x650")

                # Cargar la imagen de fondo
                fondo_img = Image.open("ptofondoo.png")
                fondo_img = fondo_img.resize((800, 650), Image.LANCZOS)  # Ajusta el tamaño de la imagen
                fondo_photo = ImageTk.PhotoImage(fondo_img)

                # Crear un Label con la imagen de fondo
                fondo_label = tk.Label(nueva_ventana, image=fondo_photo)
                fondo_label.image = fondo_photo  # Necesario para evitar que la imagen sea recolectada por el GC
                fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

                # Calcular el puntaje
                puntaje_dif = 0
                puntaje_int = 0
                preguntas_dif = 0
                preguntas_int = 0

                for (pagina, pregunta), seleccion in respuestas.items():
                        respuesta_correcta = respuestas_correctas[pagina][pregunta]
                        respuesta_usuario = seleccion

                        # Dividir las preguntas entre diferencial (páginas 0 y 1) e integral (página 2 en adelante)
                        if pagina > 1:  # Páginas de integral (página 2 en adelante)
                                if respuesta_usuario == respuesta_correcta:
                                        puntaje_int += 1
                                preguntas_int += 1
                        else:  # Páginas de diferencial (páginas 0 y 1)
                                if respuesta_usuario == respuesta_correcta:
                                        puntaje_dif += 1
                                preguntas_dif += 1

                total_preguntas = preguntas_dif + preguntas_int
                puntaje_total = puntaje_int + puntaje_dif  # Sumamos puntaje_dif y puntaje_int para obtener el total

                # A partir de aquí se mostrarán los resultados
                tk.Label(nueva_ventana, text="Resultados del examen diagnóstico", font=("Impact", 22)).pack(pady=10)
                tk.Label(nueva_ventana, text=f"Puntaje diferencial: {puntaje_dif}/10", font=("Verdana", 14)).pack(pady=10)
                tk.Label(nueva_ventana, text=f"Puntaje integral: {puntaje_int}/5", font=("Verdana", 14)).pack(pady=10)
                tk.Label(nueva_ventana, text=f"Puntaje total: {puntaje_total}/15", font=("Verdana", 14)).pack(pady=10)

                bot_button = tk.Button(nueva_ventana, text="Usar chatbot", font=("Arial", 12), command=mostrar_chatbot)
                bot_button.pack(pady=10)
                

                # Sistema experto que determina el curso que se debe tomar
                p_dif = puntaje_dif / 10
                p_int = puntaje_int / 5
                p_total = puntaje_total / 15


                # Definir los hechos del sistema
                class Puntajes(Fact):
                        """Información sobre los puntajes obtenidos en un examen diagnóstico."""
                        pass

                # Definir el motor de inferencia
                class DiagnosticoCursillo(KnowledgeEngine):

                        
                        # Constructor que recibe la ventana principal
                        def __init__(self, root):
                                super().__init__()
                                self.root = root  # Guardar la referencia a la ventana principal

                        # Función para mostrar una nueva "página" en el mismo proyecto
                        def mostrar_pagina(self, mensaje, pagina_func):
                                if messagebox.askokcancel("Recomendación", mensaje):
                                    pagina_func()

                        # Función para la página del curso de Cálculo Diferencial
                        def pagina_diferencial(self):
                                nueva_ventana = tk.Toplevel(self.root)  # Crear una nueva ventana
                                nueva_ventana.title("Curso de Cálculo Diferencial")
                                nueva_ventana.geometry("800x650")
                                # Cargar la imagen de fondo
                                fondo_img = Image.open("pt0fondo.png")
                                fondo_img = fondo_img.resize((800, 650), Image.LANCZOS)  # Ajusta el tamaño de la imagen
                                fondo_photo = ImageTk.PhotoImage(fondo_img)

                                # Crear un Label con la imagen de fondo
                                fondo_label = tk.Label(nueva_ventana, image=fondo_photo)
                                fondo_label.image = fondo_photo  # Necesario para evitar que la imagen sea recolectada por el GC
                                fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

                                label = tk.Label(nueva_ventana, text="Curso de Cálculo Diferencial", font=("Impact", 22))
                                label.pack(pady=20)

                                ventana_ejercicio=tk.Toplevel()

                                # Botones de ejercicios
                                tk.Button(nueva_ventana, text="Derivada de una gráfica", font=("Verdana", 12), command=lambda: practica(1,ventana_ejercicio)).pack(pady=5)

                                tk.Button(nueva_ventana, text="Derivada de un polinomio", font=("Verdana", 12), command=lambda: practica(2,ventana_ejercicio)).pack(pady=5)

                                tk.Button(nueva_ventana, text="Derivada de un radical", font=("Verdana", 12), command=lambda: practica(3,ventana_ejercicio)).pack(pady=5)

                                tk.Button(nueva_ventana, text="Derivada de una exponencial", font=("Verdana", 12), command=lambda: practica(4,ventana_ejercicio)).pack(pady=5)

                                # Botón para ver notas de cálculo diferencial
                                tk.Button(nueva_ventana, text="Ver Notas de Cálculo Diferencial", font=("Verdana", 12),command=lambda: abrir_pdf("notas_diferencial_SBC.pdf")).pack(pady=5)

                                # Botón para cerrar la ventana 
                                tk.Button(nueva_ventana, text="Cerrar", font=("Verdana", 12, "bold"), command=nueva_ventana.destroy).pack(pady=10)

                        # Función para la página del curso de Cálculo Integral
                        def pagina_integral(self):
                                nueva_ventana = tk.Toplevel(self.root)  # Crear una nueva ventana
                                nueva_ventana.title("Curso de Cálculo Integral")
                                nueva_ventana.geometry("800x650")
                                # Cargar la imagen de fondo
                                fondo_img = Image.open("pt0fondo1.png")
                                fondo_img = fondo_img.resize((800, 650), Image.LANCZOS)  # Ajusta el tamaño de la imagen
                                fondo_photo = ImageTk.PhotoImage(fondo_img)

                                # Crear un Label con la imagen de fondo
                                fondo_label = tk.Label(nueva_ventana, image=fondo_photo)
                                fondo_label.image = fondo_photo  # Necesario para evitar que la imagen sea recolectada por el GC
                                fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

                                label = tk.Label(nueva_ventana, text="Curso de Cálculo Integral", font=("Impact", 22))
                                label.pack(pady=20)

                                ventana_ejercicio=tk.Toplevel()
                                
                                #  Botenes de ejercicios
                                tk.Button(nueva_ventana, text="Integral de una gráfica", font=("Verdana", 12), command=lambda: practica(1,ventana_ejercicio)).pack(pady=5)

                                tk.Button(nueva_ventana, text="Integral de un polinomio", font=("Verdana", 12), command=lambda: practica(5,ventana_ejercicio)).pack(pady=5)

                                tk.Button(nueva_ventana, text="Integral de un radical", font=("Verdana", 12), command=lambda: practica(6,ventana_ejercicio)).pack(pady=5)

                                tk.Button(nueva_ventana, text="Integral de una exponencial", font=("Verdana", 12), command=lambda: practica(7,ventana_ejercicio)).pack(pady=5)

                                # Botón para ver notas de cálculo integral
                                tk.Button(nueva_ventana, text="Ver Notas de Cálculo Integral", font=("Verdana", 12), command=lambda: abrir_pdf("notas_integral_SBC.pdf")).pack(pady=5)

                                # Botón para cerrar la ventana
                                tk.Button(nueva_ventana, text="Cerrar", font=("Verdana", 12, "bold"), command=nueva_ventana.destroy).pack(pady=10)

                        # Función para la página del curso de Cálculo
                        def pagina_calculos(self):
                                nueva_ventana = tk.Toplevel(self.root)  # Crear una nueva ventana
                                nueva_ventana.title("Curso de Cálculo")
                                nueva_ventana.geometry("800x650")
                                # Cargar la imagen de fondo
                                fondo_img = Image.open("pt0fondo2.png")
                                fondo_img = fondo_img.resize((800, 650), Image.LANCZOS)  # Ajusta el tamaño de la imagen
                                fondo_photo = ImageTk.PhotoImage(fondo_img)

                                # Crear un Label con la imagen de fondo
                                fondo_label = tk.Label(nueva_ventana, image=fondo_photo)
                                fondo_label.image = fondo_photo  # Necesario para evitar que la imagen sea recolectada por el GC
                                fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

                                label = tk.Label(nueva_ventana, text="Curso de Cálculo", font=("Impact", 22))
                                label.pack(pady=10)

                                label = tk.Label(nueva_ventana, text="Ejercicios de Cálculo Diferencial", font=("Verdana", 15))
                                label.pack(pady=10)

                                ventana_ejercicio=tk.Toplevel()

                                # Botón para practicar cálculo diferencial
                                tk.Button(nueva_ventana, text="Derivada de una gráfica", font=("Verdana", 12), command=lambda: practica(1,ventana_ejercicio)).pack(pady=5)

                                tk.Button(nueva_ventana, text="Derivada de un polinomio", font=("Verdana", 12), command=lambda: practica(2,ventana_ejercicio)).pack(pady=5)

                                tk.Button(nueva_ventana, text="Derivada de un radical", font=("Verdana", 12), command=lambda: practica(3,ventana_ejercicio)).pack(pady=5)

                                tk.Button(nueva_ventana, text="Derivada de una exponencial", font=("Verdana", 12), command=lambda: practica(4,ventana_ejercicio)).pack(pady=5)

                                # Botón para ver notas de cálculo diferencial
                                tk.Button(nueva_ventana, text="Ver Notas de Cálculo Diferencial", font=("Verdana", 12),command=lambda: abrir_pdf("notas_diferencial_SBC.pdf")).pack(pady=5)

                                label = tk.Label(nueva_ventana, text="Ejercicios de Cálculo Integral", font=("Verdana", 15))
                                label.pack(pady=10)

                                # Botón para practicar cálculo integral
                                tk.Button(nueva_ventana, text="Integral de una gráfica", font=("Verdana", 12), command=lambda: practica(1,ventana_ejercicio)).pack(pady=5)

                                tk.Button(nueva_ventana, text="Integral de un polinomio", font=("Verdana", 12), command=lambda: practica(5,ventana_ejercicio)).pack(pady=5)

                                tk.Button(nueva_ventana, text="Integral de un radical", font=("Verdana", 12), command=lambda: practica(6,ventana_ejercicio)).pack(pady=5)

                                tk.Button(nueva_ventana, text="Integral de una exponencial", font=("Verdana", 12), command=lambda: practica(7,ventana_ejercicio)).pack(pady=5)

                                # Botón para ver notas de cálculo integral
                                tk.Button(nueva_ventana, text="Ver Notas de Cálculo Integral", font=("Verdana", 12), command=lambda: abrir_pdf("notas_integral_SBC.pdf")).pack(pady=5)


                                tk.Button(nueva_ventana, text="Cerrar", font=("Verdana", 12, "bold"), command=nueva_ventana.destroy).pack(pady=10)
                                
                                                      
                                             
                        @Rule(Puntajes(puntajedif=P(lambda x: x < 0.5), puntajeint=P(lambda x: x < 0.5)))
                        def recomendar_ambos(self):
                                mensaje = "Se recomienda tomar el curso de Cálculo."
                                self.mostrar_pagina(mensaje, self.pagina_calculos)

                                
                        @Rule(Puntajes(puntajedif=P(lambda x: x >= 0.5), puntajeint=P(lambda x: x < 0.5)))
                        def recomendar_integral(self):
                                mensaje = "Se recomienda tomar el curso de Cálculo Integral."
                                self.mostrar_pagina(mensaje, self.pagina_integral)
    
                        @Rule(Puntajes(puntajedif=P(lambda x: x < 0.5), puntajeint=P(lambda x: x >= 0.5)))
                        def recomendar_diferencial(self):
                                mensaje = "Se recomienda tomar el curso de Cálculo Diferencial."
                                self.mostrar_pagina(mensaje, self.pagina_diferencial)
    
                        @Rule(Puntajes(puntajedif=P(lambda x: x >= 0.7), puntajeint=P(lambda x: x >= 0.7), puntajetotal=P(lambda x: x >= 0.85)))
                        def no_recomendar(self):
                                mensaje = "No es necesario tomar ningún curso."
                                self.mostrar_pagina(mensaje, self.pagina_diferencial)
    
                # Inicializar el motor de inferencia
                engine = DiagnosticoCursillo(nueva_ventana)

                # Declarar los puntajes obtenidos en un examen diagnóstico
                engine.reset()
                engine.declare(Puntajes(puntajedif=p_dif, puntajeint=p_int, puntajetotal=p_total))
                engine.run()


                # Botón para cerrar
                tk.Button(nueva_ventana, text="Cerrar", font=("Verdana", 12, "bold"), command=nueva_ventana.destroy).pack(pady=10)

        # Mostrar la primera página
        mostrar_pagina(pagina_actual)

# Si deseas probar el formulario directamente desde este archivo, puedes descomentar lo siguiente:
if __name__ == "__main__":
        root = tk.Tk()            
        abrir_nuevo_formulario()
        root.mainloop()
