"""Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura.
Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%."""

import os 
import sys 
from datetime import datetime 

def get_input(prompt: str) -> str:
    """
    Solicita al usuario una entrada de texto mostrando un mensaje personalizado.
    
    Args:
        prompt (str): Mensaje que se muestra al usuario.
    
    Returns:
        str: Entrada no vacía proporcionada por el usuario.
    
    Si el usuario presiona Ctrl+C, el programa finaliza.
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("No digitó nada, intente de nuevo. ")
                continue
            return user_input
        except KeyboardInterrupt:
            print("Programa interrumpido por el usuario")
            sys.exit(0)

def get_IVA() -> float:
    """
    Solicita al usuario el porcentaje de IVA a aplicar.
    
    Returns:
        float: Porcentaje de IVA proporcionado por el usuario. Si el usuario no escribe nada, se aplica 21%.
    
    Si el usuario ingresa el valor con '%' al final, se elimina el símbolo antes de convertirlo a float.
    Si el usuario presiona Ctrl+C, el programa finaliza.
    """
    while True:
        try:
            IVA = input("Digite el porcentaje de IVA a aplicar (ej. 56% o 56): ").strip()
            if not IVA:
                return 21.0
            if IVA.endswith("%"):
                IVA = IVA[:-1]
            IVA = float(IVA)
            if IVA < 0:
                print("El IVA no puede ser negativo, intente de nuevo. ")
                continue
            return IVA
        except KeyboardInterrupt:
            print("Programa interrumpido por el usario. Saliendo ")
            sys.exit(0)
        except ValueError:
            print("Valor no válido")

def cantidad() -> float:
    """
    Solicita al usuario la cantidad base (sin IVA) y la convierte a float.
    
    Returns:
        float: Cantidad base positiva ingresada por el usuario.
    
    Permite ingresar decimales con coma o punto. Si el usuario ingresa un valor negativo o no numérico, se solicita de nuevo.
    """
    while True:
        try:
            valor = get_input("Digite la cantidad a pagar sin IVA: ").replace(",", ".")
            cantidad = float(valor)
            if cantidad < 0:
                print("Cantidad no válida ")
                continue
            return cantidad
        except ValueError:
            print("Cantidad inválida")

def historial(inicial: float, iva: float, final: float) -> None:
    """
    Guarda el historial de facturas en un archivo CSV.
    
    Args:
        inicial (float): Cantidad sin IVA.
        iva (float): Porcentaje de IVA aplicado.
        final (float): Cantidad final con IVA incluido.
    
    El archivo se llama 'historial.csv' y se agrega una línea por cada operación realizada.
    Si el archivo no existe o está vacío, se agrega la cabecera.
    """
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    archivo = "historial.csv"
    existe = os.path.isfile(archivo)
    try:
        with open(archivo, "a", newline="", encoding="utf-8", errors="replace") as f:
            if not existe or os.stat(archivo).st_size == 0:
                f.write(f"Fecha,Precio_sin_IVA,IVA,Precio_con_IVA\n")
            f.write(f"{fecha},{inicial},{iva},{final}\n")
    except (IOError, OSError, FileNotFoundError, PermissionError) as e:
        print(f"Error: {e}")

def factura() -> tuple:
    """
    Calcula el total de la factura aplicando el IVA.
    
    Returns:
        tuple: (precio sin IVA, porcentaje de IVA, precio con IVA)
    
    Solicita la cantidad base y el porcentaje de IVA al usuario,
    calcula el total, guarda el historial y retorna los valores.
    """
    precio = cantidad()
    iva = get_IVA()
    total = precio * (1 + iva / 100)
    historial(precio, iva, total)
    return precio, iva, total

def main():
    """
    Ejecuta el flujo principal del programa:
    - Calcula una factura
    - Muestra el desglose en pantalla
    """
    sin_iva, iva, con_iva = factura()
    print(f"Cantidad inicial: {sin_iva:.2f}\nIVA aplicado: {iva:.2f}%\nPrecio con IVA: {con_iva:.2f}")

if __name__ == "__main__":
    while True:
        main()
        rep = get_input("¿Desea repetir el programa? (Y/N) ").lower()
        if rep != "y":
            print("Adios!")
            break
