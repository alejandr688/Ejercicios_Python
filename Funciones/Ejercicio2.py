"""Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!."""

def saludo(nombre:str)->str:
    print(f"Hola {nombre}")
    
def main():
    nombre=input("Escriba su nombre: ")
    saludo(nombre)
    
if __name__=="__main__":
    main()