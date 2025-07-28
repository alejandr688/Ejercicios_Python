"""Programa que pide al usuario una palabra y muestra sus letras invertidas separadas por comas. 
También guarda un historial con la palabra introducida.
"""

import os
import sys
from datetime import datetime

def get_palabra(prompt: str) -> str:
    """
    Solicita al usuario una palabra no vacía y la retorna.
    Sale limpiamente si el usuario interrumpe con Ctrl+C.
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("No digitó nada, intente de nuevo.")
                continue
            if not user_input.isalpha():
                print("Solo se permiten letras.")
                continue
            return user_input
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario. Saliendo.")
            sys.exit(0)

def historial(palabra: str) -> None:
    """
    Registra la palabra ingresada con la fecha y hora en un archivo CSV.
    """
    fecha = datetime.now().strftime("%d/%b/%y %H:%M:%S")
    archivo = "Historial.csv"
    existe = os.path.isfile(archivo)
    try:
        with open(archivo, "a", encoding="utf-8", newline="") as f:
            if not existe or os.stat(archivo).st_size == 0:
                f.write("Fecha_registro,Palabra\n")
            f.write(f"{fecha}, {palabra}\n")
    except (IOError, FileNotFoundError, OSError) as e:
        print(f"No se pudo escribir en el archivo: {e}")

def muestra(palabra: str) -> None:
    """
    Muestra por pantalla las letras de la palabra en orden inverso, separadas por comas.
    """
    letras_invertidas = [letra for letra in palabra[::-1]]
    print(", ".join(letras_invertidas))

def main():
    """
    Ejecuta el flujo principal del programa: pedir palabra, mostrarla invertida y guardar historial.
    """
    palabra = get_palabra("Introduzca una palabra por favor: ")
    muestra(palabra)
    historial(palabra)

if __name__ == "__main__":
    while True:
        try:
            main()
            rep = input("¿Desea repetir el programa? (y/n): ").strip().lower()
            if rep != "y":
                print("¡Adiós!")
                break
        except KeyboardInterrupt:
            print("\nPrograma interrumpido. ¡Hasta luego!")
            break
