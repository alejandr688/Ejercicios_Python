"""
Programa que pregunta el nombre del usuario y un número entero,
luego imprime el nombre tantas veces como el número introducido,
cada vez en una línea distinta. Al final guarda el historial en un archivo.
"""

import sys

def get_nombre(prompt: str) -> str:
    """
    Solicita al usuario que ingrese su nombre a través de un prompt.
    
    Args:
        prompt (str): El mensaje que se mostrará al usuario en consola.
    
    Returns:
        str: El nombre introducido por el usuario, sin espacios al inicio o al final.
    
    Maneja errores:
        - Si el usuario no introduce nada, vuelve a solicitar el dato.
        - Si el usuario interrumpe el programa con Ctrl+C, sale de manera segura.
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("No digitó nada, intente de nuevo ")
                continue
            return user_input
        except ValueError:
            print("Nombre no válido. ")
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario. Saliendo")
            sys.exit(0)

def get_number(prompt: str) -> int:
    """
    Solicita al usuario que ingrese un número entero positivo a través de un prompt.
    
    Args:
        prompt (str): El mensaje que se mostrará al usuario en consola.
    
    Returns:
        int: El número entero introducido por el usuario.
    
    Maneja errores:
        - Si el usuario no introduce nada o introduce un valor no válido, vuelve a solicitar el dato.
        - Si el número es cero o negativo, lo rechaza y solicita un nuevo número.
        - Si el usuario interrumpe el programa con Ctrl+C, sale de manera segura.
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("No digitó ningún número, intente de nuevo. ")
                continue
            numero = int(user_input)
            if numero <= 0:
                print("El número no puede ser negativo ni cero ")
                continue
            return numero
        except ValueError:
            print("Valor no válido ")
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario. Saliendo ")
            sys.exit(0)

def main():
    """
    Función principal del programa.
    
    Solicita al usuario su nombre y un número entero, imprime el nombre
    tantas veces como el número ingresado, y guarda los datos en un archivo
    'Historial.txt' para registrar el historial de ejecuciones.
    
    Al finalizar, pregunta al usuario si desea repetir el programa.
    """
    nombre = get_nombre("Digite su nombre por favor: ")
    numero = get_number("Digite un número entero por favor: ")
    for i in range(numero):
        print(f"{i + 1}. {nombre}")
    with open("Historial.txt", "a") as f:
        f.write(f"\nNombre: {nombre}\nNúmero: {numero}\n\n")

if __name__ == "__main__":
    while True:
        main()
        rep = input("¿Quiere repetir el programa? (Y/N) ").strip().lower()
        if rep != "y":
            print("¡Hasta luego!")
            break
