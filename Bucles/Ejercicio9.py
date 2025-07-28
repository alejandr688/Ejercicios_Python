"""Escribir un programa que almacene la cadena de caracteres 'contraseña' en una variable,
pregunte al usuario por la contraseña hasta que la introduzca correctamente.
"""

import sys
import os
from datetime import datetime

def get_input(prompt: str) -> str:
    """
    Solicita al usuario una cadena de texto no vacía.
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("No digitó nada, intente de nuevo.")
                continue
            return user_input
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario.")
            sys.exit(0)

def historial(acceso: bool) -> None:
    """
    Guarda en un archivo CSV si el acceso fue concedido junto con la fecha y hora.
    """
    fecha = datetime.now().strftime("%d/%B/%y %H:%M:%S")
    archivo = "Historial.csv"
    existe = os.path.isfile(archivo)
    with open(archivo, "a", encoding="utf-8", newline="") as f:
        if not existe or os.stat(archivo).st_size == 0:
            f.write("Fecha, Acceso concedido\n")
        f.write(f"{fecha}, {'Sí' if acceso else 'No'}\n")

def verificar_contraseña(correcta: str) -> None:
    """
    Pide al usuario la contraseña hasta que sea igual a la contraseña correcta.
    """
    while True:
        intento = get_input("Digite la contraseña: ")
        if intento == correcta:
            print("Acceso concedido.")
            historial(True)
            break
        else:
            print("Contraseña incorrecta. Intente de nuevo.")
            historial(False)

def main():
    """
    Función principal del programa.
    """
    contraseña_correcta = "contraseña"
    verificar_contraseña(contraseña_correcta)

if __name__ == "__main__":
    while True:
        main()
        repetir = input("¿Desea intentar de nuevo? (y/n): ").strip().lower()
        if repetir != "y":
            print("¡Adiós!")
            break
