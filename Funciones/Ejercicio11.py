"""Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia. 
Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia."""


import re
from collections import Counter
from typing import Dict, Tuple, Optional

def frecuencias_palabras(texto: str) -> Dict[str, int]:
    """
    Recibe una cadena y devuelve un diccionario {palabra: frecuencia}.
    - Normaliza a minúsculas.
    - Ignora puntuación común (conserva letras acentuadas y ñ).
    """
    # Extrae "palabras" incluyendo acentos, ñ y dígitos (si los hay).
    tokens = re.findall(r"[A-Za-zÁÉÍÓÚáéíóúÜüÑñ0-9']+", texto.lower())
    return dict(Counter(tokens))

def palabra_mas_repetida(freq: Dict[str, int]) -> Optional[Tuple[str, int]]:
    """
    Recibe el diccionario de frecuencias y devuelve (palabra, frecuencia)
    de la palabra más repetida. Si el diccionario está vacío, devuelve None.
    """
    if not freq:
        return None
    palabra, cuenta = max(freq.items(), key=lambda kv: kv[1])
    return palabra, cuenta

if __name__ == "__main__":
    cadena = input("Introduce una cadena de texto: ")
    freq = frecuencias_palabras(cadena)
    print("Frecuencias por palabra:", freq)

    resultado = palabra_mas_repetida(freq)
    if resultado is None:
        print("No hay palabras en la cadena.")
    else:
        palabra, cuenta = resultado
        print(f"La palabra más repetida es '{palabra}' con {cuenta} apariciones.")
