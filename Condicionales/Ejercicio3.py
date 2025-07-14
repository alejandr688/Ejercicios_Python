"""
Programa que pide al usuario dos números y muestra por pantalla su división.
Si el divisor es cero, muestra un mensaje de error. Además, guarda cada intento exitoso en un archivo de historial con fecha y hora.
"""

import sys
from datetime import datetime

def get_numeros(prompt: str) -> float:
    """
    Solicita al usuario que introduzca un número flotante mediante un mensaje personalizado.

    Parámetros:
    ----------
    prompt : str
        Mensaje que se muestra al usuario para solicitar la entrada.

    Retorna:
    -------
    float
        El número ingresado por el usuario convertido a tipo float.

    Maneja:
    ------
    - Entrada vacía
    - Valor no convertible a float
    - Interrupción por teclado (Ctrl + C)
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("No digitó nada.")
                continue
            return float(user_input)
        except ValueError:
            print("Número no válido, digite uno válido ahora.")
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario. Saliendo...")
            sys.exit(0)

def main():
    """
    Ejecuta la lógica principal del programa:
    - Solicita dos números al usuario.
    - Realiza la división si el divisor no es cero.
    - Muestra el resultado formateado con dos decimales.
    - Guarda la operación en un archivo de historial con la fecha y hora.
    - Maneja la excepción de división entre cero.
    """
    while True:
        try:
            x = get_numeros("Digite un número por favor: ")
            y = get_numeros("Ahora digite otro :D : ")
            division = x / y
            print(f"La división de {x} entre {y} es {division:.2f}")
            fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("Historial.txt", "a", encoding="utf-8") as f:
                f.write(f"\nFecha de intento({fecha}):\n{x} dividido entre {y} da {division:.2f}")
            break
        except ZeroDivisionError:
            print("División entre cero no válida, intente de nuevo.")

if __name__ == "__main__":
    while True:
        main()
        rep = input("¿Quiere repetir el programa? (Y/N) ").strip().lower()
        if rep != "y":
            print("Bye!")
            break
