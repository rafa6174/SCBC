import tkinter as tk
from tkinter import messagebox
import sqlite3
import examen_diagnostico

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

        # Ocultar la ventana de login
        root.withdraw()

        # Llamar al nuevo formulario desde el otro archivo
        examen_diagnostico.abrir_nuevo_formulario()

    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    conn.close()

# Función para abrir la ventana de registro
def abrir_formulario_registro():
    # Crear una nueva ventana
    ventana_registro = tk.Toplevel(root)
    ventana_registro.title("Registro de Usuario")

    # Etiquetas y campos de entrada para los datos de registro
    tk.Label(ventana_registro, text="Nombre:", font=("Arial", 12)).pack(pady=5)
    nombre_entry = tk.Entry(ventana_registro, font=("Arial", 12))
    nombre_entry.pack()

    tk.Label(ventana_registro, text="Apellido:", font=("Arial", 12)).pack(pady=5)
    apellido_entry = tk.Entry(ventana_registro, font=("Arial", 12))
    apellido_entry.pack()

    tk.Label(ventana_registro, text="Correo Electrónico:", font=("Arial", 12)).pack(pady=5)
    correo_entry = tk.Entry(ventana_registro, font=("Arial", 12))
    correo_entry.pack()

    tk.Label(ventana_registro, text="Usuario:", font=("Arial", 12)).pack(pady=5)
    usuario_entry = tk.Entry(ventana_registro, font=("Arial", 12))
    usuario_entry.pack()

    tk.Label(ventana_registro, text="Contraseña:", font=("Arial", 12)).pack(pady=5)
    contraseña_entry = tk.Entry(ventana_registro, font=("Arial", 12), show="*")
    contraseña_entry.pack()

    # Función para registrar al usuario en la base de datos
    def registrar_usuario():
        nombre = nombre_entry.get()
        apellido = apellido_entry.get()
        correo = correo_entry.get()
        usuario = usuario_entry.get()
        contraseña = contraseña_entry.get()

        # Validar que no haya campos vacíos
        if not (nombre and apellido and correo and usuario and contraseña):
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        # Conectar a la base de datos
        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()

        # Insertar el nuevo usuario en la tabla usuarios
        try:
            cursor.execute('''
                INSERT INTO usuarios (usuario, contraseña)
                VALUES (?, ?)
            ''', (usuario, contraseña))

            # Obtener el id del último usuario insertado
            user_id = cursor.lastrowid

            # Insertar los datos personales en la tabla datos_personales
            cursor.execute('''
                INSERT INTO datos_personales (id, nombre, apellido, correo)
                VALUES (?, ?, ?, ?)
            ''', (user_id, nombre, apellido, correo))

            conn.commit()
            messagebox.showinfo("Registro exitoso", "El usuario ha sido registrado con éxito")
            ventana_registro.destroy()  # Cerrar la ventana de registro
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "El nombre de usuario ya existe")
        finally:
            conn.close()

    # Botón para registrar al usuario
    tk.Button(ventana_registro, text="Registrar", font=("Arial", 12), command=registrar_usuario).pack(pady=20)

# Crear la ventana principal
root = tk.Tk()
root.title("Portada")

# Crear etiquetas con el texto deseado
label1 = tk.Label(root, text="Universidad Autónoma de Hidalgo", font=("Arial", 16, "bold"))
label2 = tk.Label(root, text="Tutorial Inteligente de Cálculo Diferencial", font=("Arial", 14))
label3 = tk.Label(root, text="Sistemas Basados en Conocimiento", font=("Arial", 14))
label4 = tk.Label(root, text="Profesora: Martha Idalid Rivera González", font=("Arial", 12, "italic"))
label5 = tk.Label(root, text="Alumnos: Rafael Nieves Álvarez, Loren Clavel Nolasco Hernández", font=("Arial", 12))

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

# Crear un botón para abrir el formulario de registro
register_button = tk.Button(root, text="Registrar", font=("Arial", 12), command=abrir_formulario_registro)
register_button.pack(pady=10)

# Iniciar el loop principal
root.mainloop()
