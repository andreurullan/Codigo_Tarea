# test_registro.py
import unittest
from registro import RegistroApp
import tkinter as tk

class TestRegistroApp(unittest.TestCase):
    def setUp(self):
        # Configuración antes de cada prueba
        self.root = tk.Tk()
        self.app = RegistroApp(self.root)

    def tearDown(self):
        # Cerrar ventana después de cada prueba
        self.root.destroy()

    def test_registro_exitoso(self):
        # Simular entradas válidas
        self.app.nombre_entry.insert(0, "Usuario")
        self.app.correo_entry.insert(0, "usuario@ejemplo.com")
        self.app.contrasena_entry.insert(0, "contraseña123")

        # Simular clic en el botón de registro
        self.app.registrar_button.invoke()

        # Verificar mensaje de éxito
        self.assertEqual(self.app.resultado_label.cget("text"), "Registro exitoso")
   
    def test_correo_invalido(self):
        # Simular un correo inválido
        self.app.nombre_entry.insert(0, "Usuario")
        self.app.correo_entry.insert(0, "correo-invalido")
        self.app.contrasena_entry.insert(0, "contraseña123")

        # Simular clic en el botón de registro
        self.app.registrar_button.invoke()

        # Verificar mensaje de error
        self.assertEqual(self.app.resultado_label.cget("text"), "Correo no válido")

    def test_campos_vacios(self):
        # Dejar todos los campos vacíos
        self.app.nombre_entry.insert(0, "")
        self.app.correo_entry.insert(0, "")
        self.app.contrasena_entry.insert(0, "")

        # Simular clic en el botón de registro
        self.app.registrar_button.invoke()

        # Verificar mensaje de error por campos vacíos
        self.assertEqual(self.app.resultado_label.cget("text"), "Por favor, complete todos los campos")

if __name__ == "__main__":
    unittest.main()