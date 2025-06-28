""" 
Programa para calcular el Índice de Masa Corporal (IMC) de un usuario.
Solicita al usuario su peso en kilogramos y estatura en metros, calcula el IMC,
muestra el resultado en pantalla junto con la categoría correspondiente,
y guarda cada cálculo en un archivo 'historial_imc.txt'.
"""

import sys

def get_values(prompt: str) -> float:
    """
    Solicita al usuario un valor numérico positivo con el mensaje dado.

    Parámetros:
    -----------
    prompt : str
        Mensaje que se mostrará al usuario al solicitar el valor.

    Retorna:
    --------
    float
        Valor ingresado por el usuario convertido a flotante, validado para ser positivo.

    Maneja errores de entrada como valores vacíos, no numéricos o negativos, y permite salir del programa con Ctrl+C.
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("Valor nulo, no digitó nada.")
                continue
            value = float(user_input)
            if value <= 0:
                print("El valor no puede ser negativo o cero, intente de nuevo.")
                continue
            return value
        except ValueError:
            print("Valor no válido.")
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario.")
            sys.exit(0)

def main():
    """
    Función principal del programa.
    Solicita estatura y peso al usuario, calcula el IMC, determina la categoría de peso,
    muestra el resultado y guarda un registro del cálculo en 'historial_imc.txt'.
    """
    estatura = get_values("Escriba su estatura en metros por favor: ")
    peso = get_values("Escriba su peso en kilogramos por favor: ")
    imc = peso / (estatura ** 2)

    if imc < 18.5:
        estado = "Bajo Peso"
    elif 18.5 <= imc <= 24.9:
        estado = "Peso normal"
    elif 25 <= imc <= 29.9:
        estado = "Sobrepeso"
    elif 30 <= imc <= 34.9:
        estado = "Obesidad grado 1"
    elif 35 <= imc <= 39.9:
        estado = "Obesidad grado 2"
    elif imc > 40:
        estado = "Obesidad grado 3"
    else:
        estado = "Fuera de rango"

    print(f"Su IMC es de {imc:.2f}, su estado es: {estado}")

    # Guardar en el historial de cálculos
    with open("historial_imc.txt", "a") as f:
        f.write(f"Estatura: {estatura:.2f} m, Peso: {peso:.1f} kg, IMC: {imc:.2f}, Estado: {estado}\n")

if __name__ == "__main__":
    """
    Bucle principal que permite al usuario realizar múltiples cálculos de IMC consecutivos,
    preguntando al final si desea repetir o salir del programa.
    """
    while True:
        main()
        rep = input("¿Desea hacer otro cálculo? (Y/N) ").strip().lower()
        if rep != "y":
            print("¡Hasta luego!")
            break
