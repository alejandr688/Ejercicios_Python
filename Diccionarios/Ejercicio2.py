"""Programa que solicita al usuario su nombre, edad, dirección y teléfono, los guarda en un diccionario,
los registra en un archivo CSV y muestra un mensaje con dicha información formateada."""

import sys
import os 
import unicodedata
from datetime import datetime

def get_input(prompt: str) -> str:
    """
    Solicita al usuario una entrada de texto, la limpia y la devuelve en minúsculas.
    
    Args:
        prompt (str): El mensaje que se muestra al usuario.
    
    Returns:
        str: Entrada del usuario normalizada.
    """
    while True:
        try:
            user_input = input(prompt).strip().lower()
            if not user_input:
                print("No digitaste nada, intenta de nuevo.")
                continue
            return user_input
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario. Saliendo.")
            sys.exit(0)

def historial(nombre: str, edad: int, direccion: str, telefono: str) -> None:
    """
    Guarda los datos del usuario en un archivo CSV con marca de tiempo.
    
    Args:
        nombre (str): Nombre del usuario.
        edad (int): Edad del usuario.
        direccion (str): Dirección del usuario.
        telefono (str): Teléfono del usuario.
    """
    fecha = datetime.now().strftime("%d/%m/%y %H:%M:%S")
    archivo = "Historial.csv"
    existe = os.path.isfile(archivo)
    try:
        with open(archivo, "a", newline="", encoding="utf-8") as f:
            if not existe or os.stat(archivo).st_size == 0:
                f.write("Fecha,Nombre,Edad,Direccion,Telefono\n")
            f.write(f"{fecha},{nombre},{edad},{direccion},{telefono}\n")
    except (IOError, OSError, FileNotFoundError, PermissionError) as e:
        print(f"No se pudo escribir en el archivo: {e}")

def get_diccionario() -> dict:
    """
    Solicita los datos del usuario, valida cada uno y los guarda en un diccionario.
    
    Returns:
        dict: Diccionario con los datos del usuario.
    """
    diccionario = {}
    nombre = get_input("Digite su nombre por favor: ")
    diccionario["Nombre"] = nombre

    while True:
        try:
            edad = int(get_input("Digite su edad por favor: "))
            if edad < 0 or edad > 120:
                print("Edad fuera de rango válido.")
                continue
            diccionario["Edad"] = edad
            break
        except ValueError:
            print("Edad no válida.")

    direccion = get_input("Digite su dirección por favor: ")
    diccionario["Dirección"] = direccion

    while True:
        telefono = get_input("Digite su teléfono por favor (10 dígitos): ")
        if len(telefono) != 10 or not telefono.isdigit():
            print("Teléfono no válido.")
            continue
        diccionario["Teléfono"] = telefono
        break

    historial(nombre, edad, direccion, telefono)
    return diccionario

def main():
    """
    Función principal que coordina la obtención de datos, muestra el mensaje final
    y permite repetir el programa si el usuario lo desea.
    """
    datos = get_diccionario()
    print(f"{datos['Nombre'].capitalize()} tiene {datos['Edad']} años, vive en {datos['Dirección'].capitalize()} y su número de teléfono es {datos['Teléfono']}.")

if __name__ == "__main__":
    while True:
        main()
        rep = input("¿Quiere repetir el programa? (y/n): ").strip().lower()
        if rep != "y":
            print("¡Adiós!")
            break
 