"""
Programa para calcular la suma de los n primeros enteros positivos.

Este programa solicita al usuario un número entero positivo n e imprime
la suma de todos los enteros desde 1 hasta n usando la fórmula:
    suma = n(n + 1) / 2

"""

import sys

def get_number(prompt: str) -> int:
    """
    Solicita al usuario que introduzca un número entero positivo.

    Muestra un mensaje especificado por `prompt` y valida la entrada:
    - Si el usuario introduce un número negativo, vuelve a preguntar.
    - Si la entrada no es un número válido, vuelve a preguntar.
    - Si el usuario interrumpe el programa con Ctrl+C, sale limpiamente.

    Args:
        prompt (str): Mensaje a mostrar al usuario.

    Returns:
        int: Número entero positivo introducido por el usuario.
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("No digitó nada, intente de nuevo.")
                continue
            n = int(user_input)
            if n < 0:
                print("El número no puede ser negativo.")
                continue
            return n
        except ValueError:
            print("Número no válido.")
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario.")
            sys.exit()

def main():
    """
    Función principal del programa.

    Llama a `get_number()` para leer un número entero positivo del usuario,
    calcula la suma de los enteros desde 1 hasta n usando la fórmula
    suma = n(n + 1)/2, y muestra el resultado.
    """
    while True:
        n = get_number("Digite un número entero positivo: ")
        print(f"La suma de 1 hasta {n} es {n * (n + 1) / 2:.0f}")
        break

if __name__ == "__main__":
    while True:
        main()
        rep = input("¿Quiere hacer otra suma? (Y/N) ").strip().lower()
        if rep != "y":
            print("¡Hasta luego!")
            break
