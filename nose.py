import sys
import time

operador = input("Sistema: Identifícate: ")
if operador == "Alejandro":
    print("Sistema: Bienvenido Alejandro")

    while True:
        try:
            acción = int(input("Sistema: ¿Qué acción quiere realizar? "))
        except ValueError:
            print("Sistema: Debes ingresar un número válido")
            input()
            continue  # vuelve a pedir la acción
            
        if acción == 1:
            print("Sistema: 100")
            input()
            break
        elif acción == 2:
            print("Sistema: 200")
            input()
            break
        elif acción == 3:
            print("Sistema: 300")
            input()
            break
        elif acción == 4:
            print("Sistema: 400")
            input()
            break
        elif acción == 5:
            print("Sistema: 500")
            input()
            break
        else:
            print("Sistema: Acción no válida")
            # vuelve al inicio del bucle

    sys.exit()

else:
    print("Sistema: Acceso denegado")
    time.sleep(1)
    sys.exit()
