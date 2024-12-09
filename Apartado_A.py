import re

while True:
    
    contraseña = input("Introduce una contraseña para validar: ")

    # Requisitos de la contraseña
    longitud = len(contraseña) >= 8
    mayuscula = any(char.isupper() for char in contraseña)
    minuscula = any(char.islower() for char in contraseña)
    numero = any(char.isdigit() for char in contraseña)
    caracter = re.search(r'[!@#$%^&*(),.?":{}|<>]', contraseña) is not None

    # Validaciones 
    if not longitud:
        print("La contraseña debe tener al menos 8 caracteres.")

    if not mayuscula:
        print("La contraseña debe incluir al menos una mayúscula.")

    if not minuscula:
        print("La contraseña debe incluir al menos una minúscula.")

    if not numero:
        print("La contraseña debe incluir al menos un número.")

    if not caracter:
        print("La contraseña debe incluir al menos un carácter especial")

    # Verificamos si la contraseña es válida
    if longitud and mayuscula and minuscula and numero and caracter:
        print("Contraseña correcta.")
        break  
    else:
        print("Mec!!! error, vuelve a probar \n")