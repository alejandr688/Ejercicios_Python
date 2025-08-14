import sys
import os
from datetime import datetime

def get_input(prompt: str) -> str:
    """Solicita al usuario una entrada no vacía y maneja KeyboardInterrupt."""
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("No digitó nada. Intente de nuevo.")
                continue
            return user_input
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario. Saliendo.")
            sys.exit(0)

def mostrar_estado(facturas: dict, cobrado: float):
    """Muestra el estado actual de las facturas y cantidades."""
    pendiente = sum(facturas.values())
    print("\n----- ESTADO ACTUAL -----")
    print(f"Facturas pendientes: {len(facturas)}")
    if facturas:
        for num, valor in facturas.items():
            print(f"  Factura {num}: ${valor:.2f}")
    print(f"Total cobrado:      ${cobrado:.2f}")
    print(f"Total pendiente:    ${pendiente:.2f}\n")

def guardar_historial(accion: str, factura: str, valor: float, cobrado: float, pendiente: float):
    """Guarda un registro de las operaciones realizadas en un archivo CSV."""
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    archivo = "HistorialFacturas.csv"
    existe = os.path.isfile(archivo)
    linea = f"{fecha},{accion},{factura},{valor:.2f},{cobrado:.2f},{pendiente:.2f}\n"
    try:
        with open(archivo, "a", encoding="utf-8") as f:
            if not existe:
                f.write("Fecha,Accion,Factura,Valor,Cobrado,Pendiente\n")
            f.write(linea)
    except Exception as e:
        print(f"Error guardando historial: {e}")

def agregar_factura(facturas: dict) -> float:
    """Agrega una nueva factura al diccionario."""
    while True:
        numero = get_input("Número de factura nueva: ")
        if numero in facturas:
            print("Ese número de factura ya existe. Intente otro.")
            continue
        break
    while True:
        try:
            valor = float(get_input("Valor de la factura: $"))
            if valor <= 0:
                print("El valor debe ser positivo.")
                continue
            break
        except ValueError:
            print("Valor inválido. Introduzca un número.")
    facturas[numero] = valor
    print(f"Factura {numero} añadida con valor ${valor:.2f}.")
    return valor

def pagar_factura(facturas: dict) -> float:
    """Paga (elimina) una factura del diccionario."""
    numero = get_input("Número de factura a pagar: ")
    if numero not in facturas:
        print("No existe esa factura pendiente.")
        return 0.0
    valor = facturas.pop(numero)
    print(f"Factura {numero} pagada. Valor: ${valor:.2f}")
    return valor

def menu():
    print("GESTIÓN DE FACTURAS PENDIENTES")
    print("1. Añadir nueva factura")
    print("2. Pagar una factura")
    print("3. Terminar")
    return get_input("Elija una opción (1/2/3): ")

def main():
    facturas = {}
    cobrado = 0.0
    while True:
        mostrar_estado(facturas, cobrado)
        opcion = menu()
        if opcion == "1":
            valor = agregar_factura(facturas)
            guardar_historial("Añadida", list(facturas.keys())[-1], valor, cobrado, sum(facturas.values()))
        elif opcion == "2":
            valor = pagar_factura(facturas)
            if valor > 0:
                cobrado += valor
                guardar_historial("Pagada", "N/A", valor, cobrado, sum(facturas.values()))
        elif opcion == "3":
            print("Saliendo. ¡Que tenga buen día!")
            break
        else:
            print("Opción inválida.")
        # Estado siempre se muestra después de cada acción

if __name__ == "__main__":
    main()
