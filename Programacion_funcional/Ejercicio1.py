

import os
import sys 
from datetime import datetime 

def get_input(prompt:str)->float:
    while True:
        try:
            user_input=input(prompt).strip()
            if not user_input:
                print("No digitó nada, intente de nuevo. ")
                continue
            numero=float(user_input)
            if numero<0:
                print("Cantidad no válida")
                continue
            return numero
        except ValueError:
            print("Dato no válido")
        except KeyboardInterrupt:
            print("Programa interrumpido por el usuario. Saliendo")
            sys.exit(0)
            
def get_producto(prompt:str)->str:
    while True:
        try:
            entrada=input(prompt).strip()
            if not entrada:
                print("No digitó nada, intente de nuevo ")
                continue
            return entrada
        except KeyboardInterrupt:
            print("Programa interrumpido por el usuario. Saliendo")
            sys.exit(0)
            
def descuento(precio:float)->tuple[float,float]:
    while True:
        descuento=get_input("Digite el descuento que obtuvo en porcentaje: ")
        if descuento>100:
            print("Descuento no válido")
            continue
        return (precio*(descuento/100),descuento)
        


def iva(precio:float)->tuple[float,float]:
    while True:
        iva=get_input("Digite el IVA se que va a aplicar en porcentaje: ")
        if iva>100:
            print("IVA no válido, intenta de nuevo ")
            continue
        return (precio*(iva/100),iva)
    
def cesta()->tuple[dict[str, dict[str, float]], float, float]:
    cesta={}
    valor_iva=0.0
    valor_descuento=0.0
    while True:
        producto=get_producto("Digite el nombre del producto o 'q' para salir: ")
        if producto.lower()=='q':
            return (cesta,valor_iva,valor_descuento)
        precio=get_input("Digite el precio del producto: ")
        discount,valor_descuento=descuento(precio)
        IVA,valor_iva=iva(precio)
        cesta[producto]={
            "Precio":precio,
            "Descuento":discount,
            "IVA":IVA
        }
        
def historial(cesta:dict,preciofinal:float)->None:
    fecha=datetime.now().strftime("%Y-%m-%d %H:%M:%S ")
    archivo="Historial.csv"
    existe=os.path.isfile(archivo)
    try:
        with open(archivo,"a",newline="",encoding="utf-8",errors="replace") as f:
            if not existe or os.stat(archivo).st_size==0:
                f.write(f"Fecha, Producto, Precio_inicial, Descuento, IVA, Precio_final\n")
            for clave, valor in cesta.items():
                f.write(f"{fecha}, {clave}, {valor['Precio']:.2f}, {valor['Descuento']:.2f}, {valor['IVA']:.2f}, {preciofinal}\n")
    except (IOError, OSError, FileNotFoundError) as e:
        print(f"Error: {e}")
        
def main():
    cesta_de_compras,valor_iva,valor_descuento=cesta()
    print("===Precios finales para cada produtco===")
    for clave, valor in cesta_de_compras.items():
        precio_final=valor["Precio"]-valor["Descuento"]+valor["IVA"]
        print(f"Producto: {clave}\n"
            f"Precio inicial: {valor['Precio']:.2f}\n"
            f"Descuento ({valor_descuento}%): {valor["Descuento"]:.2f}\n"
            f"IVA ({valor_iva}%): {valor["IVA"]:.2f}\n"
            f"Precio final: {precio_final:.2f}"
            )
        historial(cesta_de_compras,precio_final)
        
if __name__=="__main__":
    while True:
        main()
        rep=input("¿Desea repetir el programa? (Y/N) ").strip().lower()
        if rep!="y":
            print("Adios, gracias por su compra")
            break
    