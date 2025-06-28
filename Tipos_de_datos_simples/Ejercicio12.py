"""
Este programa calcula el coste final de la compra de barras de pan que no son del día en una panadería.
Cada barra cuesta 3.49$ normalmente, pero las que no son frescas tienen un 60% de descuento.
El programa pide al usuario la cantidad de barras no frescas, calcula el precio original, el descuento y el precio final,
y muestra esta información por pantalla. También guarda el historial de operaciones en un archivo de texto.
"""

import sys

def get_cantidad(prompt: str) -> int:
    """
    Solicita al usuario un número entero positivo correspondiente a la cantidad de barras de pan no frescas.

    Args:
        prompt (str): El mensaje que se muestra al usuario para pedir la cantidad.

    Returns:
        int: La cantidad de barras ingresada por el usuario.
    
    El bucle continúa hasta recibir un valor válido. Si el usuario interrumpe el programa, se sale limpiamente.
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("No digitó nada, intente de nuevo.")
                continue
            cantidad = int(user_input)
            if cantidad < 0:
                print("El número de barras no puede ser un número negativo.")
                continue
            return cantidad
        except ValueError:
            print("Cantidad no válida, intente de nuevo.")
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario. Saliendo...")
            sys.exit(0)

def main():
    """
    Función principal del programa.

    Realiza lo siguiente:
    - Llama a get_cantidad() para solicitar la cantidad de barras de pan no frescas.
    - Calcula el precio original, el descuento y el precio final.
    - Muestra los resultados al usuario por pantalla.
    - Escribe los detalles de la operación en el archivo 'Historial.txt'.
    """
    cantidad_barras = get_cantidad("Digite el número de barras que no son del día que está llevando: ")
    precio_original = cantidad_barras * 3.49
    descuento = precio_original * 0.6
    precio_final = precio_original - descuento

    print(f"El precio habitual de una barra es de 3.49$, el descuento que tiene por comprar {cantidad_barras} que no son del día es de "
          f"{descuento:.2f}$, el coste original es de {precio_original:.2f}$ y el precio final es {precio_final:.2f}$.")

    with open("Historial.txt", "a") as f:
        f.write(f"Cantidad de barras de pan: {cantidad_barras}\n"
                f"Precio original: {precio_original:.2f}$\n"
                f"Descuento: {descuento:.2f}$\n"
                f"Precio final: {precio_final:.2f}$\n\n")

if __name__ == "__main__":
    while True:
        main()
        rep = input("¿Desea hacer otra operación? (Y/N) ").strip().lower()
        if rep != "y":
            print("¡Hasta luego!")
            break
