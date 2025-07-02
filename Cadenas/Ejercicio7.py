"""Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la @) pero con dominio ceu.es."""

import sys

def get_correo(prompt: str) -> str:
    """
    Solicita al usuario que introduzca un correo electrónico a través de la consola.
    
    Muestra el mensaje especificado en 'prompt' y devuelve la entrada del usuario
    como una cadena sin espacios al inicio ni al final. Si el usuario no ingresa nada,
    se le volverá a pedir. Si interrumpe el programa con Ctrl+C, se mostrará un mensaje
    y el programa terminará limpiamente.
    
    Parámetros:
    ----------
    prompt : str
        Mensaje que se muestra al usuario para solicitar la entrada.
        
    Retorna:
    -------
    str
        La cadena ingresada por el usuario, limpia de espacios.
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("No digitó nada, intente de nuevo. ")
                continue
            return user_input
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario. Saliendo ")
            sys.exit(0)

def main():
    """
    Función principal del programa.
    
    Solicita al usuario un correo electrónico, valida si contiene el carácter '@'.
    Si es válido, reemplaza el dominio por 'ceu.es' y muestra el correo original
    y el nuevo. Además, guarda ambos correos en un archivo 'Historial.txt'.
    Si el correo no es válido, solicita nuevamente al usuario otro correo.
    """
    while True:
        correo = get_correo("Digite su correo electrónico: ")
        if "@" not in correo:
            print("Correo no válido, intente de nuevo")
            continue
        usuario, dominio = correo.split("@", 1)
        correonuevo = f"{usuario}@ceu.es"
        print(f"Su correo original es {correo}\nSu correo nuevo es {correonuevo}")
        with open("Historial.txt", "a") as f:
            f.write(f"Correo original: {correo}\nCorreo nuevo: {correonuevo}\n")

if __name__ == "__main__":
    while True:
        main()
        rep = input("¿Quiere repetir el programa? (Y/N) ").strip().lower()
        if rep != "y":
            print("¡Adiós!")
            break
