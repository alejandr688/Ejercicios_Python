"""
Programa que solicita al usuario un número entero positivo y muestra por pantalla 
la cuenta regresiva desde ese número hasta cero, separados por comas.
Registra en un archivo CSV la fecha y el número introducido por el usuario.
"""

import sys
import os
from datetime import datetime

def get_numero(prompt: str) -> int:
    """
    Solicita al usuario un número entero positivo mediante input.
    Valida que la entrada no esté vacía, que sea un número entero, 
    que no sea decimal ni negativo.

    Parámetros:
    prompt (str): Mensaje que se muestra al usuario en consola.

    Retorna:
    int: Número entero positivo ingresado por el usuario.

    Maneja:
    - Entradas vacías.
    - Valores decimales o no numéricos.
    - Valores negativos.
    - Interrupción por teclado (Ctrl+C).
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("No digitó nada, intente de nuevo. ")
                continue
            if "." in user_input:
                print("Digite un entero sin decimales ")
                continue
            numero = int(user_input)
            if numero < 0:
                print("Número negativo no válido. ")
                continue
            return numero
        except ValueError:
            print("Dato no válido. ")
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario")
            sys.exit(0)

def historial(numero: int) -> None:
    """
    Guarda en un archivo CSV la fecha y el número introducido por el usuario.

    Parámetros:
    numero (int): Número ingresado por el usuario.

    Crea o actualiza el archivo 'Historial.csv' con el formato:
    Fecha, número_introducido
    """
    fecha = datetime.now().strftime("%d/%B/%y %H:%M:%S")
    archivo = "Historial.csv"
    existe = os.path.isfile(archivo)
    with open(archivo, "a", encoding="utf-8", newline="") as f:
        if not existe or os.stat(archivo).st_size == 0:
            f.write("Fecha, número_introducido\n")
        f.write(f"{fecha}, {numero}\n")

def main():
    """
    Ejecuta la lógica principal del programa:
    - Solicita un número entero positivo al usuario.
    - Imprime una cuenta regresiva desde ese número hasta 0.
    - Guarda el número en un archivo de historial con marca de tiempo.
    """
    numero = get_numero("Digite un número entero positivo: ")
    cuenta_reversa = [str(i) for i in range(numero, -1, -1)]
    print(", ".join(cuenta_reversa))
    historial(numero)

if __name__ == "__main__":
    """
    Bucle principal del programa que permite repetir la ejecución según decisión del usuario.
    """
    while True:
        main()
        rep = input("¿Desea repetir el programa? ").strip().lower()
        if rep != "y":
            print("¡Adiós!")
            break
