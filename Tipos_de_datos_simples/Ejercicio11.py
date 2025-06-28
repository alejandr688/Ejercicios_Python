"""Programa para calcular el crecimiento de una cuenta de ahorros.

Imagina que acabas de abrir una cuenta de ahorros que te ofrece el 4% de interés al año.
Estos ahorros, debido a intereses que no se cobran hasta finales de año, se añaden al
balance final de tu cuenta. Este programa lee la cantidad depositada inicialmente y calcula
la cantidad de ahorros tras el primer, segundo y tercer año, mostrando los resultados
redondeados a dos decimales.
"""

import sys

def get_cantidad_inicial(prompt: str) -> float:
    """
    Solicita al usuario una cantidad inicial de ahorros, valida la entrada
    para asegurar que sea un número positivo, y devuelve el valor como float.

    Args:
        prompt (str): El mensaje que se mostrará al usuario para solicitar la entrada.

    Returns:
        float: La cantidad inicial válida ingresada por el usuario.
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("No digitó nada, intente de nuevo.")
                continue
            cantidad = float(user_input)
            if cantidad <= 0:
                print("Cantidad no válida. Intente con un número mayor a cero.")
                continue
            return cantidad
        except ValueError:
            print("Valor no válido. Por favor, ingrese un número.")
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario. Saliendo...")
            sys.exit(0)
            
def main():
    """
    Calcula y muestra la cantidad de ahorros después del primer, segundo y tercer año
    considerando un interés compuesto anual del 4%. Los resultados se muestran por
    pantalla y se registran en un archivo 'Historial.txt'.
    """
    cantidad = get_cantidad_inicial("Digite la cantidad inicial de ahorros: ")
    tasa = 0.04  # 4% de interés anual
    primer_ano = cantidad * (1 + tasa) ** 1
    segundo_ano = cantidad * (1 + tasa) ** 2
    tercer_ano = cantidad * (1 + tasa) ** 3
    print(f"Cantidad de ahorros tras el primer año: {primer_ano:.2f}")
    print(f"Cantidad de ahorros tras el segundo año: {segundo_ano:.2f}")
    print(f"Cantidad de ahorros tras el tercer año: {tercer_ano:.2f}")
    with open("Historial.txt", "a") as f:
        f.write(
            f"Cantidad inicial: {cantidad:.2f}\n"
            f"Primer año: {primer_ano:.2f}\n"
            f"Segundo año: {segundo_ano:.2f}\n"
            f"Tercer año: {tercer_ano:.2f}\n\n"
        )

if __name__ == "__main__":
    """
    Bucle principal que permite al usuario realizar múltiples cálculos consecutivos.
    Finaliza cuando el usuario indica que no desea continuar.
    """
    while True:
        main()
        rep = input("¿Quiere hacer otro cálculo? (Y/N) ").strip().lower()
        if rep != "y":
            print("¡Hasta luego!")
            break
