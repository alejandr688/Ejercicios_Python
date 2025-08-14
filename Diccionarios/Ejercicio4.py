"""Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma 
fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes."""

import sys
import os
from datetime import datetime 
import re
import locale
locale.setlocale(locale.LC_TIME,"Spanish")

def get_input(prompt:str)->str:
    while True:
        try:
            user_input=input(prompt).strip().lower()
            if not user_input:
                print("No digitó nada, intente de nuevo. ")
                continue
            return user_input
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario. Saliendo ")
            sys.exit(0)

def historial(fecha:str,fecha_completa:str)->None:
    date=datetime.now().strftime("%d/%B/%y %I:%M %p")
    archivo="Historial.csv"
    existe=os.path.isfile(archivo)
    try:
        with open(archivo,"a",newline="",encoding="utf-8") as f:
            if not existe or os.stat(archivo).st_size==0:
                f.write("Fecha, fecha introducida, fecha completa\n")
            f.write(f"{date}, {fecha}, {fecha_completa}\n")
    except (IOError, OSError, FileNotFoundError, PermissionError) as e:
        print(f"No se pudo escribir en el archivo: {e}")
        
def get_fecha()->str:
    patron=r'^\d{1,2}[-/]\d{1,2}[-/]\d{4}$'
    while True:
        try:
            fecha=get_input("Digite la fecha con este formato (dd/mm/yyyy o dd-mm-yyyy): ")
            if not re.fullmatch(patron, fecha):
                print("Formato de fecha no válida, intente de nuevo. ")
                continue
            separador="-" if "-" in fecha else "/"
            fecha=datetime.strptime(fecha, f"%d{separador}%m{separador}%Y")
            return fecha
        except ValueError:
            print("Fecha no válida.")
            
def main():
    fecha=get_fecha()
    fecha_str = fecha.strftime("%d/%m/%Y")
    fecha_completa = fecha.strftime("%d de %B de %Y").capitalize()
    dia=fecha.day
    mes=fecha.month
    año=fecha.year
    nombre_mes = fecha.strftime("%B")  # → 'julio'
    print(f"La fecha es: {dia} de {nombre_mes} de {año}")
    historial(fecha_str, fecha_completa)
    
if __name__=="__main__":
    while True:
        main()
        rep=input("¿Desea repetir el programa? (y/n) ").strip().lower()
        if rep!="y":
            print("¡Adios!")
            break