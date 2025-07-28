"""Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo:

1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
"""

import os
import sys
from datetime import datetime

def get_numero(prompt: str) -> int:
    """
    Solicita al usuario un número entero positivo mediante un prompt.

    Parámetros:
        prompt (str): El mensaje que se mostrará al usuario.

    Retorna:
        int: Número entero positivo ingresado por el usuario.

    Manejo de errores:
        - Reintenta si el usuario no introduce nada, introduce texto no convertible a entero o un número negativo.
        - Sale del programa si se detecta una interrupción con Ctrl+C.
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("No digitó nada, intente de nuevo.")
                continue
            numero = int(user_input)
            if numero < 0:
                print("Número negativo no válido.")
                continue
            return numero
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario.")
            sys.exit(0)
        except ValueError:
            print("Valor inválido.")

def historial(numero: int) -> None:
    """
    Registra el número ingresado por el usuario junto con la fecha y hora actual en un archivo CSV.

    Parámetros:
        numero (int): Número que el usuario introdujo.
    
    Crea o actualiza:
        'historial.csv' con los datos en el formato: Fecha, numero_introducido
    """
    fecha = datetime.now().strftime("%d/%B/%y %H:%M:%S")
    archivo = "historial.csv"
    existe = os.path.isfile(archivo)
    with open(archivo, "a", encoding="utf-8", newline="") as f:
        if not existe or os.stat(archivo).st_size == 0:
            f.write("Fecha, numero_introducido\n")
        f.write(f"{fecha}, {numero}\n")

def triangulo(numero: int) -> None:
    """
    Imprime un triángulo rectángulo invertido de números impares en consola.

    El número de filas del triángulo depende del número impar más cercano al número ingresado.

    Parámetros:
        numero (int): Número entero positivo que define la altura del triángulo.
    
    Ejemplo de salida si numero = 10:
    1
    3 1
    5 3 1
    7 5 3 1
    9 7 5 3 1
    """
    for i in range(0, numero):
        if i % 2 != 0:
            for j in range(i, 0, -1):
                if j % 2 != 0:
                    print(f"{j} ", end="")
            print("\n")

def main():
    """
    Función principal del programa.
    - Solicita un número al usuario.
    - Imprime el triángulo.
    - Guarda el número ingresado en un historial.
    """
    numero = get_numero("Digite un número entero positivo: ")
    triangulo(numero)
    historial(numero)

if __name__ == "__main__":
    while True:
        main()
        rep = input("¿Desea repetir? (y/n) ").strip().lower()
        if rep != "y":
            print("¡Adiós!")
            break
