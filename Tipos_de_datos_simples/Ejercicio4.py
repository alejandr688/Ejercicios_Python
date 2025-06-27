#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Programa interactivo para calcular la operación aritmética ((a + b) / (c * d)) ** 2
Solicita al usuario los valores de a, b, c y d, realiza la operación y muestra el resultado.
Permite repetir el cálculo tantas veces como el usuario desee.
"""

import sys

def get_values(prompt: str) -> float:
    """
    Solicita al usuario un valor numérico con el mensaje especificado.

    Args:
        prompt (str): Mensaje que se muestra al solicitar el valor.

    Returns:
        float: Valor numérico introducido por el usuario.

    Control de errores:
        - Si el usuario no introduce nada, se solicita de nuevo.
        - Si el usuario introduce un valor no numérico, se solicita de nuevo.
        - Si el usuario interrumpe el programa con Ctrl+C, el programa se detiene educadamente.
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("Número inválido, intente de nuevo.")
                continue
            n = float(user_input)
            return n
        except ValueError:
            print("Número inválido, intente de nuevo.")
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario.")
            sys.exit()

def main():
    """
    Ejecuta el flujo principal del programa:
    - Muestra un mensaje de bienvenida.
    - Solicita los valores de a, b, c y d al usuario.
    - Calcula la operación ((a + b) / (c * d)) ** 2.
    - Muestra el resultado con dos decimales.
    - Maneja el caso de división por cero mostrando un mensaje de error.
    """
    print("Bienvenido a mi programa, haremos la siguiente operación: ((a + b) / (c * d)) ** 2")
    a = get_values("Escribe el valor de a: ")
    b = get_values("Escribe el valor de b: ")
    c = get_values("Escribe el valor de c: ")
    d = get_values("Escribe el valor de d: ")
    try:
        operacion = ((a + b) / (c * d)) ** 2
        print(f"El resultado de la operación es {operacion:.2f}")
    except ZeroDivisionError:
        print("Error, división entre 0 no válida.")

if __name__ == "__main__":
    while True:
        main()
        again = input("¿Quieres hacer otra operación? (Y/N): ").strip().lower()
        if again != "y":
            print("¡Hasta luego!")
            break
