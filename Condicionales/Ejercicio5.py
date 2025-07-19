"""
Programa para determinar si un usuario debe tributar un impuesto.

Según la normativa, se debe tributar si se tienen más de 16 años y
unos ingresos iguales o superiores a 1000 dólares mensuales.

El programa solicita al usuario su edad y sus ingresos, determina si
debe tributar y guarda un registro en un archivo con marca de tiempo.
"""

import sys
from datetime import datetime

def get_numero(prompt: str) -> float:
    """
    Solicita al usuario un número (edad o ingreso) con validación.

    Args:
        prompt (str): El mensaje que se le mostrará al usuario.

    Returns:
        float: El número ingresado por el usuario.

    Manejo de errores:
        - Si el usuario no ingresa nada, se vuelve a pedir.
        - Si el valor no puede convertirse a float, se muestra un error.
        - Si el usuario interrumpe el programa con Ctrl+C, se sale con un mensaje.
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("No digitó nada, intente de nuevo.")
                continue
            return float(user_input)
        except ValueError:
            print("Dato no válido")
        except KeyboardInterrupt:
            print("Programa interrumpido por el usuario. Saliendo...")
            sys.exit(0)

def historial(edad: int, ingreso: float, tributar: str):
    """
    Guarda en un archivo los datos del usuario y si debe tributar.

    Args:
        edad (int): Edad del usuario.
        ingreso (float): Ingreso mensual del usuario.
        tributar (str): Resultado de si tiene que tributar o no.
    """
    with open("Historial.txt", "a") as f:
        fecha = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
        f.write(f"\n{fecha}\nEdad: {edad}, Ingreso: ${ingreso:.2f}, Resultado: {tributar}\n")

def main():
    """
    Ejecuta el flujo principal del programa:
    - Solicita la edad del usuario y valida que sea un número entero no negativo.
    - Solicita los ingresos del usuario y valida que sea un número no negativo.
    - Determina si el usuario debe tributar.
    - Muestra el resultado y lo guarda en un archivo.
    """
    while True:
        edad = get_numero("Digite su edad por favor (número entero): ")
        if edad < 0 or not edad.is_integer():
            print("Edad no válida, intente de nuevo.")
            continue
        edad = int(edad)
        break

    while True:
        ingreso = get_numero("Digite sus ingresos por favor: ")
        if ingreso < 0:
            print("Ingreso no válido.")
            continue
        break

    if edad > 16 and ingreso >= 1000:
        print("Tiene que tributar.")
        historial(edad, ingreso, "tiene que tributar")
    else:
        print("No tiene que tributar.")
        historial(edad, ingreso, "no tiene que tributar")

if __name__ == "__main__":
    while True:
        main()
        rep = input("¿Quiere repetir el programa? (Y/N) ").strip().lower()
        if rep != "y":
            print("¡Adiós!")
            break
