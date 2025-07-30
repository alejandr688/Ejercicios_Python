"""Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.
"""

lista1=[1,2,3]
lista2=[4,5,6]

producto=sum(x*y for x,y in zip(lista1,lista2))
print(f"El producto punto es {producto}")