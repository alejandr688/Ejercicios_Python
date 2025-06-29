"""
Este programa pregunta el nombre del usuario en consola y después de que el usuario lo introduzca,
muestra por pantalla "<nombre> tiene <n> letras", donde <nombre> es el nombre del usuario en mayúsculas
y <n> es el número de letras que tiene el nombre. Además, guarda la información en un archivo de historial.
"""

import sys

def get_nombre(prompt: str) -> str:
    """
    Solicita al usuario que introduzca su nombre a través de la consola.

    Args:
        prompt (str): Mensaje que se mostrará al usuario para pedir el nombre.

    Returns:
        str: El nombre introducido por el usuario (sin espacios al principio y al final).

    Maneja:
        - Si el usuario no escribe nada, vuelve a pedir el nombre.
        - Si el usuario interrumpe el programa con Ctrl+C, se sale de forma controlada.
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("Nombre vacío, escriba un nombre.")
                continue
            return user_input
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario. Saliendo.")
            sys.exit(0)
            
def main():
    """
    Función principal que:
    - Llama a get_nombre() para pedir el nombre del usuario.
    - Calcula la longitud del nombre introducido.
    - Muestra en pantalla cuántas letras tiene el nombre.
    - Guarda el resultado en un archivo llamado 'Historial.txt'.
    """
    nombre = get_nombre("Escriba su nombre por favor: ")
    n = len(nombre)
    print(f"{nombre.upper()} tiene {n} letras.")
    with open("Historial.txt", "a") as f:
        f.write(f"{nombre.upper()} tiene {n} letras.\n")

if __name__ == "__main__":
    """
    Bucle principal del programa que permite repetir la ejecución.
    Pregunta al usuario si desea volver a ejecutar el programa.
    Termina cuando el usuario responde con algo diferente a 'Y' o 'y'.
    """
    while True:
        main()
        rep = input("¿Quiere repetir el programa? (Y/N) ").strip().lower()
        if rep != "y":
            print("¡Hasta luego!")
            break
