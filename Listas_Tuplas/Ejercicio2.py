"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el 
mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas
introducidas por el usuario."""


import sys
import os
from datetime import datetime
import unicodedata

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

def historial(datos:dict)->None:
    fecha=datetime.now().strftime("%d/%m/%y %H:%M:%S")
    archivo="Historial.csv"
    existe=os.path.isfile(archivo)
    try:
        with open(archivo,"a",encoding="utf-8", newline="") as f:
            if not existe or os.stat(archivo).st_size==0:
                f.write("fecha, materias, calificaciones\n")
            materias=", ".join(datos.keys())
            calificaciones=", ".join(str(n) for n in datos.values())
            f.write(f"{fecha}, {materias}, {calificaciones}\n")
    except (IOError,OSError,FileNotFoundError) as e:
        print(f"No se pudo escribir en el archivo: {e}")
        
def normalizar(texto:str)->str:
    texto=unicodedata.normalize("NFKD",texto) #[n,´]
    texto="".join([c for c in texto if not unicodedata.combining(c)])
    return texto
        
def diccionario()->dict:
    datos={}
    while True:
        clave=get_input("Digite la materia que cursó(o escriba 'salir' para terminar): ")
        clave=normalizar(clave)
        if clave in datos:
            print("Ya ingresó esa materia. ")
            continue
        if clave=="salir":
            break
        while True:
            try:
                valor=get_input(f"Digite la calificación para la materia {clave}: ")
                valor=int(valor)
                if valor<0 or valor>10:
                    print("Calificación no válida. ")
                    continue
                datos[clave]=valor
                break
            except ValueError:
                print("Calificación no válida. ")
    return datos

def main():
    datos=diccionario()
    historial(datos)
    for clave, valor in datos.items():
        print(f"En {clave} has sacado {valor} de califición.\n")
    
        

if __name__=="__main__":
    while True:
        main()
        rep=get_input("¿Quiere repetir el programa? (y/n) ")
        if rep!="y":
            print("¡Adios!")
            break
