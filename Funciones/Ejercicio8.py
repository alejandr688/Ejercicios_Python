"""Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, varianza y desviación típica."""
import os 
import sys 
from datetime import datetime 
import statistics as stats

def get_input(prompt:str)->str:
    while True:
        try:
            user_input=input(prompt).strip()
            if not user_input:
                print("No digitó nada, intente de nuevo. ")
                continue
            return user_input
        except KeyboardInterrupt:
            print("Programa interrumpido por el usuario. Saliendo ")
            sys.exit(0)
            
def get_lista()->list[float]:
    lista=[]
    while True:
        try:
            entrada=get_input("Agrega un elemento o 'q' para salir: ").lower()
            if entrada=="q":
                return lista
            elemento=float(entrada)
            lista.append(elemento)
        except ValueError:
            print("Valor no válido ")

def diccionario(lista:list)->dict:
    media=stats.mean(lista)
    varianza=stats.pvariance(lista)
    desviacion=stats.pstdev(lista)
    dicc={"media":round(media,2),"varianza":round(varianza,2),"Desviacion":round(desviacion,2)}
    return dicc 

def historial(lista:list,datos:dict)->None:
    fecha=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    archivo="Historial.csv"
    existe=os.path.isfile(archivo)
    try:
        with open(archivo,"a",newline="",encoding="utf-8",errors="replace") as f:
            if not existe or os.stat(archivo).st_size==0:
                f.write("Fecha, lista, media, varianza, desviacion estandar\n")
            f.write(f"{fecha}, {";".join(map(str,lista))},{datos.get("media","")}, {datos.get("varianza","")},{datos.get("desviacion","")}\n")
    except (IOError, OSError, FileNotFoundError,PermissionError) as e:
        print(f"Error: {e}")

def main():
    lista = get_lista()
    diccion = diccionario(lista)
    historial(lista, diccion)
    print(
        f"Lista original: {lista}\n"
        f"Media: {diccion.get('media',''):.2f}\n"
        f"Varianza: {diccion.get('varianza',''):.2f}\n"
        f"Desviación: {diccion.get('Desviacion',''):.2f}"
    )

    

if __name__=="__main__":
    while True:
        main()
        rep=get_input("¿Desea repetir el programa? (Y/N) ").lower()
        if rep!="y":
            break