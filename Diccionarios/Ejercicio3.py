"""Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, 
un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un 
mensaje informando de ello."""
import sys 
import os 
from datetime import datetime
import unicodedata
import locale
locale.setlocale(locale.LC_TIME,"Spanish")

def get_input(prompt:str)->str:
    while True:
        try:
            user_input=input(prompt).strip().lower()
            if not user_input:
                print("No digitó nada, intente de nuevo. ")
                continue
            return user_input
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario. Saliendo")
            sys.exit()
            
def historial(fruta:str, kilos:float, precio:float)->None:
    fecha=datetime.now().strftime("%d/%B/%y %H:%M:%S")
    archivo="Historial.csv"
    existe=os.path.isfile(archivo)
    try:
        with open(archivo,"a",newline="",encoding="utf-8") as f:
            if not existe or os.stat(archivo).st_size==0:
                f.write("Fecha, fruta, kilos, precio\n")
            f.write(f"{fecha}, {fruta}, {kilos}, {precio:.2f}\n")
    except (IOError, OSError, FileNotFoundError, PermissionError) as e:
        print(f"No se pudo escribir en el archivo: {e}")
        
def normalizar(texto:str)->str:
    texto=unicodedata.normalize("NFKD",texto)
    return "".join(c for c in texto if not unicodedata.combining(c))

def diccionario()->dict:
    catalogo={"platano":1.35,"manzana":0.80,"pera":0.85,"naranja":0.70}
    datos={}
    while True:
        fruta=get_input("Escriba una fruta de su elección:\n-Plátano\n-Manzana\n-Pera\n-Naranja\n-> ")
        fruta_normalizada=normalizar(fruta)
        if not fruta_normalizada in catalogo:
            print("Esa fruta no está disponible.")
            continue
        datos["Fruta"]=fruta
        break
    while True:
        try:
            kilos=get_input("Digite la cantidad de kilos de esa fruta: ")
            kilos=float(kilos)
            if kilos<0:
                print("No puedes tener kilos negativos.")
                continue
            datos["Kilos"]=kilos
            break
        except ValueError:
            print("Cantidad no válida. ")
    precio=kilos*catalogo[fruta_normalizada]
    datos["Precio"]=precio
    historial(fruta, kilos, precio)
    print(f"El precio por kilo de la fruta {fruta_normalizada} es de {catalogo[fruta_normalizada]} $")
    return datos

def main():
    datos=diccionario()
    print(f"Para la fruta {datos["Fruta"]}, usted compró {datos["Kilos"]} kilos con precio total de {datos["Precio"]:.2f} $")
    
if __name__=="__main__":
    while True:
        main()
        rep=get_input("¿Desea repetir el programa? (y/n) ")
        if rep!="y":
            print("¡Adios!")
            break
    
    
    