"""Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba 'salir' terminará"""

import os
import sys
from datetime import datetime

def get_input(prompt:str)->str:
    try:
        user_input=input(prompt)
        return user_input
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario")
        sys.exit(0)
def historial(texto:str)->None:
    fecha=datetime.now().strftime("%d/%b/%y %H:%M:%S")
    archivo="Historial.csv"
    existe=os.path.isfile(archivo)
    try:
        with open(archivo,"a",encoding="utf-8",newline="") as f:
            if not existe or os.stat(archivo).st_size==0:
                f.write("Fecha_registro, texto_escrito\n")
            f.write(f"{fecha}, {texto}\n")
    except (IOError,FileNotFoundError, OSError) as e:
        print(f"No se pudo escribir en el archivo: {e}")


def echo()->str:
    while True:
        texto=get_input("Escribe lo que quieras: ").strip().lower()
        if texto=="salir":
            print("Programa terminado")
            break
        print(f"Eco: {texto}")
        historial(texto)
    
    
def main():
    echo()


    
if __name__=="__main__":
    main()