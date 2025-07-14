"""
Programa que pregunta al usuario su edad y le indica si es mayor de edad.
Registra la fecha y la edad en un archivo 'Historial.txt'.
El usuario puede repetir el proceso varias veces si así lo desea.
"""

from datetime import datetime
import sys

def get_edad(prompt: str) -> int:
    """
    Solicita al usuario que ingrese su edad mediante un mensaje por consola.
    Repite la solicitud hasta que el usuario ingrese un valor válido (entero positivo).
    
    Parámetros:
    -----------
    prompt : str
        Mensaje que se muestra al usuario para solicitar la edad.
    
    Retorna:
    --------
    int
        Edad ingresada por el usuario como un entero.
    
    Excepciones:
    ------------
    - ValueError: Si el valor ingresado no es un número entero válido.
    - KeyboardInterrupt: Permite al usuario salir del programa con Ctrl+C.
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("No digitó nada, intente de nuevo. ")
                continue
            edad = int(user_input)
            return edad
        except ValueError:
            print("Edad no válida, intente de nuevo. ")
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario. Saliendo ")
            sys.exit(0)

def main():
    """
    Función principal que gestiona la lógica del programa:
    - Solicita la edad del usuario.
    - Valida que la edad esté en un rango razonable (0 a 120 años).
    - Informa si el usuario es mayor o menor de edad.
    - Guarda la fecha y la edad en el archivo 'Historial.txt'.
    Permite repetir la solicitud si se ingresa una edad inválida.
    """
    while True:
        edad = get_edad("Digite su edad por favor: ")
        if edad < 0 or edad > 120:
            print("Edad no válida")
            continue
        if edad >= 18:
            print("Es mayor de edad. ")
        else:
            print("Es menor de edad. ")
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("Historial.txt", "a", encoding="utf-8") as f:
            f.write(f"\n{fecha}\nEdad: {edad}\n años")
        break

if __name__ == "__main__":
    """
    Punto de entrada principal del programa.
    Permite al usuario repetir el proceso según su elección.
    """
    while True:
        main()
        rep = input("¿Quiere repetir el programa? (Y/N) ").strip().lower()
        if rep != "y":
            print("¡Hasta luego! ")
            break
