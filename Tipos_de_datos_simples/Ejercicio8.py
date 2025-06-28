"""
Escribir un programa que pida al usuario dos números enteros y muestre por pantalla
"<n> entre <m> da un cociente <c> y un resto <r>",
donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente
y el resto de la división entera respectivamente. Además, guarda cada operación realizada
en un archivo llamado 'Historial.txt'.
"""

import sys

def get_values(prompt: str) -> int:
    """
    Solicita un número entero al usuario con el mensaje indicado.

    Parámetros:
    -----------
    prompt : str
        El mensaje que se mostrará al usuario al solicitar el número.

    Retorna:
    --------
    int
        Número entero ingresado por el usuario.

    Maneja errores como entradas vacías, valores no numéricos y permite salir del programa
    con Ctrl+C (KeyboardInterrupt).
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("No digitó nada, intente de nuevo.")
                continue
            value = int(user_input)
            return value
        except ValueError:
            print("Valor inválido.")
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario.")
            sys.exit(0)

def main():
    """
    Función principal: solicita dos números enteros al usuario, calcula el cociente y el resto
    de su división entera, muestra los resultados por pantalla y los guarda en 'Historial.txt'.
    También gestiona el error de división entre cero mostrando un mensaje de advertencia.
    """
    n = get_values("Digite el valor de n: ")
    m = get_values("Digite el valor de m: ")
    try:
        c = n // m
        r = n % m
        print(f"{n} entre {m} da un cociente de {c} y un resto de {r}.")
        with open("Historial.txt", "a") as f:
            f.write(f"n: {n}, m: {m}, cociente: {c}, resto: {r}\n")
    except ZeroDivisionError:
        print("Error, división entre cero no válida.")

if __name__ == "__main__":
    """
    Bucle principal del programa: permite realizar múltiples cálculos consecutivos,
    preguntando al usuario si desea repetir tras cada ejecución.
    """
    while True:
        main()
        rep = input("¿Quiere repetir el programa? (Y/N) ").strip().lower()
        if rep != "y":
            print("¡Hasta luego!")
            break
