import sqlite3
import tkinter as tk

# Conexión a la base de datos
conn = sqlite3.connect("basededatos.db")
cursor = conn.cursor()

# Crear tabla (solo la primera vez, luego comenta esta línea)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        nombre TEXT,
        edad INTEGER
    )
''')
conn.commit()

# Función para agregar usuario
def agregar_usuario():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", (nombre, edad))
    conn.commit()

# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Base de Datos con Tkinter")

tk.Label(ventana, text="Nombre:").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Edad:").pack()
entry_edad = tk.Entry(ventana)
entry_edad.pack()

tk.Button(ventana, text="Agregar Usuario", command=agregar_usuario).pack()

ventana.mainloop()