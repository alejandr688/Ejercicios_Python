"""Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar, 
además de guardar un historial con la fecha y el tipo de número (par o impar)."""

import sys
from datetime import datetime

def get_numero(prompt: str) -> int:
    """
    Solicita al usuario un número entero por consola.

    Args:
        prompt (str): Mensaje a mostrar al usuario.

    Returns:
        int: Número entero ingresado por el usuario.

    Maneja errores:
        - Si no se ingresa nada, vuelve a solicitar el dato.
        - Si se ingresa un valor no numérico, muestra un mensaje de error.
        - Si el usuario interrumpe con Ctrl+C, sale del programa con un mensaje.
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("No digitó nada, intente de nuevo.")
                continue
            return int(user_input)
        except ValueError:
            print("Número no válido, debe digitar un número entero.")
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario. Saliendo...\n")
            sys.exit(0)

def guardar_historial(numero: int, tipo: str) -> None:
    """
    Guarda en un archivo el número ingresado con su clasificación y la fecha actual.

    Args:
        numero (int): El número ingresado por el usuario.
        tipo (str): Tipo de número ("par" o "impar").
    """
    with open("Historial.txt", "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"\n{timestamp}\n{numero} es {tipo}\n")

def main():
    """
    Ejecuta el proceso principal:
    - Solicita un número al usuario.
    - Determina si es par o impar.
    - Muestra el resultado en pantalla.
    - Guarda el resultado en un archivo de historial.
    """
    numero = get_numero("Digite un número entero por favor: ")
    if numero % 2 == 0:
        print("Es número par.")
        guardar_historial(numero, "par")
    else:
        print("Es un número impar.")
        guardar_historial(numero, "impar")

if __name__ == "__main__":
    while True:
        main()
        rep = input("¿Quiere repetir? (Y/N): ").strip().lower()
        if rep != "y":
            print("¡Adiós!")
            break
