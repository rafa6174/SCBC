import tkinter as tk

# Función para abrir la ventana con el nuevo formulario
def abrir_nuevo_formulario():
    nueva_ventana = tk.Toplevel()
    nueva_ventana.title("Nuevo Formulario")

    # Aquí puedes añadir los widgets del nuevo formulario
    tk.Label(nueva_ventana, text="Formulario Principal", font=("Arial", 16, "bold")).pack(pady=20)

    # Ejemplo de campos para el formulario
    tk.Label(nueva_ventana, text="Campo 1:", font=("Arial", 12)).pack(pady=5)
    campo1_entry = tk.Entry(nueva_ventana, font=("Arial", 12))
    campo1_entry.pack()
    tk.Label(nueva_ventana, text="Campo 2:", font=("Arial", 12)).pack(pady=5)
    campo2_entry = tk.Entry(nueva_ventana, font=("Arial", 12))
    campo2_entry.pack()

    tk.Button(nueva_ventana, text="Guardar", font=("Arial", 12)).pack(pady=20)

# Si deseas probar el formulario directamente desde este archivo, puedes descomentar lo siguiente:
# if __name__ == "__main__":
#     root = tk.Tk()
#     abrir_nuevo_formulario()
#     root.mainloop()
