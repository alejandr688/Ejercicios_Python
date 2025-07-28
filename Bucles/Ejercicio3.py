"""Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas."""

import sys
import os
from datetime import datetime

def get_numero(prompt: str) -> int:
    """
    Solicita al usuario un número entero positivo.

    Args:
        prompt (str): Mensaje que se muestra al usuario.

    Returns:
        int: Número entero positivo ingresado por el usuario.

    Manejo de errores:
        - Si el usuario no introduce nada o introduce un valor no numérico, se le solicita de nuevo.
        - Si se interrumpe con Ctrl+C, el programa se cierra.
        - Si se introduce un número negativo, se rechaza.
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("No digitó nada, intente de nuevo. ")
                continue
            n = int(user_input)
            if n < 0:
                print("No puede digitar un número negativo. ")
                continue
            return n
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario. ")
            sys.exit(0)
        except ValueError:
            print("Dato no válido. ")

def historial(numero: int)->None:
    """
    Guarda en un archivo CSV la fecha y el número introducido por el usuario.

    Args:
        numero (int): Número ingresado por el usuario.

    Crea o actualiza el archivo 'Historial.csv'.
    Si es la primera vez que se escribe, agrega encabezados.
    """
    fecha = datetime.now().strftime("%d/%m/%y %H:%M:%S")
    archivo = "Historial.csv"
    existe = os.path.isfile(archivo)
    with open(archivo, "a", encoding="utf-8", newline="") as f:
        if not existe or os.stat(archivo).st_size == 0:
            f.write("Fecha, numero introducido\n")
        f.write(f"{fecha}, {numero}\n")

def main():
    """
    Función principal del programa.

    - Solicita un número al usuario.
    - Guarda el número en el historial.
    - Muestra en pantalla todos los números impares desde 1 hasta el número ingresado.
    """
    numero = get_numero("Digite un número entero positivo: ")
    historial(numero)
    impares = [str(i) for i in range(1, numero + 1) if i % 2 != 0]
    print(", ".join(impares))


if __name__ == "__main__":
    while True:
        main()
        rep = input("\n¿Quiere repetir? (y/n) ").strip().lower()
        if rep != "y":
            print("¡Adios!")
            break
