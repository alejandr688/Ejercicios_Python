"""Escribir un programa en el que se pregunte al usuario por una frase y por una letra, y muestre por pantalla el número de veces que aparece la letra en la
frase"""

import sys
import os
from datetime import datetime

def get_string(prompt:str)->str:
    while True:
        try:
            user_input=input(prompt).strip()
            if not user_input:
                print("No digitó nada, intente de nuevo. ")
                continue
            return user_input
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario. ")
            
def historial(frase:str,letra:str,cantidad:int)->None:
    fecha=datetime.now().strftime("%d/%B/%y %H:%M:%S")
    archivo="Historial.csv"
    existe=os.path.isfile(archivo)
    try:
        with open(archivo,"a",encoding="utf-8", newline="") as f:
            if not existe or os.stat(archivo).st_size==0:
                f.write("Fecha_registro, frase, letra, coincidencias\n")
            f.write(f"{fecha}, {frase}, {letra}, {cantidad}\n")
    except (IOError,FileNotFoundError,OSError) as e:
        print(f"No se puedo escribir el archivo: {e}")

def coincidencias(palabra:str,letra:str)->int: #manzana
    contador=0
    for i in palabra:
        if letra==i:
            contador+=1
    return contador

def main():
    frase=get_string("Digite una frase por favor: ")
    letra=get_string("Digite una letra: ")
    cantidad_coincidencias=coincidencias(frase,letra)
    print(f"El número de veces que aparece la letra '{letra}' en la frase '{frase}' es {cantidad_coincidencias} ")
    historial(frase,letra,cantidad_coincidencias)
    
if __name__=="__main__":
    while True:
        main()
        rep=input("¿Desea repetir el programa? (y/n) ").strip().lower()
        if rep!="y":
            print("¡Adios!")
            break
        
