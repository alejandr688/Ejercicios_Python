"""Programa que solicita una muestra de números, los guarda en una lista y muestra la media y desviación típica."""

import math

def obtener_muestra():
    """
    Solicita al usuario una lista de números separados por comas y los convierte a float.
    
    Retorna:
    list: Lista de números ingresados.
    """
    while True:
        entrada = input("Introduce una muestra de números separados por comas: ").strip()
        try:
            numeros = [float(num.strip()) for num in entrada.split(",") if num.strip()]
            if not numeros:
                print("Por favor ingresa al menos un número.")
                continue
            return numeros
        except ValueError:
            print("Entrada inválida. Asegúrate de ingresar solo números separados por comas.")

def calcular_media(lista):
    """Calcula la media de una lista de números."""
    return sum(lista) / len(lista)

def calcular_desviacion_tipica(lista, media):
    """Calcula la desviación típica de una lista de números."""
    varianza = sum((x - media) ** 2 for x in lista) / len(lista)
    return math.sqrt(varianza)

# Programa principal
muestra = obtener_muestra()
media = calcular_media(muestra)
desviacion = calcular_desviacion_tipica(muestra, media)

print(f"\nMuestra: {muestra}")
print(f"Media: {media:.2f}")
print(f"Desviación típica: {desviacion:.2f}")
