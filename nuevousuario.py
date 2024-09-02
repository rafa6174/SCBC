import sqlite3

conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()

# Insertar datos en usuarios
cursor.execute('''
INSERT INTO usuarios (usuario, contraseña)
VALUES ('rafael', '1234')
''')

# Obtener el id del último usuario insertado
user_id = cursor.lastrowid

# Insertar datos en datos_personales
cursor.execute('''
INSERT INTO datos_personales (id, nombre, apellido, correo)
VALUES (?, 'Rafael', 'Nieves', 'nievesalvarez1618@gmail.com')
''', (user_id,))

conn.commit()
conn.close()
