"""Clasificación de alumnos en grupos A y B según su sexo y nombre.

El grupo A está formado por las mujeres con un nombre anterior a la M y los hombres con nombre posterior a la N.
El grupo B está formado por el resto.

El programa solicita al usuario su nombre y sexo, determina el grupo correspondiente y guarda un historial.
"""

import sys
from datetime import datetime

def get_string(prompt: str) -> str:
    """
    Solicita al usuario una cadena de texto, la limpia y la convierte a minúsculas.

    Parámetros:
        prompt (str): Mensaje que se muestra al usuario.

    Retorna:
        str: Cadena introducida por el usuario, en minúsculas y sin espacios al principio ni al final.
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("No digitaste nada, intente de nuevo. ")
                continue
            return user_input.lower()
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario. Saliendo...")
            sys.exit(0)

def clasificacion(sexo: str, nombre: str) -> str:
    """
    Determina el grupo (A o B) al que pertenece una persona según su sexo y nombre.

    Parámetros:
        sexo (str): Sexo de la persona ('hombre' o 'mujer').
        nombre (str): Nombre de la persona (en minúsculas).

    Retorna:
        str: 'A' si pertenece al grupo A, 'B' en caso contrario.
    """
    if (sexo == "mujer" and nombre < "m") or (sexo == "hombre" and nombre > "n"):
        return "A"
    else:
        return "B"

def historial(sexo: str, nombre: str, grupo: str) -> None:
    """
    Guarda el historial de clasificación en un archivo CSV con fecha y hora.

    Parámetros:
        sexo (str): Sexo de la persona.
        nombre (str): Nombre de la persona.
        grupo (str): Grupo asignado ('A' o 'B').
    """
    with open("Historial.csv", "a") as f:
        fecha = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
        f.write(f"\n{fecha}, {nombre}, {sexo}, {grupo}\n")

def main():
    """
    Función principal que gestiona la interacción con el usuario:
    - Solicita sexo y nombre.
    - Determina grupo.
    - Muestra resultado.
    - Guarda en historial.
    """
    while True:
        sexo = get_string("Digite su sexo (hombre o mujer): ")
        if sexo not in ["hombre", "mujer"]:
            print("Sexo no válido, intente de nuevo ")
            continue
        break
    nombre = get_string("Digite su nombre por favor: ")
    grupo = clasificacion(sexo, nombre)
    print(f"{nombre.title()} con sexo {sexo} está en el grupo {grupo}")
    historial(sexo, nombre, grupo)

if __name__ == "__main__":
    while True:
        main()
        rep = input("¿Quiere repetir el programa? (Y/N) ")
        if rep.lower() != "y":
            print("¡Adiós!")
            break
