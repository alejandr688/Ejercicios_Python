"""Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas."""
lista=[1,2,3,4,5,6,7,8,9,10]
print("Orden inverso: ", ", ".join([str(n) for n in sorted(lista, reverse=True)]))