"""Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'},
pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario."""

import sys
import unicodedata
import os
from datetime import datetime

catalogo={'euro':'€', 'dollar':'$', 'yen':'¥'}

def get_input(prompt:str)->str:
    while True:
        try:
            user_input=input(prompt).strip().lower()
            if not user_input:
                print("No se digitó nada, intente de nuevo")
                continue
            return user_input
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario. Saliendo ")
            sys.exit(0)
        except KeyError:
            print("Clave del diccionario no encontrada")

def historial(entrada:str)->str:
    fecha=datetime.now().strftime("%d/%m/%y %H:%M:%S")
    archivo="Historial.csv"
    existe=os.path.isfile(archivo)
    try:
        with open(archivo,"a",newline="",encoding="utf-8") as f:
            if not existe or os.stat(archivo).st_size==0:
                f.write("fecha_registro, entrada \n")
            f.write(f"{fecha},{entrada}\n")
    except (OSError,FileNotFoundError,IOError,PermissionError) as e:
        print(f"No se pudo escribir en el archivo: {e}")
        
def normalizar(texto:str)->str:
    texto=unicodedata.normalize("NFKD",texto)
    return "".join(c for c in texto if not unicodedata.combining(c))

def main():
    print("===Buscador de simbolos de divisas===")
    print("Escriba 'salir' para salir.")
    while True:
        divisa=get_input("Digite una divisa: ")
        if divisa=="salir":
            break
        normalizar(divisa)
        if not divisa in catalogo:
            print("Divisa no válida. ")
            continue
        print(f"El simbolo de la divisa {divisa.title()} es {catalogo[divisa]}. ")
        historial(divisa.title())
        
while True:
        main()
        rep=input("¿Desea repetir el programa?(Y/N) ").strip().lower()
        if rep!="y":
            print("¡Adios!")
            break