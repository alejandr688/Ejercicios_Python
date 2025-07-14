"""
Programa que solicita al usuario ingresar los productos de una cesta de compra separados por comas o espacios,
y muestra cada producto en una línea distinta numerada. Además, guarda un historial de los productos ingresados
en un archivo llamado 'Historial.txt'.
"""

import sys
import re

def get_productos(prompt: str) -> str:
    """
    Solicita al usuario que ingrese una cadena de texto mediante la consola.

    Parámetros:
    prompt (str): El mensaje que se mostrará al usuario.

    Retorna:
    str: La cadena ingresada por el usuario, sin espacios iniciales ni finales.

    Manejo de errores:
    - Si el usuario no escribe nada, se le volverá a pedir la entrada.
    - Si se presiona Ctrl+C, se termina el programa de forma controlada.
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

def main():
    """
    Función principal del programa.
    Solicita al usuario los productos comprados, los separa y limpia,
    los muestra uno por uno numerados, y guarda el resultado en un archivo de historial.
    """
    productos = get_productos("Digite el nombre de todos los productos que compró separados por comas o espacios: ")
    lista = [p.strip() for p in re.split(r"[,\s]+", productos) if p.strip()]
    
    print("\nLos productos son:")
    
    with open("Historial.txt", "a", encoding="utf-8") as f:
        f.write("\nProductos:")
        
    for x, elemento in enumerate(lista, start=1):
        print(f"{x}.- {elemento}")
        with open("Historial.txt", "a", encoding="utf-8") as f:
            f.write(f"\n {elemento.strip()}")

if __name__ == "__main__":
    """
    Bucle principal del programa.
    Ejecuta la función main() repetidamente hasta que el usuario decida salir.
    """
    while True:
        main()
        rep = input("¿Desea repetir el programa? (Y/N) ").strip().lower()
        if rep != "y":
            print("¡Adiós!")
            break
