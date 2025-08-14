"""Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.)
que se le pida al usuario. Cada vez que se añada un nuevo dato de una persona debe imprimirse el contenido del diccionario."""

import sys
import os 
from datetime import datetime 
import locale
locale.setlocale(locale.LC_ALL, "Spanish")
import unicodedata
import re

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
            
def historial(nombre:str,edad:int,sexo:str,telefono:int,correo:str)->None:
    fecha=datetime.now().strftime("%d/%B/%y %H:%M:%S")
    archivo="Historial.csv"
    existe=os.path.isfile(archivo)
    try:
        with open(archivo,"a",newline="",encoding="utf-8",errors="replace") as f:
            if not existe or os.stat(archivo).st_size==0:
                f.write("Fecha,Nombre, Edad, Sexo, Teléfono, Correo\n")
            f.write(f"{fecha}, {nombre}, {edad}, {sexo}, {telefono}, {correo}\n")
    except (IOError, OSError, FileNotFoundError, PermissionError) as e:
        print(f"No se pudo escribir en el archivo: {e}")

def normalizar(texto:str)->str:
    texto=unicodedata.normalize("NFKD",texto)
    return "".join(c for c in texto if not unicodedata.combining(c))    

def diccionario()->dict:
        datos={}
        nombre=get_input("Digite su nombre por favor: ")
        datos["nombre"]=nombre
        while True:
            try:
                edad=int(get_input("Digite su edad por favor: "))
                if edad<0 or edad>120:
                    print("Edad no permitida. ")
                    continue
                datos["edad"]=edad
                break
            except ValueError:
                print("Valor no válido")
        while True:
            sexos=["masculino", "femenino", "male","female","m","f","hombre","mujer","h"]
            sexo=get_input("Digite su sexo por favor(masculino/femenino): ")
            sexo_normalizado=normalizar(sexo)
            if sexo_normalizado in sexos:
                datos["sexo"]=sexo
                break
            print("Tipo de sexo no permitido. ")
            continue
        while True:
            try:
                telefono=int(get_input("Digite su teléfono por favor(10 digitos): "))
                if telefono<0 or len(str(telefono))!=10:
                    print("Numero de teléfono no válido")
                    continue
                datos["teléfono"]=telefono
                break
            except ValueError:
                print("Número inválido")
        while True:
            patron=r'^[A-Za-z0-9_.+-]+@[A-Za-z0-9-]+\.[A-Za-z0-9-.]+$'
            correo=get_input("Digite su correo electrónico por favor: ")
            if not re.fullmatch(patron,correo):
                print("Correo no válido, intente de nuevo. ")
                continue
            datos["correo"]=correo
            break
        print("===Datos nuevos===\n")
        for clave, valor in datos.items():
            print(f"{clave}: {valor}")
        return datos
    
def main():
    datos=diccionario()
    nombre,edad,sexo,telefono,correo=datos.values()
    historial(nombre,edad, sexo, telefono,correo)
    
if __name__=="__main__":
    while True:
        main()
        rep=get_input("¿Desea repetir el programa? (y/n) ")
        if rep!="y":
            print("¡Adiós!")
            break
    
            
            
