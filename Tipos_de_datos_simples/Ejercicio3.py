"""Escribir un programa que pregunte el nombre del usuario en consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!,
donde el <nombre> es el nombre que el usuario haya introducido"""
import sys
def get_nombre()->str: #Estas son anotaciones de tipo, sirven para indicar el tipo de dato que se espera como argumento y el tipo de dato que se espera como retorno de la función.
    """Función para pedirle el nombre al usuario"""
    while True:
        try:
            user_input=input("Digita tu nombre por favor: ").strip() # el strip() elimina los espacios en blanco al principio y al final de la cadena
            if not user_input: #Verifica que la cadena no esté vacía
                print("El nombre no puede ser vacío, intenta de nuevo")
                continue
            return user_input
        except ValueError:
            print("Dato invalido, intenta de nuevo")
        except KeyboardInterrupt: #Esto sirve por si el usairio digita control+c,control+v, etc
            print("\nPrograma interrumpido por el usario, saliendo...")
            sys.exit()
            
def main():
    """Función principal main"""
    nombre=get_nombre() #Llamando a la función main
    print(f"Hola {nombre}")
    
if __name__=="__main__":
    main()