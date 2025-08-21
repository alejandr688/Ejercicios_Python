"""Escribir una función que reciba un número entero positivo y devuelva su factorial."""
import sys
import os
from datetime import datetime

def get_entero(prompt:str)->int:
    while True:
        try:
            user_input=input(prompt).strip()
            if not user_input:
                print("No digitó nada, intente de nuevo")
                continue
            n=int(user_input)
            if n<0:
                print("El entero no puede ser negativo ")
                continue
            return n
        except ValueError:
            print("Valor inválido ")
        except KeyboardInterrupt:
            print("Programa interrumpido por el usuario. Saliendo ")
            sys.exit(0)
            
def factorial()->tuple:
    n_factorial=1
    n=get_entero("Digite un número entero positivo por favor: ")
    for i in range(1,n+1):
        n_factorial*=i
    return n_factorial,n

def historial(n:int,factorial:int)->None:
    fecha=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    archivo="Historial.csv"
    existe=os.path.isfile(archivo)
    try:
        with open(archivo,"a",newline="",encoding="utf-8",errors="ignore",buffering=1) as f:
            if not existe or os.stat(archivo).st_size==0:
                f.write(f"Fecha, Entero, Factorial\n")
            f.write(f"{fecha},{n}, {factorial}\n")
            
    except (IOError, OSError, FileExistsError,PermissionError) as e:
        print(f"Error: {e}")
    

def main():
    numero,n=factorial()
    print(f"El factorial de {n} es {numero} :D")
    historial(n,numero)

if __name__=="__main__":
    while True:
        main()
        rep=input("¿Desea repetir el programa? (Y/N) ").strip().lower()
        if rep!="y":
            print("Adios")
            break
        