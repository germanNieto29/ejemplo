import sqlite3
import tkinter as tk
from tkinter import messagebox

# Conexión a la base de datos
conn = sqlite3.connect("basededatos.db")
cursor = conn.cursor()

# Crear tabla si no existe
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

    # Validación básica
    if not nombre or not edad:
        messagebox.showerror("Error", "Todos los campos son obligatorios.")
        return
    if not edad.isdigit():
        messagebox.showerror("Error", "La edad debe ser un número.")
        return

    try:
        cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", (nombre, int(edad)))
        conn.commit()
        messagebox.showinfo("Éxito", f"Usuario '{nombre}' agregado correctamente.")
        entry_nombre.delete(0, tk.END)
        entry_edad.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al agregar el usuario:\n{e}")

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
print ("este mensaje fue echo desde github.com")
print ("prueba rama")
