from experta import *
import tkinter as tk
from tkinter import ttk

# Función para crear el formulario con las preguntas
def abrir_nuevo_formulario():
        nueva_ventana = tk.Toplevel()
        nueva_ventana.title("Examen diagnóstico")

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
                tk.Label(nueva_ventana, text="Resultados del examen diagnóstico", font=("Arial", 16, "bold")).pack(pady=10)
                tk.Label(nueva_ventana, text=f"Puntaje diferencial: {puntaje_dif}/{preguntas_dif}", font=("Arial", 14)).pack(pady=10)
                tk.Label(nueva_ventana, text=f"Puntaje integral: {puntaje_int}/{preguntas_int}", font=("Arial", 14)).pack(pady=10)
                tk.Label(nueva_ventana, text=f"Puntaje total: {puntaje_total}/{total_preguntas}", font=("Arial", 14)).pack(pady=10)
                tk.Label(nueva_ventana, text="Resultados del curso a tomar", font=("Arial", 16, "bold")).pack(pady=10)


                # Sistema experto que determina el curso que se debe tomar
                puntajedif = puntaje_dif / preguntas_dif
                puntajeint = puntaje_int / preguntas_int
                puntajetotal = puntaje_total / total_preguntas

                class ExamenDiagnostico(Fact):
                        pass

                class SistemaExperto1(KnowledgeEngine):
                        @Rule(ExamenDiagnostico(puntaje1=P(lambda x: x < 0.5)))
                        def necesita_curso(self):
                                tk.Label(nueva_ventana, text="Debe tomar el curso de cálculo.", font=("Arial", 14, "italic")).pack(pady=10)

                        @Rule(ExamenDiagnostico(puntaje1=P(lambda x: x >= 0.5)))
                        def no_necesita_curso(self):
                                tk.Label(nueva_ventana, text="No necesita tomar el curso de cálculo.", font=("Arial", 14, "italic")).pack(pady=10)

                class SistemaExperto2(KnowledgeEngine):
                        @Rule(ExamenDiagnostico(puntaje2=P(lambda x: x < 0.5)))
                        def necesita_curso(self):
                                tk.Label(nueva_ventana, text="Debe tomar el curso de cálculo diferencial.", font=("Arial", 14, "italic")).pack(pady=10)

                        @Rule(ExamenDiagnostico(puntaje2=P(lambda x: x >= 0.5)))
                        def no_necesita_curso(self):
                                tk.Label(nueva_ventana, text="No necesita tomar el curso de cálculo diferencial.", font=("Arial", 14, "italic")).pack(pady=10)

                class SistemaExperto3(KnowledgeEngine):
                        @Rule(ExamenDiagnostico(puntaje3=P(lambda x: x < 0.5)))
                        def necesita_curso(self):
                                tk.Label(nueva_ventana, text="Debe tomar el curso de cálculo integral.", font=("Arial", 14, "italic")).pack(pady=10)

                        @Rule(ExamenDiagnostico(puntaje3=P(lambda x: x >= 0.5)))
                        def no_necesita_curso(self):
                                tk.Label(nueva_ventana, text="No necesita tomar el curso de cálculo integral.", font=("Arial", 14, "italic")).pack(pady=10)

                # Para sistema experto 1
                engine = SistemaExperto1()
                engine.reset()
                engine.declare(ExamenDiagnostico(puntaje1=puntajetotal))
                engine.run()

                # Para sistema experto 2
                engine = SistemaExperto2()
                engine.reset()
                engine.declare(ExamenDiagnostico(puntaje2=puntajedif))
                engine.run()

                # Para sistema experto 3
                engine = SistemaExperto3()
                engine.reset()
                engine.declare(ExamenDiagnostico(puntaje3=puntajeint))
                engine.run()

                # Botón para cerrar
                tk.Button(nueva_ventana, text="Cerrar", font=("Arial", 12), command=nueva_ventana.destroy).pack(pady=20)

        # Mostrar la primera página
        mostrar_pagina(pagina_actual)

# Si deseas probar el formulario directamente desde este archivo, puedes descomentar lo siguiente:
if __name__ == "__main__":
        root = tk.Tk()
        abrir_nuevo_formulario()
        root.mainloop()
