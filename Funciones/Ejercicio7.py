"""Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados."""

import os 
import sys 
from datetime import datetime 

def get_input(prompt:str)->str:
    while True:
        try:
            user_input=input(prompt).strip().lower()
            if not user_input:
                print("No digitó nada, intente de nuevo. ")
                continue 
            return user_input
        except KeyboardInterrupt:
            print("Programa interrumpido por el usuario. Saliendo")
            sys.exit(0)
            
def get_lista()->list[float]:
    lista=[]
    while True:
        try:
            entrada=get_input("Agrega un elemento o 'q' para salir: ")
            if entrada=="q":
                return lista 
            elemento=float(entrada)
            lista.append(elemento)
        except ValueError:
            print("El elemento debe ser un número. ")
            
def historial(lista:list,cuadrados:list)->None:
    fecha=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    archivo="Historial.csv"
    existe=os.path.isfile(archivo)
    try:
        with open(archivo,"a",newline="",encoding="utf-8",errors="replace") as f:
            if not existe or os.stat(archivo).st_size==0:
                f.write("Fecha, Lista, Lista_cuadrada\n")
            f.write(f"{fecha}, {";".join(map(str,lista))}, {",".join(map(str,cuadrados))}\n")
    except (KeyboardInterrupt, IOError, OSError, PermissionError) as e:
        print(f"Error: {e}")
        
def main():
    lista=get_lista()
    cuadrados=list(map(lambda x:x**2,lista))
    historial(lista,cuadrados)
    print(f"Lista original: {lista}\nLista de cuadrados: {cuadrados}")
    
    
if __name__=="__main__":
    while True:
        main()
        rep=get_input("¿Quiere repetir el programa? (Y/N) ")
        if rep!="y":
            break