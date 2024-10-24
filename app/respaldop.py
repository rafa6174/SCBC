def diferncial(opcion):
    match opcion:
        case 1:
                for widget in nueva_ventana.winfo_children():
                        widget.destroy()
                grafpol.mostrar_ejercicio_grafica(wn)
        case 2:
                for widget in nueva_ventana.winfo_children():
                        widget.destroy()
                cursodif.crear_ejercicio(wn)
        case 3:
                for widget in nueva_ventana.winfo_children():
                        widget.destroy()
                cursodif.crear_ejercicio(wn)
        case 4:
                for widget in nueva_ventana.winfo_children():
                        widget.destroy()
                derac.mostrar_ejercicio_derivada_sqrt(wn)
        case 5:
                for widget in nueva_ventana.winfo_children():
                        widget.destroy()
                derexp.mostrar_ejercicio_derivada_exp(wn
        case _:
                return "Caso por defecto"

# Función para practicar cálculo diferencial
def practicar_diferencial():
        nueva_ventana = tk.Toplevel()
        opcion=1
        while opcion<=5:
                diferencial(opcion)
                boton_frame = tk.Frame(nueva_ventana)
                boton_frame.pack(pady=10)

                if opcion > 0:
                        tk.Button(boton_frame, text="Anterior", font=("Arial", 12), command=lambda: cambiar_pagina(pagina - 1)).pack(side=tk.LEFT, padx=10)

                if opcion < 5:
                        tk.Button(boton_frame, text="Siguiente", font=("Arial", 12), command=lambda: cambiar_pagina(pagina + 1)).pack(side=tk.RIGHT, padx=10)
                else:
                        tk.Button(boton_frame, text="Finalizar", font=("Arial", 12), command=finalizar_formulario).pack(side=tk.RIGHT, padx=10)
