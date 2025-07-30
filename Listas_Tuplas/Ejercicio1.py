"""Escribir un programa que almacene las asignaturas de un curso(por ejemplo  matemáticas, física, química, historia y lenguas) en una lista y muestre por pantalla
el mensaje 'yo estudio <asignatura>, donde asignatura es cada una de las asignaturas de la lista"""

import os
import sys
from datetime import datetime 


def get_input(prompt:str)->str:
    while True:
        try:
            user_input=input(prompt).strip()
            if not user_input:
                print("No escribió nada, intente de nuevo. ")
                continue
            return user_input
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario. Saliendo")
            sys.exit(0)
            
def historial(materias:list)->None:
    fecha=datetime.now().strftime("%d/%m/%Y %I:%M:%p")
    archivo="Historial.csv"
    existe=os.path.isfile(archivo)
    try:
        with open(archivo,"a",encoding="utf-8",newline="") as f:
            if not existe or os.stat(archivo).st_size==0:
                f.write("fecha_registro, materias\n")
            f.write(f"{fecha}, {materias}\n")
    except (IOError,OSError,FileNotFoundError) as e:
        print(f"No se puedo abrir el archivo: {e}")



def asignaturas()->list:
    materias=[]
    print("Digite la materia que va a cursar o escriba 'salir' para salir del programa: ")
    while True:
        asignatura=get_input("").lower()
        if asignatura.title() in materias:
            print("Ya escribió esa asignatura. ")
            continue
        if asignatura=="salir":
            break
        materias.append(asignatura.title())
    return materias

def main():
    lista_materias=asignaturas()
    historial(lista_materias)
    print("Usted estudia:", ", ".join(lista_materias))
    
if __name__=="__main__":
    while True:
        main()
        rep=get_input("¿Desea repetir el programa? (y/n) ").lower()
        if rep!="y":
            print("¡Adios!")
            break
        