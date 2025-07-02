''' 
Escribir un programa que le pida al usuario que introduzca una frase en la consola 
y muestre por pantalla la frase invertida. El programa almacena un historial de las frases 
introducidas y sus correspondientes inversiones en un archivo de texto.
'''

import sys

def get_frase(prompt: str) -> str:
    """
    Solicita al usuario que introduzca una frase a través de la consola.
    
    El mensaje a mostrar se especifica en el parámetro 'prompt'.
    Si el usuario no introduce nada, se le pedirá de nuevo.
    Si el usuario interrumpe el programa con Ctrl+C, se muestra un mensaje y el programa finaliza.

    Args:
        prompt (str): El mensaje que se mostrará al usuario al solicitar la frase.

    Returns:
        str: La frase introducida por el usuario, eliminando espacios en blanco al inicio y final.
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("No digitó nada, intente de nuevo. ")
                continue
            return user_input
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario.\n")
            sys.exit(0)
            
def main():
    """
    Función principal del programa.

    Solicita una frase al usuario, invierte la frase y la muestra en pantalla.
    También guarda tanto la frase original como la invertida en un archivo llamado 'Historial.txt'.
    """
    frase = get_frase("Digite una frase cualquiera por favor: ")
    frase_invertida = frase[::-1]
    print(f"La frase original es: {frase}\nLa frase invertida es: {frase_invertida}\n")
    with open("Historial.txt", "a") as f:
        f.write(f"La frase original es: {frase}\nLa frase invertida es: {frase_invertida}\n\n")

if __name__ == "__main__":
    while True:
        main()
        rep = input("¿Desea repetir el programa? (Y/N) ").strip().lower()
        if rep != "y":
            print("¡Hasta luego!")
            break
