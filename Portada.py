import tkinter as tk
from tkinter import messagebox
import sqlite3

# Función para manejar el inicio de sesión
def login():
    usuario = user_entry.get()  # Obtiene el texto del campo de usuario
    contraseña = password_entry.get()  # Obtiene el texto del campo de contraseña

    # Conectar a la base de datos
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()

    # Buscar el usuario y contraseña en la tabla 'usuarios'
    cursor.execute('SELECT id FROM usuarios WHERE usuario=? AND contraseña=?', (usuario, contraseña))
    resultado = cursor.fetchone()

    if resultado:
        user_id = resultado[0]

        # Si el login es exitoso, buscar los datos personales en la tabla 'datos_personales'
        cursor.execute('SELECT nombre, apellido, correo FROM datos_personales WHERE id=?', (user_id,))
        datos = cursor.fetchone()

        if datos:
            nombre, apellido, correo = datos
            messagebox.showinfo("Inicio de Sesión", f"Bienvenido {nombre} {apellido}\nCorreo: {correo}")
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    conn.close()

# Crear la ventana principal
root = tk.Tk()
root.title("Portada")

# Crear etiquetas con el texto deseado
label1 = tk.Label(root, text="Universidad Autónoma de Hidalgo", font=("Arial", 16, "bold"))
label2 = tk.Label(root, text="Tutorial Inteligente de Cálculo", font=("Arial", 14))
label3 = tk.Label(root, text="Sistemas Basados en Conocimiento", font=("Arial", 14))
label4 = tk.Label(root, text="Profesora: Martha Idalid Rivera González", font=("Arial", 12, "italic"))
label5 = tk.Label(root, text="Alumnos: Rafael Nieves Álvarez", font=("Arial", 12))

# Empaquetar las etiquetas en la ventana
label1.pack(pady=10)
label2.pack(pady=5)
label3.pack(pady=5)
label4.pack(pady=10)
label5.pack(pady=5)

# Crear una etiqueta para el Login
login_label = tk.Label(root, text="Login", font=("Arial", 14, "bold"))
login_label.pack(pady=20)

# Crear etiquetas y campos de entrada para usuario y contraseña
user_label = tk.Label(root, text="Usuario:", font=("Arial", 12))
user_label.pack()
user_entry = tk.Entry(root, font=("Arial", 12))
user_entry.pack(pady=5)

password_label = tk.Label(root, text="Contraseña:", font=("Arial", 12))
password_label.pack()
password_entry = tk.Entry(root, font=("Arial", 12), show="*")
password_entry.pack(pady=5)

# Crear un botón de inicio de sesión
login_button = tk.Button(root, text="Iniciar Sesión", font=("Arial", 12), command=login)
login_button.pack(pady=10)

# Iniciar el loop principal
root.mainloop()
