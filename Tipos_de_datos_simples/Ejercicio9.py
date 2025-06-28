"""
Programa para calcular el capital obtenido en una inversión.

Este script pregunta al usuario una cantidad a invertir, el interés anual y el número de años.
Calcula el capital final usando interés compuesto y muestra el resultado por pantalla.
También guarda un historial de los cálculos realizados en un archivo 'Historial.txt'.
"""

import sys

def get_value(prompt: str) -> int | float:
    """
    Solicita al usuario un valor numérico a través de un prompt, validando la entrada.

    Args:
        prompt (str): El mensaje a mostrar al usuario.

    Returns:
        int | float: El valor ingresado por el usuario convertido a número.

    Raises:
        SystemExit: Si el usuario interrumpe el programa con Ctrl+C.
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("No digitó nada, intente de nuevo.")
                continue
            return float(user_input)
        except ValueError:
            print("Valor no válido, intente de nuevo.")
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario, saliendo...")
            sys.exit(0)

def main():
    """
    Función principal del programa.

    - Solicita la cantidad a invertir, el interés anual y el número de años.
    - Calcula el capital final usando la fórmula de interés compuesto.
    - Muestra el resultado en pantalla.
    - Guarda el cálculo en un archivo de historial.
    """
    while True:
        cantidad = float(get_value("Digite la cantidad a invertir por favor: "))
        if not cantidad > 0:
            print("La cantidad debe ser positiva, intente de nuevo.")
            continue
        break

    while True:
        interes = float(get_value("Digite el interés porcentual anual: "))
        if interes <= 0:
            print("El interés debe ser positivo, intente de nuevo.")
            continue
        break

    while True:
        años = int(get_value("Digite el número de años: "))
        if años <= 0 or años >= 100:
            print("Número de años no válido, intente de nuevo.")
            continue
        break

    capital_final = cantidad * (1 + (interes / 100)) ** años
    print(f"Con una cantidad inicial de {cantidad}, a un interés de {interes}% en {años} año(s), "
          f"su capital final es de {capital_final:.2f}")

    with open("Historial.txt", "a") as f:
        f.write(f"Cantidad inicial: {cantidad}, interés: {interes}, años: {años}, cantidad final: {capital_final:.2f}\n")

if __name__ == "__main__":
    """
    Punto de entrada del programa.

    Permite repetir el cálculo si el usuario así lo desea.
    """
    while True:
        main()
        repetir = input("¿Quiere hacer otro cálculo? (Y/N) ").strip().lower()
        if repetir != 'y':
            print("¡Hasta luego!")
            break
