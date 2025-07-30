"""Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo."""

import sys
import os
from datetime import datetime

def get_palabra(prompt: str) -> str:
    """
    Solicita al usuario una palabra mediante el mensaje dado por 'prompt'.
    Valida que la entrada no esté vacía, no contenga espacios ni comas.
    
    Args:
        prompt (str): Mensaje que se muestra al usuario.

    Returns:
        str: Palabra en minúsculas, sin espacios ni comas.
    """
    while True:
        try:
            user_input = input(prompt).strip().lower()
            if not user_input:
                print("No digitó nada, intente de nuevo.")
                continue
            if " " in user_input or "," in user_input:
                print("Una sola palabra por favor.")
                continue
            return user_input
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario. Saliendo")
            sys.exit(0)

def historial(palabra: str, palindromo: str) -> None:
    """
    Guarda en un archivo de texto el historial de palabras verificadas y su estatus como palíndromo.

    Args:
        palabra (str): Palabra ingresada por el usuario.
        palindromo (str): Resultado de la verificación ("es palindromo" o "no es palindromo").
    """
    fecha = datetime.now().strftime("%d/%m/%y %H:%M:%S")
    archivo = "Historial.txt"
    existe = os.path.isfile(archivo)
    try:
        with open(archivo, "a", encoding="utf-8", newline="") as f:
            if not existe or os.stat(archivo).st_size == 0:
                f.write(f"{'='*12} Historial de palíndromos {'='*12}\n{fecha}\nPalabra, ¿es palíndromo?\n")
            f.write(f"{palabra}, {palindromo}\n")
    except (OSError, IOError, FileNotFoundError) as e:
        print(f"No se pudo escribir en el archivo: {e}")

def palindromo() -> tuple[str, str]:
    """
    Verifica si la palabra ingresada por el usuario es un palíndromo.

    Returns:
        tuple[str, str]: Una tupla con la palabra y el resultado del análisis.
    """
    palabra = get_palabra("Digite una palabra por favor: ")
    inversa = palabra[::-1]
    if palabra == inversa:
        return palabra, "es palindromo"
    else:
        return palabra, "no es palindromo"

def main():
    """
    Ejecuta el flujo principal del programa:
    - Solicita una palabra.
    - Verifica si es palíndromo.
    - Muestra el resultado.
    - Guarda en historial.
    """
    palabra, estatus = palindromo()
    historial(palabra, estatus)
    print(f"La palabra {palabra} {estatus}.")

if __name__ == "__main__":
    while True:
        main()
        rep = input("¿Desea repetir el programa? (y/n) ").strip().lower()
        if rep != "y":
            print("¡Adiós!")
            break
