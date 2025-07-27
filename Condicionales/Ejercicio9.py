import sys
from datetime import datetime
import os

def get_edad(prompt: str) -> int:
    """
    Solicita la edad al usuario de forma interactiva, validando que el valor sea un entero positivo y realista (0-120).
    
    Args:
        prompt (str): Mensaje que se muestra al solicitar la edad.
    
    Returns:
        int: Edad ingresada por el usuario (entre 0 y 120).

    Manejo de errores:
        - Si el usuario ingresa un valor no numérico, negativo, mayor a 120 o vacío, se solicita de nuevo.
        - Si el usuario interrumpe con Ctrl+C, el programa termina educadamente.
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("No digitó nada, intente de nuevo. ")
                continue
            edad = int(user_input)
            if edad < 0:
                print("No puedes tener una edad negativa. ")
                continue
            if edad > 120:
                print("Limite de edad superada. ")
                continue
            return edad
        except ValueError:
            print("Dato no válido")
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario. Saliendo ")
            sys.exit(0)
            
def criterio(edad: int) -> str:
    """
    Determina el costo de la entrada en función de la edad del cliente.

    Args:
        edad (int): Edad del cliente.

    Returns:
        str: Precio de la entrada ("gratis", "5$", "10$").
    """
    if edad < 4:
        return "gratis"
    elif 4 <= edad <= 18:
        return "5$"
    else:
        return "10$"
    
def historial(edad: int, pago: str):
    """
    Registra en un archivo CSV la fecha y hora, edad y pago correspondiente de cada cliente atendido.

    Args:
        edad (int): Edad del cliente.
        pago (str): Pago determinado según la edad.

    El archivo es creado si no existe y agrega una cabecera al inicio si el archivo está vacío.
    """
    fecha = datetime.now().strftime("%d/%m/%y %H:%M:%S")
    archivo = "historial.csv"
    existe = os.path.isfile(archivo) 
    with open(archivo, "a", newline="") as f:
        if not existe or os.stat(archivo).st_size == 0:
            f.write("fecha, edad, pago\n")
        f.write(f"{fecha}, {edad}, {pago}\n")
        
def main():
    """
    Función principal. Solicita la edad, calcula el pago, registra el historial y muestra el resultado.
    """
    edad = get_edad("Digite su edad porfavor: ")
    pago = criterio(edad)
    historial(edad, pago)
    print(f"Tiene {edad} años, su pago es: {pago}")


if __name__ == "__main__":
    while True:
        main()
        rep = input("¿Quiere repetir el programa? (Y/N) ").strip().lower()
        if rep != "y":
            print("¡Adios!")
            break
