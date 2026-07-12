import random
import string

def generar_contraseña(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longitud))

print("Generador de Contraseñas")

while True:
    try:
        longitud = int(input("Ingrese la longitud de la contraseña: "))
        break
    except ValueError:
        print("Sistema: Debes ingresar un número válido")

print("Contraseña generada:", generar_contraseña(longitud))
input()
