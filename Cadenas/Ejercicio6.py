""" 
Escribir un programa que pida al usuario que introduzca una frase en consola y una vocal, 
y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
"""

import sys

def get_frase_vocal(prompt: str) -> str:
    """
    Solicita al usuario una entrada de texto con un mensaje personalizado.

    Args:
        prompt (str): El mensaje que se mostrará al usuario al solicitar la entrada.

    Returns:
        str: La cadena ingresada por el usuario, con espacios al inicio y final eliminados.

    Nota:
        Si el usuario presiona Ctrl+C, el programa mostrará un mensaje y se cerrará.
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

def main():
    """
    Función principal del programa.

    - Solicita una vocal al usuario y verifica que sea válida.
    - Solicita una frase al usuario.
    - Reemplaza todas las ocurrencias de la vocal en la frase con la misma vocal en mayúscula.
    - Muestra la frase modificada por pantalla.
    """
    while True:
        vocal = get_frase_vocal("Digite una vocal por favor (a, e, i, o, u): ").lower()
        if vocal not in ["a", "e", "i", "o", "u"]:
            print(f"'{vocal}' no está dentro de ['a', 'e', 'i', 'o', 'u']. Intenta de nuevo.")
            continue
        break
    frase = get_frase_vocal("Ahora digite una frase cualquiera: ")
    frase_modificada = frase.replace(vocal, vocal.upper())
    print(frase_modificada)

if __name__ == "__main__":
    main()
