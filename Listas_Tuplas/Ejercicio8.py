"""Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal."""
import os
import sys
from datetime import datetime
import unicodedata

def get_palabra(prompt:str)->str:
    while True:
        try:
            user_input=input(prompt).strip().lower()
            if not user_input:
                print("No digitó nada, intente de nuevo. ")
                continue
            if " " in user_input or "," in user_input:
                print("Digite una sola palabra por favor: ")
                continue
            return user_input
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario. Saliendo")
            sys.exit(0)
            
def historial(palabra:str,conteo:dict)->None:
    fecha=datetime.now().strftime("%d/%m/%y %H:%M:%S")
    archivo="Historial.txt"
    existe=os.path.isfile(archivo)
    try:
        with open(archivo,"a",encoding="utf-8",newline="") as f:
            if not existe or os.stat(archivo).st_size==0:
                f.write("Palabra, a, e, i, o, u\n")
            f.write(f"{fecha}\n, {palabra}, {conteo.get('a', 0)}, {conteo.get('e', 0)}, {conteo.get('i', 0)}, {conteo.get('o', 0)}, {conteo.get('u', 0)}\n")
    except (IOError,OSError,FileNotFoundError) as e:
        print(f"No se pudo escribir en el archivo: {e}")
        
def normalizador(palabra:str)->str:
    texto=unicodedata.normalize("NFKD",palabra)
    return ", ".join(c for c in texto if not unicodedata.combining(c))
    

def contador_vocales()->tuple[dict,str]:
    vocales="aeiou"
    palabra=get_palabra("Digite una palabra cualquiera: ")
    palabra_normalizada=normalizador(palabra)
    conteo={vocal:0 for vocal in vocales}
    for letra in palabra_normalizada:
        if letra in conteo:
            conteo[letra]+=1
    historial(palabra,conteo)
    return conteo,palabra
            
def main():
    datos,palabra=contador_vocales()
    print(f"Para la palabra: {palabra.title()}:")
    for clave, valor in datos.items():
        print(f"La vocal {clave} está {valor} veces")
        
if __name__=="__main__":
    while True:
        main()
        rep=input("¿Desea repetir el programa? (y/n) ").strip().lower()
        if rep!="y":
            print("¡Adios!")
            break
        
    
    