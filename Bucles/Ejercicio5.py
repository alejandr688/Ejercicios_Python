import os
import sys
from datetime import datetime

def get_numero(prompt: str) -> float:
    """
    Solicita al usuario un número positivo (float) mediante un mensaje.

    Parámetros:
        prompt (str): Texto que se muestra al pedir el dato.

    Retorna:
        float: Número ingresado por el usuario.
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("No digitó nada, intente de nuevo.")
                continue
            numero = float(user_input)
            if numero < 0:
                print("No puede ser una cantidad negativa.")
                continue
            return numero
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario.")
            sys.exit(0)
        except ValueError:
            print("Dato no válido.")

def historial(cantidad: float, interes: float, años: float, cantidad_final: float) -> None:
    """
    Registra en un archivo CSV la información de la inversión.

    Parámetros:
        cantidad (float): Monto inicial invertido.
        interes (float): Tasa de interés anual en porcentaje.
        años (float): Duración de la inversión en años.
        cantidad_final (float): Monto final tras los años invertidos.
    """
    fecha = datetime.now().strftime("%d/%B/%y %H:%M:%S")
    archivo = "Historial_inversiones.csv"
    existe = os.path.isfile(archivo)
    with open(archivo, "a", encoding="utf-8", newline="") as f:
        if not existe or os.stat(archivo).st_size == 0:
            f.write("Fecha, Cantidad, Interes, Años, Cantidad_Final\n")
        f.write(f"{fecha}, {cantidad}, {interes}, {años}, {cantidad_final}\n")

def calculo(cantidad: float, interes: float, años: float) -> list[float]:
    """
    Calcula el capital obtenido cada año durante la inversión.

    Parámetros:
        cantidad (float): Monto inicial invertido.
        interes (float): Tasa de interés anual en porcentaje.
        años (float): Duración de la inversión en años.

    Retorna:
        list[float]: Lista con el capital obtenido al final de cada año.
    """
    cantidades = []
    for i in range(1, int(años) + 1):
        obtenido = round(cantidad * (1 + interes / 100) ** i, 2)
        print(f"Cantidad después de {i} año(s): {obtenido}")
        cantidades.append(obtenido)
    return cantidades

def main():
    """
    Función principal que ejecuta la lógica del programa:
    - Solicita datos al usuario.
    - Realiza los cálculos.
    - Muestra resultados.
    - Registra historial.
    """
    cantidad = get_numero("Digite la cantidad inicial a invertir: ")
    interes = get_numero("Digite el interés anual (%): ")
    años = get_numero("Digite la cantidad de años: ")
    ganancias = calculo(cantidad, interes, años)
    historial(cantidad, interes, años, ganancias[-1])

if __name__ == "__main__":
    while True:
        main()
        rep = input("¿Desea repetir el programa? (y/n): ").strip().lower()
        if rep != "y":
            print("¡Adiós!")
            break
