"""Este programa almacena una contraseña predefinida y solicita al usuario que la introduzca.
Compara la entrada del usuario con la contraseña almacenada, ignorando mayúsculas y minúsculas.
Si el usuario falla más de 5 veces, se bloquea el acceso. Los intentos incorrectos se guardan en un archivo con fecha y hora."""

import sys
import getpass
from datetime import datetime

# Contraseña predefinida (en minúsculas)
contraseña_verdadera = "contraseña"

def get_password(prompt: str) -> str:
    """
    Solicita al usuario una contraseña de manera oculta (no visible en pantalla).
    
    Parámetros:
    prompt (str): El mensaje a mostrar al usuario.
    
    Retorna:
    str: La contraseña introducida por el usuario en minúsculas.
    
    Salida del programa:
    Si el usuario interrumpe con Ctrl+C, el programa termina limpiamente.
    """
    while True:
        try:
            user_input = getpass.getpass(prompt).strip()
            if not user_input:
                print("No digitó nada, intente de nuevo. ")
                continue
            return user_input.lower()
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario. Saliendo ")
            sys.exit(0)

def main():
    """
    Función principal que controla el flujo del programa:
    - Pide la contraseña hasta que el usuario acierte o falle 5 veces.
    - Registra los intentos fallidos en el archivo 'Historial.txt' con fecha y hora.
    - Informa si la contraseña es correcta o si se ha excedido el número de intentos.
    """
    contador = 0
    with open("Historial.txt", "a", encoding="utf-8") as f:
        f.write(f"\n\nContraseñas incorrectas: \n")

    while True:
        contraseña = get_password("Escriba la contraseña correcta: ")
        contador += 1
        if contraseña == contraseña_verdadera:
            print("Contraseña correcta :D ")
            break
        if contador >= 5:
            print("Número de intentos máximos fallidos, bloqueando")
            break
        else:
            print("Contraseña incorrecta D: ")
            hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("Historial.txt", "a", encoding="utf-8") as f:
                f.write(f"\n{contador} - {contraseña} - {hora}")
            continue

if __name__ == "__main__":
    """
    Ejecuta el programa en un bucle hasta que el usuario decida no repetirlo.
    """
    while True:
        main()
        rep = input("¿Quiere repetir el programa? (Y/N) ").strip().lower()
        if rep != "y":
            print("Adiosito ")
            break
