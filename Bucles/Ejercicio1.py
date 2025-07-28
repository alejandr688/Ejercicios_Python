"""
Programa que solicita una palabra al usuario, la imprime 10 veces numerada y guarda un historial con fecha.
"""

import sys
from datetime import datetime
import os

def get_palabra(prompt: str) -> str:
    """
    Solicita al usuario una palabra. Si no escribe nada, vuelve a pedirla.
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("No digitó nada, intente de nuevo.")
                continue
            return user_input
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario. Saliendo...")
            sys.exit(0)

def historial(palabra: str):
    """
    Guarda la palabra ingresada junto con la fecha y hora en un archivo CSV llamado Historial.csv
    """
    fecha = datetime.now().strftime("%d/%m/%y %H:%M:%S")
    archivo = "Historial.csv"
    existe = os.path.isfile(archivo)
    
    with open(archivo, mode="a", encoding="utf-8", newline="") as f:
        if not existe or os.stat(archivo).st_size == 0:
            f.write("Fecha,Palabra\n")
        f.write(f"{fecha},{palabra}\n")

def main():
    """
    Función principal que pide la palabra, la imprime 10 veces y guarda el historial.
    """
    palabra = get_palabra("Digite una palabra por favor: ")
    for i in range(10):
        print(f"{i + 1} - {palabra}")
    historial(palabra)

if __name__ == "__main__":
    while True:
        main()
        rep = input("\n¿Quiere repetir el programa? (y/n): ").strip().lower()
        if rep != "y":
            print("¡Adiós!")
            break
        print()  # Línea en blanco entre ejecuciones
