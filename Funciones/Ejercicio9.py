"""Escribir una función que calcule el máximo común divisor de dos números
y otra que calcule el mínimo común múltiplo.
"""

import os
import sys
from datetime import datetime
from typing import Tuple

def get_numero(prompt: str) -> int:
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("No digitó nada, intente de nuevo.")
                continue
            # Forzamos entero; si el usuario pone 5.0 lo aceptamos como 5
            numero = int(float(user_input))
            return numero
        except ValueError:
            print("Valor no válido. Ingrese un número entero.")
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario. Saliendo.")
            sys.exit(0)

def get_lista() -> Tuple[int, int]:
    a = get_numero("Digite el primer número: ")
    b = get_numero("Digite un segundo número: ")
    return a, b

def mcd(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    # Convención: si alguno es 0, el mcm es 0
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // mcd(a, b)

def historial(a: int, b: int, gcd_val: int, lcm_val: int) -> None:
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    archivo = "Historial.csv"
    existe = os.path.isfile(archivo)
    try:
        with open(archivo, "a", newline="", encoding="utf-8", errors="replace") as f:
            if not existe or os.stat(archivo).st_size == 0:
                f.write("Fecha,numero1,numero2,gcd,lcm\n")
            f.write(f"{fecha},{a},{b},{gcd_val},{lcm_val}\n")
    except (IOError, OSError, PermissionError, FileNotFoundError) as e:
        print(f"Error al escribir historial: {e}")

def main():
    a, b = get_lista()
    gcd_ = mcd(a, b)
    lcm_ = lcm(a, b)
    print(
        f"Los dos números fueron: {a} y {b}\n"
        f"El máximo común divisor es: {gcd_}\n"
        f"El mínimo común múltiplo es: {lcm_}\n"
    )
    historial(a, b, gcd_, lcm_)

if __name__ == "__main__":
    while True:
        main()
        rep = input("¿Desea repetir el programa? (Y/N) ").strip().lower()
        if rep != "y":
            print("¡Adiós!")
            break
