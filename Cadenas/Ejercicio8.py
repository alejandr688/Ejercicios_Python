"""
Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales
y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
"""

import sys

def get_precio(prompt: str) -> str:
    """
    Solicita al usuario que ingrese un precio con dos decimales.

    Args:
        prompt (str): Mensaje a mostrar en consola al pedir el precio.

    Returns:
        str: Precio ingresado por el usuario como string.

    Nota:
        Si el usuario no ingresa nada o interrumpe el programa,
        se vuelve a solicitar el dato o se sale del programa.
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("No digitó nada, intente de nuevo. ")
                continue
            return user_input
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario.")
            sys.exit(0)

def main():
    """
    Función principal del programa.

    Solicita un precio en euros con dos decimales, valida el formato y muestra
    por pantalla el número de euros y céntimos. Guarda el historial en un archivo de texto.

    El programa continúa ejecutándose hasta que el usuario decida salir.
    """
    while True:
        precio = get_precio("Digite el precio del producto en euros con dos decimales por favor: ")
        
        if "." not in precio:
            print("Formato de precio no válido, intente de nuevo.")
            continue
        
        partes = precio.split(".")
        
        if len(partes) != 2 or len(partes[1]) != 2:
            print("Debe ingresar un número con dos decimales exactos.")
            continue
        
        try:
            precio_float = round(float(precio), 2)
            print(f"Precio válido: {precio_float}€")
            print(f"El precio es {partes[0]} euros con {partes[1]} céntimos.")
            
            with open("Historial.txt", "a") as f:
                f.write(f"\nPrecio: {precio_float}\nEuros: {partes[0]}\nCéntimos: {partes[1]}\n")
            
            break
        except ValueError:
            print("Precio no válido, debe escribir números.")

if __name__ == "__main__":
    """
    Punto de entrada del programa.

    Ejecuta repetidamente la función principal y pregunta al usuario si desea repetir.
    Termina si el usuario ingresa una respuesta diferente a 'y' o 'Y'.
    """
    while True:
        main()
        rep = input("¿Quiere repetir el programa? (Y/N) ").strip().lower()
        if rep != "y":
            print("¡Adiós!")
            break
