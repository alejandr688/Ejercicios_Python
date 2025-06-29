"""
Este programa solicita al usuario que ingrese su nombre completo y luego muestra el nombre de tres formas:
1) Todo en minúsculas.
2) Todo en mayúsculas.
3) Con la primera letra de cada palabra en mayúscula.
El usuario puede ingresar su nombre con cualquier combinación de mayúsculas y minúsculas. El programa también guarda cada entrada
en un archivo de historial llamado 'Historial.txt' y permite repetir el proceso.
"""

import sys

def get_nombre_completo(prompt: str) -> str:
    """
    Solicita al usuario que introduzca su nombre completo mediante un mensaje en consola.
    
    Parámetros:
    ----------
    prompt : str
        Mensaje que se muestra al usuario para pedir la entrada.
    
    Retorna:
    -------
    str
        El nombre completo introducido por el usuario, sin espacios iniciales ni finales.
    
    Excepciones:
    -----------
    ValueError:
        Si la entrada no es válida (aunque en este contexto es improbable que ocurra).
    KeyboardInterrupt:
        Permite salir del programa limpiamente si el usuario presiona Ctrl+C.
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("No digitó nada, intente de nuevo. ")
                continue
            return user_input
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario. Saliendo")
            sys.exit(0)
            
def main():
    """
    Ejecuta la lógica principal del programa:
    - Obtiene el nombre completo del usuario.
    - Imprime el nombre en minúsculas, mayúsculas y capitalizado (title case).
    - Guarda la entrada en un archivo llamado 'Historial.txt'.
    """
    nombre = get_nombre_completo("Digite su nombre completo por favor: ")
    print(f"{nombre.lower()}\n{nombre.upper()}\n{nombre.title()}\n")
    with open("Historial.txt", "a") as f:
        f.write(f"{nombre}\n")

if __name__ == "__main__":
    """
    Bucle principal que permite repetir el programa tantas veces como el usuario desee.
    Después de cada ejecución, pregunta si se quiere volver a ejecutar.
    """
    while True:
        main()
        rep = input("¿Quiere repetir el programa? (Y/N) ").strip()
        if rep.lower() != "y":
            print("¡Hasta luego! ")
            break
