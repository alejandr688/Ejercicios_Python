"""
Programa que solicita al usuario el nombre de un producto, su precio unitario y el número de unidades, 
y muestra en pantalla una cadena formateada con el nombre del producto, su precio unitario (6 dígitos enteros y 2 decimales), 
el número de unidades (3 dígitos) y el coste total (8 dígitos enteros y 2 decimales). 
También guarda esta información en un archivo 'Historial.txt'.
"""

import sys

def get_user_input(prompt: str) -> str:
    """
    Solicita al usuario una entrada de texto con el mensaje especificado.
    Repite hasta que el usuario digite algo.
    Permite salir con Ctrl+C.
    
    Args:
        prompt (str): Mensaje a mostrar al usuario.

    Returns:
        str: Entrada del usuario sin espacios al inicio ni final.
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("No digitó nada, debe digitar algo. ")
                continue
            return user_input
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario")
            sys.exit(0)

def datos() -> tuple:
    """
    Solicita al usuario el nombre del producto, precio unitario y número de unidades.
    Realiza validaciones para asegurar datos correctos.

    Returns:
        tuple: (producto (str), precio (float), unidades (int))
    """
    producto = get_user_input("Digite el nombre del producto: ")
    while True:
        try:
            precio = float(get_user_input("Digite el precio unitario del producto por favor: "))
            break
        except ValueError:
            print("Precio no válido, debe digitar un precio unitario válido.")
    while True:
        try:
            unidades = int(get_user_input("Digite el número de unidades: "))
            break
        except ValueError:
            print("Número de unidades no válido, intente de nuevo.")
    return producto, precio, unidades

def main():
    """
    Función principal.
    Obtiene los datos del producto, calcula el coste total y muestra la información formateada.
    Además, guarda la información en el archivo 'Historial.txt'.
    """
    nombre, precio, unidades = datos()
    total = precio * unidades
    print(f"El nombre del producto es {nombre}, su precio unitario es {precio:09.2f}, el número de unidades es {unidades:03d} y el coste total es {total:010.2f}")
    with open("Historial.txt", "a", encoding="utf-8") as f:
        f.write(f"\nEl nombre del producto es {nombre}, su precio unitario es {precio:09.2f}, el número de unidades es {unidades:03d} y el coste total es {total:010.2f}\n")

if __name__ == "__main__":
    """
    Bucle principal para repetir el programa según lo desee el usuario.
    """
    while True:
        main()
        rep = input("¿Desea repetir el programa? (Y/N) ").strip().lower()
        if rep != "y":
            print("¡Adiós!")
            break
