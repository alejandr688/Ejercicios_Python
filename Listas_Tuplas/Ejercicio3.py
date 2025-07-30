import sys
import os
from datetime import datetime

def get_input(prompt: str) -> str:
    """Pide un número al usuario y devuelve una cadena de dos dígitos, o 'salir'."""
    while True:
        try:
            user_input = input(prompt).strip().lower()
            if user_input == "salir":
                return "salir"
            if not user_input:
                print("No digitó nada, intente de nuevo.")
                continue
            if not user_input.isdigit():
                print("Sólo se aceptan números enteros no negativos.")
                continue
            numero = int(user_input)
            if numero > 99:
                print("Solo se aceptan números del 00 al 99.")
                continue
            return f"{numero:02d}"
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario. Saliendo.")
            sys.exit(0)

def historial(lista: list) -> None:
    """Guarda la lista ganadora en un archivo con marca de tiempo."""
    fecha = datetime.now().strftime("%d/%m/%y %H:%M:%S")
    archivo = "Historial.csv"
    existe = os.path.isfile(archivo)
    try:
        with open(archivo, "a", encoding="utf-8", newline="") as f:
            if not existe or os.stat(archivo).st_size == 0:
                f.write("fecha, lista_ganadora\n")
            f.write(f"{fecha}, {lista}\n")
    except (IOError, OSError, FileNotFoundError) as e:
        print(f"No se pudo escribir en el archivo: {e}")

def lista() -> list:
    """Solicita al usuario los números ganadores y devuelve la lista ordenada."""
    lista_ganadora = []
    print("Digite los números ganadores o 'salir' para terminar:")
    while True:
        numero = get_input("→ ")
        if numero == "salir":
            break
        lista_ganadora.append(numero)
    return sorted(lista_ganadora)

def main():
    lista_ganadora = lista()
    print("Números ordenados:", ", ".join(lista_ganadora))
    historial(lista_ganadora)

if __name__ == "__main__":
    while True:
        main()
        rep = input("¿Desea repetir el programa? (y/n) ").strip().lower()
        if rep != "y":
            print("¡Adiós!")
            break
