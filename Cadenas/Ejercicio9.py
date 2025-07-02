"""Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestre por pantalla el día, mes y el año. Adaptar el programa
para que también funcione cuando el día o el mes se introduzcan con un sólo carácter."""

import re
from datetime import datetime
import sys

def get_fecha(prompt: str) -> str:
    """
    Solicita al usuario que ingrese una fecha mediante un mensaje proporcionado.

    Args:
        prompt (str): El mensaje que se muestra al usuario para pedir la fecha.

    Returns:
        str: La cadena ingresada por el usuario, que representa la fecha.

    Maneja interrupciones por teclado (Ctrl+C) finalizando el programa de forma segura.
    """
    while True:
        try:
            fecha = input(prompt).strip()
            if not fecha:
                print("No digitó nada, intente de nuevo. ")
                continue
            return fecha
        except KeyboardInterrupt:
            print("Programa interrumpido por el usuario")
            sys.exit(0)

def vericar_formato(fecha: str) -> bool:
    """
    Verifica si la fecha proporcionada cumple con el formato dd/mm/aaaa,
    permitiendo uno o dos dígitos para el día y el mes.

    Args:
        fecha (str): La fecha a verificar.

    Returns:
        bool: True si el formato es correcto, False en caso contrario.
    """
    patron = r'^\d{1,2}/\d{1,2}/\d{4}$'
    resultado = re.match(patron, fecha)
    return bool(resultado)

def fecha_valida(fecha: str) -> bool:
    """
    Comprueba que la fecha proporcionada sea válida y exista en el calendario.

    Args:
        fecha (str): La fecha a comprobar.

    Returns:
        bool: True si la fecha es válida, False si no existe o tiene formato incorrecto.
    """
    if not vericar_formato(fecha):
        return False
    try:
        datetime.strptime(fecha, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def main():
    """
    Función principal del programa.

    Solicita al usuario la fecha de nacimiento, valida su formato y existencia,
    y muestra el día, mes y año por separado. Además, guarda esta información en un archivo
    'Historial.txt'. Permite repetir el proceso si el usuario lo desea.
    """
    while True:
        fecha = get_fecha("Digite la fecha en ese formato dd/mm/aaaa: ")
        if not fecha_valida(fecha):
            print("Fecha no válida o formato incorrecto. Intente de nuevo. ")
            continue
        fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
        print(f"Dia: {fecha_dt.day}")
        print(f"Mes: {fecha_dt.month}")
        print(f"Año: {fecha_dt.year}")
        with open("Historial.txt", "a") as f:
            f.write(f"\nFecha original: {fecha}\nDia: {fecha_dt.day}\nMes: {fecha_dt.month}\nAño: {fecha_dt.year}\n")
        break

if __name__ == "__main__":
    while True:
        main()
        rep = input("¿Desea repetir el programa?(Y/N) ").strip().lower()
        if rep != "y":
            print("¡Adiós!")
            break
