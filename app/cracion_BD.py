import sqlite3

# Conexión a la base de datos (crea la base de datos si no existe)
conn = sqlite3.connect('usuarios.db')

# Crear un cursor
cursor = conn.cursor()

# Crear tabla usuarios
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT NOT NULL UNIQUE,
    contraseña TEXT NOT NULL
)
''')

# Crear tabla datos_personales
cursor.execute('''
CREATE TABLE IF NOT EXISTS datos_personales (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    correo TEXT NOT NULL,
    FOREIGN KEY(id) REFERENCES usuarios(id)
)
''')

# Guardar cambios y cerrar la conexión
conn.commit()
conn.close()
