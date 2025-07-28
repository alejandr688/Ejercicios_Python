"""Programa que genera un triángulo rectángulo de asteriscos a partir de un número introducido por el usuario,
y guarda un historial con la fecha y el valor proporcionado."""

import sys
import os
from datetime import datetime

def get_numero(prompt:str) -> int:
    """
    Solicita al usuario un número entero positivo desde la consola.
    Valida que el valor ingresado no esté vacío, no tenga decimales, no sea negativo, y que sea numérico.
    
    Args:
        prompt (str): El mensaje que se mostrará al usuario para solicitar el número.
    
    Returns:
        int: El número entero positivo ingresado por el usuario.
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("No digitó nada, intente de nuevo. ")
                continue
            if "." in user_input:
                print("Escriba un número sin punto decimal. ")
                continue
            numero = int(user_input)
            if numero < 0:
                print("Número negativo no válido")
                continue
            return numero
        except ValueError:
            print("Dato no válido. ")
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario. ")
            sys.exit(0)

def historial(numero:int) -> None:
    """
    Guarda un registro en un archivo CSV con la fecha actual y el número ingresado por el usuario.

    Args:
        numero (int): El número introducido por el usuario.
    """
    fecha = datetime.now().strftime("%d/%B/%y %H:%M:%S")
    archivo = "Historial.csv"
    existe = os.path.isfile(archivo)
    with open(archivo, "a", encoding="utf-8", newline="") as f:
        if not existe or os.stat(archivo).st_size == 0:
            f.write("Fecha, numero_introducido\n")
        f.write(f"{fecha}, {numero}\n")

def arbolito(numero:int) -> None:
    """
    Imprime un triángulo rectángulo de asteriscos con una altura igual al número recibido.

    Args:
        numero (int): La altura del triángulo a imprimir.
    """
    for i in range(numero + 1):
        print("*" * i)

def main():
    """
    Función principal que orquesta la ejecución del programa:
    pide el número, imprime el triángulo y guarda el historial.
    """
    numero = get_numero("Digite un número entero positivo: ")
    arbolito(numero)
    historial(numero)

if __name__ == "__main__":
    while True:
        main()
        rep = input("¿Desea repetir el programa? (y/n) ").strip().lower()
        if rep != "y":
            print("¡Adios!")
            break
