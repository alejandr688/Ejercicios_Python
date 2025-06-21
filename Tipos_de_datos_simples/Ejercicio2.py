'''Escribir un programa que almacene la cadena "¡Hola mundo!" en una variable y luego muestre por pantalla el contenido de esa variable'''
# Declaramos una variable llamada saludo y le asignamos un texto (cadena de caracteres o string)
saludo = "Hello world"

# Imprimimos el contenido de la variable usando la función print
print(saludo)

# ------------------------------
# Distintas formas de imprimir el contenido de una variable en Python:
# ------------------------------

# 1. Usando f-strings (formato moderno desde Python 3.6)
# Muy útil cuando quieres insertar variables directamente dentro del texto
print(f"El saludo es {saludo}")  # Salida: El saludo es Hello world

# 2. Usando comas en print
# Las comas añaden automáticamente espacios entre los elementos
print("El saludo es", saludo)   # Salida: El saludo es Hello world

# 3. Concatenando strings con +
# Nota: todas las partes deben ser strings, si no da error
print("El saludo es " + saludo)  # Salida: El saludo es Hello world

# 4. Usando el método .format()
# Otra manera versátil y muy usada de formatear cadenas
print("El saludo es {}".format(saludo))  # Salida: El saludo es Hello world

# ------------------------------
# Nota adicional:
# Todas estas formas sirven para mostrar variables dentro de textos,
# y elegir una u otra depende de tu estilo y versión de Python.
# Las f-strings suelen ser la forma más legible y moderna.
# ------------------------------

# Extra: si quieres saber el tipo de dato de una variable puedes hacer esto:
print(type(saludo))  # Salida: <class 'str'>

# También puedes transformar variables a texto con str() si es necesario:
numero = 5
print("El número es " + str(numero))  # Evita error de tipo al concatenar
