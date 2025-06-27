#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Programa interactivo que pregunta al usuario el número de horas trabajadas y el coste por hora,
calcula la paga correspondiente y la muestra por pantalla. Permite repetir la operación si el
usuario lo desea. Incluye validación de entrada y manejo de errores para mejorar la experiencia
del usuario.
"""

import sys

def get_values(prompt: str) -> float:
    """
    Solicita al usuario un número flotante válido a través de la entrada estándar.

    Args:
        prompt (str): Mensaje que se muestra para solicitar el dato.

    Returns:
        float: Número flotante ingresado por el usuario.

    Comportamiento:
        - Si el usuario introduce un valor no numérico, se solicita de nuevo.
        - Si el usuario presiona Ctrl+C, el programa se cierra ordenadamente.
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("Valor no válido, intente de nuevo.")
                continue
            valor = float(user_input)
            return valor
        except ValueError:
            print("Dato inválido, intente de nuevo.")
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario.")
            sys.exit()

def main():
    """
    Ejecuta el flujo principal del cálculo:
    - Solicita al usuario el número de horas trabajadas y el coste por hora.
    - Verifica que los valores sean positivos.
    - Calcula la paga correspondiente como horas * coste por hora.
    - Muestra el resultado formateado con dos decimales.
    """
    while True:
        horas_trabajadas = get_values("Digite el número de horas trabajadas por favor: ")
        if horas_trabajadas < 0:
            print("Número de horas trabajadas inválido, intente de nuevo.")
            continue

        coste_hora = get_values("Digite el coste por hora: ")
        if coste_hora < 0:
            print("El coste por hora no puede ser un número negativo, intente de nuevo.")
            continue

        print(f"La paga que le corresponde es de {coste_hora * horas_trabajadas:.2f} $")
        break

if __name__ == "__main__":
    while True:
        main()
        again = input("¿Quieres hacer otra operación? (Y/N): ").strip().lower()
        if again != "y":
            print("¡Hasta pronto!")
            break
