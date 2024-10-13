# Creamos una nueva ventana solo si es necesario
                if index >= len(ejercicios):
                        tk.Label(nueva_ventana, text="¡Has completado todos los ejercicios de cálculo diferencial!").pack(pady=10)
                        index=index+1
                        return

                # Llamamos al ejercicio actual
                ejercicios[index](nueva_ventana)
                index=index+1

                if index < len(ejercicios) - 1:
                        siguiente_btn = tk.Button(nueva_ventana, text="Siguiente ejercicio",
                                                  command=lambda: mostrar_ejercicio(index + 1))
                        siguiente_btn.pack(pady=10)
                        index=index+1
