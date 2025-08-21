"""Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función."""

import os 
import sys 
from datetime import datetime 
import math

def get_input(prompt:str)->str:
    while True:
        try:
            user_input=input(prompt).strip()
            if not user_input:
                print("No digitó nada,intente de nuevo. ")
                continue
            return user_input
        except KeyboardInterrupt:
            print("Programa interrumpido por el usuario ")
            sys.exit(0)
            
def get_area()->tuple:
    while True:
        try:
            entrada=get_input("Digite el radio en cm por favor: ")
            radio=float(entrada)
            if radio<0:
                print("No puedes tener un radio negativo. ")
                continue
            return (radio, math.pi*radio**2)
        except ValueError:
            print("Valor no válido")
            
def get_volumen(area:float)->float:
    while True:
        try:
            entrada=get_input("Digite al altura del cilindo: ")
            altura=float(entrada)
            if altura<0:
                print("No puedes tener una altura negativa ")
                continue
            return area*altura
        except ValueError:
            print("Valor inválido")
            
def historial(radio:float,area:float,volumen:float)->None:
    fecha=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    archivo="Historial.csv"
    existe=os.path.isfile(archivo)
    try:
        with open(archivo,"a",encoding="utf-8",newline="",errors="replace") as f:
            if not archivo or os.stat(archivo).st_size==0:
                f.write("Fecha, Radio, Area, Volumen\n")
            f.write(f"{fecha}, {radio:.2f}, {area:.2f}, {volumen:.2f}\n")
    except (IOError, OSError, FileNotFoundError, PermissionError) as e:
        print(f"Error: {e}")

            
def main():
    radio,area=get_area()
    volumen=get_volumen(area)
    print(f"El cilindo con radio {radio:.2f} cm tiene {area:.2f} cm^2 de area de la base y volumen {volumen:.2f} cm^3 ")
    historial(radio,area,volumen)
    
if __name__=="__main__":
    while True:
        main()
        rep=get_input("¿Quiere repetir el programa? (Y/N) ").lower()
        if rep!="y":
            print("Adios!")
            break
        
        