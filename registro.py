# registro.py
import tkinter as tk
from tkinter import messagebox
import re

class RegistroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Usuario")

        # Campos del formulario
        self.nombre_label = tk.Label(root, text="Nombre")
        self.nombre_label.pack()
        self.nombre_entry = tk.Entry(root)
        self.nombre_entry.pack()
        
       #Añadir correo y contraseña.

        self.correo_label = tk.Label(root, text="Correo")
        self.correo_label.pack()
        self.correo_entry = tk.Entry(root)
        self.correo_entry.pack()

        self.contrasena_label = tk.Label(root, text="Contraseña")
        self.contrasena_label.pack()
        self.contrasena_entry = tk.Entry(root, show="*")
        self.contrasena_entry.pack()

        # Botón de registro
        self.registrar_button = tk.Button(root, text="Registrar", command=self.registrar_usuario)
        self.registrar_button.pack()

        # Etiqueta para mensajes de resultado
        self.resultado_label = tk.Label(root, text="")
        self.resultado_label.pack()

    def registrar_usuario(self):
        nombre = self.nombre_entry.get()
        #registar correo y contraseña
        correo = self.correo_entry.get()
        contrasena = self.contrasena_entry.get()

        if not nombre or not correo or not contrasena:
            self.resultado_label.config(text="Por favor, complete todos los campos")
        elif not self.validar_correo(correo):
            self.resultado_label.config(text="Correo no válido")
        else:
            self.resultado_label.config(text="Registro exitoso")

    def validar_correo(self, correo):
        # Expresión regular para verificar formato de correo
        regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return re.match(regex, correo) is not None

if __name__ == "__main__":
    root = tk.Tk()
    app = RegistroApp(root)
    root.mainloop()
    