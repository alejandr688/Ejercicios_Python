"""
Este programa solicita al usuario un número de teléfono en el formato +34-XXXXXXXXX-XX,
donde:
- +34 es el prefijo del país,
- XXXXXXXXX es el número principal,
- XX es la extensión.
El programa extrae y muestra solo el número principal, sin el prefijo ni la extensión.
"""

import sys

def get_number(prompt: str) -> str:
    """
    Solicita al usuario un número de teléfono en el formato +34-XXXXXXXXX-XX.

    Args:
        prompt (str): Mensaje para pedir el número de teléfono.

    Returns:
        str: Número de teléfono introducido por el usuario.

    Maneja:
        - Si la entrada está vacía, vuelve a pedir el número.
        - Si el usuario interrumpe el programa con Ctrl+C, se sale de forma controlada.
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("No digitó nada, intente de nuevo.")
                continue
            return user_input
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario. Saliendo.")
            sys.exit(0)

def extraer_numero_principal(numero: str) -> str:
    """
    Extrae el número principal de un número de teléfono con formato +34-XXXXXXXXX-XX.

    Args:
        numero (str): Número de teléfono en el formato correcto.

    Returns:
        str: El número principal (sin prefijo ni extensión).

    Lanza:
        ValueError: Si el número no cumple el formato esperado.
    """
    partes = numero.split('-')
    if len(partes) != 3 or not partes[0].startswith('+'):
        raise ValueError("El número no tiene el formato +34-XXXXXXXXX-XX.")
    return partes[1]

def main():
    """
    Función principal del programa:
    - Pide al usuario el número de teléfono.
    - Extrae el número principal.
    - Muestra el número principal por pantalla.
    """
    numero = get_number("Digite el número de teléfono con el formato +34-XXXXXXXXX-XX: ")
    try:
        numero_principal = extraer_numero_principal(numero)
        print(f"El número principal es: {numero_principal}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
