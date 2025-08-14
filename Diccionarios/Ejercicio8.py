"""Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y 
cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español 
y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir."""

import sys
import re
import os
from datetime import datetime
import unicodedata
import locale 
locale.setlocale(locale.LC_ALL,"Spanish")

def get_input(prompt:str)->str:
    while True:
        try:
            user_input=input(prompt).strip()
            if not user_input:
                print("No digitó nada, intente de nuevo. ")
                continue
        except KeyboardInterrupt:
            print("Programa interrumpido por el usuario. Saliendo ")
            sys.exit(0)
        return user_input
def historial(datos:dict)->None:
    fecha=datetime.now().strftime("%d/%B/%y %H/%M/%S")
    archivo="Historial.csv"
    existe=os.path.isfile(archivo)
    try:
        with open(archivo,"a",newline="",encoding="utf-8",errors="replace") as f:
            if not existe or os.stat(archivo).st_size==0:
                f.write("Fecha, Palabra_Es, Palabra_EN\n")
            for palabra_es,palabra_en in datos.items():
                f.write(f"{fecha}, {palabra_es}, {palabra_en}\n")
    except (IOError, OSError, FileNotFoundError, PermissionError) as e:
            print(f"No se pudo escribir en el archivo: {e}")


def normalizar(texto:str)->str:
    texto=unicodedata.normalize("NFKD",texto)
    return "".join(c for c in texto if not unicodedata.combining(c))

def diccionario() -> dict:
    datos = {}
    patron = r'^([a-zA-ZñÑáéíóúüÁÉÍÓÚÜ0-9]+:[a-zA-ZñÑáéíóúüÁÉÍÓÚÜ0-9]+)(,([a-zA-ZñÑáéíóúüÁÉÍÓÚÜ0-9]+:[a-zA-ZñÑáéíóúüÁÉÍÓÚÜ0-9]+))*$'
    while True:
        entrada = get_input("Digite las palabras en español e inglés separadas por dos puntos (coma entre pares): ")
        if not re.fullmatch(patron, entrada):
            print("Formato equivocado. Intente de nuevo.")
            continue
        break

    pares = entrada.split(",")
    for par in pares:
        clave, valor = par.split(":", 1)
        datos[clave.strip().lower()] = valor.strip().lower()
    historial(datos)
    return datos


def traductor():
    datos=diccionario()
    frase=get_input("Digite una frase cualquiera por favor: ")
    frase_traducida=frase
    palabras=frase_traducida.split(" ")
    for palabra in palabras:
        if palabra.strip() in datos:
            palabra_traducida=datos[palabra]
        else:
            palabra_traducida=palabra
        frase_traducida=frase_traducida.replace(palabra,palabra_traducida)
    return frase, frase_traducida

def main():
    frase, frase_traducida=traductor()
    print(f"Frase original: {frase}\nFrase traducida: {frase_traducida}")
    

if __name__=="__main__":
    while True:
        main()
        rep=get_input("¿Quiere repetir el programa? (Y/N) ").lower()
        if rep!="y":
            print("¡Adios!")
            break
            