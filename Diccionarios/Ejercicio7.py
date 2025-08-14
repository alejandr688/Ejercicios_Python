import sys 
import os 
from datetime import datetime 
import locale 

locale.setlocale(locale.LC_ALL, "Spanish")

def get_input(prompt: str) -> str:
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("No digitó nada, intente de nuevo.")
                continue
            return user_input
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario. Saliendo.")
            sys.exit(0)

def historial(datos: dict, total: float) -> None:
    fecha = datetime.now().strftime("%d/%B/%y %I:%M:%S %p")
    archivo = "Historial.csv"
    existe = os.path.isfile(archivo)
    try:
        with open(archivo, "a", newline="", encoding="utf-8", errors="replace") as f:
            if not existe or os.stat(archivo).st_size == 0:
                f.write("Fecha,Articulo,Precio,Total\n")
            for articulo, precio in datos.items():
                f.write(f"{fecha},{articulo},{precio:.2f},{total:.2f}\n")
    except (IOError, OSError, FileNotFoundError, PermissionError) as e:
        print(f"No se pudo escribir en el archivo: {e}")

def diccionario() -> None:
    datos = {}
    print("Ingrese el nombre de los artículos y su precio (o escriba 'salir'):")

    while True:
        articulo = get_input("Artículo: ")
        if articulo.lower() == "salir":
            break

        while True:
            try:
                precio_str = get_input("Precio: ")
                precio = float(precio_str)
                if precio < 0:
                    print("Precio incorrecto.")
                    continue
                break
            except ValueError:
                print("Precio inválido")

        datos[articulo] = precio

    if datos:
        print("\n=== Lista de compras ===")
        for clave, valor in datos.items():
            print(f"{clave} --- ${valor:.2f}")
        total = round(sum(datos.values()), 2)
        print(f"Total --- ${total:.2f}")
        historial(datos, total)
    else:
        print("No se ingresó ningún artículo.")

def main():
    diccionario()

if __name__ == "__main__":
    while True:
        main()
        rep = get_input("¿Desea repetir el programa? (y/n): ").lower()
        if rep != "y":
            print("¡Adiós!")
            break
