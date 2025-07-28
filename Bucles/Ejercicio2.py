""" 
Programa que solicita al usuario su edad y muestra por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
Además, guarda un registro de las edades ingresadas junto con la fecha y hora en un archivo CSV llamado 'Historial.csv'.
"""

import os
import sys
from datetime import datetime

def get_edad(prompt: str) -> int:
    """
    Solicita al usuario que ingrese su edad mediante un input. 
    Valida que el dato ingresado sea un número entero positivo menor o igual a 120.
    
    Parámetros:
    prompt (str): Mensaje que se muestra al usuario.

    Retorna:
    int: Edad válida ingresada por el usuario.

    Maneja:
    - Entradas vacías.
    - Valores negativos o mayores a 120.
    - Decimales o valores no numéricos.
    - Interrupción por teclado (Ctrl+C).
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("No digitó nada, intente de nuevo. ")
                continue
            if "." in user_input:
                print("Digite una edad sin decimales por favor. ")
                continue
            edad = int(user_input)
            if edad < 0 or edad > 120:
                print("Edad incorrecta. ")
                continue
            return edad
        except ValueError:
            print("Dato no válido")
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario. Saliendo ")
            sys.exit(0)

def historial(edad: int):
    """
    Guarda la edad ingresada por el usuario junto con la fecha y hora actual en un archivo CSV.

    Parámetros:
    edad (int): Edad ingresada por el usuario.

    Crea o agrega a un archivo 'Historial.csv' con formato:
    Fecha, edad
    """
    fecha = datetime.now().strftime("%d/%m/%y %H:%M:%S")
    archivo = "Historial.csv"
    existe = os.path.isfile(archivo)
    with open(archivo, "a", encoding="utf-8", newline="") as f:
        if not existe or os.stat(archivo).st_size == 0:
            f.write("Fecha, edad\n")
        f.write(f"{fecha}, {edad}\n")

def main():
    """
    Ejecuta la lógica principal del programa:
    - Solicita la edad del usuario.
    - Guarda el dato en el historial.
    - Muestra todos los años cumplidos desde 1 hasta la edad ingresada.
    """
    edad = get_edad("Digite su edad por favor: ")
    historial(edad)
    print("Años cumplidos:")
    for i in range(edad):
        print(f"{i+1}", end=", ")

if __name__ == "__main__":
    """
    Bucle principal del programa. Permite repetir la ejecución si el usuario lo desea.
    """
    while True:
        main()
        rep = input("\n¿Desea repetir? (y/n) ").strip().lower()
        if rep != "y":
            print("¡Adiós!")
            break
