"""Escribir una función que reciba una muestra de números en una lista y devuelva su media."""

import os 
import sys 
from datetime import datetime

def get_input(prompt:str)->str:
    while True:
        try:
            user_input=input(prompt).strip().lower()
            if not user_input:
                print("No digitó nada, intente de nuevo ")
                continue
            return user_input
        except KeyboardInterrupt:
            print("Programa interrumpido por el usuario. Saliendo")
            
def get_lista()->list:
    lista=[]
    while True:
        try:
            entrada=get_input("Agrega un elemento a la lista o escriba 'q' para salir: ")
            if entrada=="q":
                return lista
            elemento=float(entrada)
            lista.append(elemento)
        except ValueError:
            print("Valor no válido, intente de nuevo. ")

def get_media(lista:list)->float:
    try:
        media=sum(lista)/len(lista)
        return media
    except ZeroDivisionError:
        print("Error, lista vacía ")


def historial(lista:list, media:float)->None:
    fecha=datetime.now().strftime("%Y-%m-%d %H:%M:%S ")
    archivo="Historial.csv"
    existe=os.path.isfile(archivo)
    try:
        with open(archivo,"a",newline="",encoding="utf-8",errors="replace") as f:
            if not existe or os.stat(archivo).st_size==0:
                f.write("Fecha, Lista, Media \n")
            f.write(f"{fecha}, {lista}, {media}\n")
    except (IOError, OSError, PermissionError, FileExistsError) as e:
        print(f"Error: {e}")

def main():
    lista=get_lista()
    media=get_media(lista)
    print(f"La media de la lista {lista} es {media:.2f}")
    historial(lista,media)


if __name__=="__main__":
    while True:
        main()
        rep=get_input("¿Desea repetir el programa? (Y/N) ")
        if rep!="y":
            break