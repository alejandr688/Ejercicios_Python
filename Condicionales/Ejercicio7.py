"""Programa que solicita al usuario su renta anual y muestra el tipo impositivo correspondiente.
   También guarda el historial en un archivo CSV con la fecha, renta y tipo impositivo aplicado.
"""

import sys
from datetime import datetime

def get_renta(prompt: str) -> float:
    """
    Solicita al usuario un valor numérico de renta anual válido.

    Args:
        prompt (str): El mensaje que se muestra al usuario para solicitar la entrada.

    Returns:
        float: La renta anual proporcionada por el usuario.

    Maneja errores como valores vacíos, negativos, no numéricos o interrupciones del teclado.
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("No digitó nada, intente de nuevo. ")
                continue
            if float(user_input) < 0:
                print("El valor no puede ser negativo, intente de nuevo. ")
                continue
            return float(user_input)
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario. Saliendo")
            sys.exit(0)
        except ValueError:
            print("Valor no válido. ")

def condiciones(renta: float) -> str:
    """
    Determina el tipo impositivo aplicable según la renta anual del usuario.

    Args:
        renta (float): La renta anual del usuario.

    Returns:
        str: El porcentaje de impuesto correspondiente como cadena con símbolo '%'.
    """
    if renta < 10e3:
        return "5%"
    elif 10e3 <= renta <= 20e3:
        return "15%"
    elif 20e3 < renta <= 35e3:
        return "20%"
    elif 35e3 < renta <= 60e3:
        return "30%"
    elif renta > 60e3:
        return "45%"

def main():
    """
    Ejecuta el flujo principal del programa:
    - Solicita la renta anual.
    - Muestra el tipo impositivo correspondiente.
    - Guarda los datos con la fecha y hora en un archivo CSV llamado 'Historial.csv'.
    """
    renta = get_renta("Digite su renta anual por favor: ")
    print(f"El tipo impositivo que le corresponde es: {condiciones(renta)} ")
    with open("Historial.csv", "a") as f:
        fecha = datetime.now().strftime("%d/%B/%y, %H:%M:%S")
        f.write(f"\n{fecha},{renta:.2f},{condiciones(renta)}")

if __name__ == "__main__":
    while True:
        main()
        rep = input("¿Desea repetir el programa?(Y/N) ").strip().lower()
        if rep != "y":
            print("¡Adiós!")
            break
