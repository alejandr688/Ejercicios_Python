"""
Este programa calcula el peso total de un paquete con payasos y muñecas vendidos por una juguetería. Cada payaso pesa 112 g y cada muñeca 75 g.
El usuario introduce el número de payasos y muñecas en el pedido, y el programa muestra el peso total en kilogramos, además de guardar un registro
del pedido en un archivo 'Historial.txt'. El programa permite realizar múltiples cálculos hasta que el usuario decida salir.
"""

import sys

def get_cantidad(prompt: str) -> float:
    """
    Solicita al usuario un número entero no negativo mediante el mensaje especificado en 'prompt'.
    
    Args:
        prompt (str): Mensaje que se mostrará para solicitar la entrada.
    
    Returns:
        int: La cantidad ingresada por el usuario, validada como número entero no negativo.
    
    Excepciones:
        ValueError: Si el usuario introduce un valor que no es un número entero.
        KeyboardInterrupt: Si el usuario interrumpe el programa con Ctrl+C.
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("No digitó nada, intente de nuevo. ")
                continue
            cantidad = int(user_input)
            if cantidad < 0:
                print("El número no puede ser negativo, intente de nuevo. ")
                continue
            return cantidad
        except ValueError:
            print("Cantidad no válida. ")
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario")
            sys.exit(0)

def main():
    numero_payasos = get_cantidad("Digite el número de payasos: ")
    numero_muñecas = get_cantidad("Digite el número de muñecas: ")
    pesototal = (numero_muñecas * 75 + numero_payasos * 112) / 1000
    print(f"Con {numero_payasos} payasos y {numero_muñecas} muñecas, el peso del paquete será de {pesototal:.2f} kg")
    with open("Historial.txt", "a") as f:
        f.write(f"#Payasos: {numero_payasos}, #Muñecas: {numero_muñecas}, peso total: {pesototal:.2f} kg\n")

if __name__ == "__main__":
    while True:
        main()
        rep = input("¿Desea hacer otro cálculo? (Y/N) ").strip().lower()
        if rep != "y":
            print("¡Hasta luego! ")
            break
