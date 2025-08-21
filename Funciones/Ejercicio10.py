"""Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal."""

import sys

def get_numero(prompt: str) -> int:
    """Pide un entero (acepta signo) y lo devuelve como int."""
    while True:
        try:
            s = input(prompt).strip()
            if not s:
                print("No escribió nada, intente de nuevo.")
                continue
            n = int(s)  # valida y convierte (acepta + / -)
            return n
        except ValueError:
            print("Entrada no válida. Escriba un entero (ej. 42 o -7).")
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario. Saliendo.")
            sys.exit(0)

def decimal_binario(numero: int) -> str:
    """Convierte un entero decimal a cadena binaria con prefijo '0b'."""
    return bin(numero)

def binario_decimal(binario: str) -> int:
    """Convierte cadena binaria (con o sin '0b') a entero decimal."""
    b = binario.strip().lower()
    if b.startswith("0b"):
        b = b[2:]
    if not b or any(ch not in "01" for ch in b):
        raise ValueError(f"'{binario}' no es un binario válido.")
    return int(b, 2)

def main():
    numero = get_numero("Digite un número entero por favor: ")
    b = decimal_binario(numero)
    d = binario_decimal(b)  # convierte de vuelta
    print(f"Decimal → binario: {numero}  ->  {b}")
    print(f"Binario → decimal: {b}  ->  {d}\n")

if __name__ == "__main__":
    while True:
        try:
            main()
            rep = input("¿Desea repetir el programa? (Y/N) ").strip().lower()
            if rep != "y":
                print("Adiós")
                break
        except ValueError as e:
            # Errores de binario_decimal, por si decides probar manualmente
            print("Error:", e)
