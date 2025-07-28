""" 
Este programa solicita al usuario un número entero y determina si es un número primo o no. 
Además, guarda el historial de los resultados en un archivo CSV con marca de tiempo.
"""

import os
import sys
from datetime import datetime 

def get_numero(prompt: str) -> int:
    """
    Solicita al usuario un número entero mediante un mensaje personalizado.
    
    Parámetros:
        prompt (str): El mensaje que se muestra al usuario.

    Retorna:
        int: El número entero ingresado por el usuario.

    Maneja:
        - Entradas vacías.
        - Valores no enteros.
        - Interrupciones con Ctrl+C (KeyboardInterrupt).
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("No digitó nada, intente de nuevo.")
                continue
            return int(user_input)
        except ValueError:
            print("Número no válido.")
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario. Saliendo.")
            sys.exit(0)

def historial(numero: int, primo: str) -> None:
    """
    Guarda el número evaluado y si es primo o no en un archivo CSV con marca de tiempo.

    Parámetros:
        numero (int): El número evaluado.
        primo (str): Resultado de la evaluación ("es primo" o "no es primo").

    Crea o actualiza el archivo 'Historial.csv'. Maneja errores de escritura.
    """
    fecha = datetime.now().strftime("%d/%B/%y %H:%M:%S")
    archivo = "Historial.csv"
    existe = os.path.isfile(archivo)
    try:
        with open(archivo, "a", encoding="utf-8", newline="") as f:
            if not existe or os.stat(archivo).st_size == 0:
                f.write("fecha_registro, numero, ¿es primo?\n")
            f.write(f"{fecha}, {numero}, {primo}\n")
    except (IOError, FileNotFoundError, OSError) as e:
        print(f"No se pudo escribir en el archivo: {e}")

def eval_primo(numero: int) -> str:
    """
    Evalúa si un número entero es primo.

    Parámetros:
        numero (int): Número a evaluar.

    Retorna:
        str: "es primo" si el número tiene exactamente dos divisores, "no es primo" en caso contrario.
    """
    contador = 0
    for i in range(numero, 0, -1):
        if numero % i == 0:
            contador += 1
    return "es primo" if contador == 2 else "no es primo"

def main():
    """
    Función principal del programa.
    Obtiene un número del usuario, evalúa si es primo, lo muestra y guarda el resultado en el historial.
    """
    numero = get_numero("Digite un número entero por favor: ")
    es_primo = eval_primo(numero)
    print(f"El número {numero} {es_primo}")
    historial(numero, es_primo)

if __name__ == "__main__":
    """
    Bucle principal que permite al usuario repetir el programa si lo desea.
    Finaliza si el usuario ingresa algo distinto de 'y'.
    """
    while True:
        main()
        rep = input("¿Desea repetir el programa? (y/n) ").strip().lower()
        if rep != "y":
            print("¡Adiós!")
            break
