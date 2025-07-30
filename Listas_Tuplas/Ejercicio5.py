from datetime import datetime
import os
import sys
import unicodedata

def get_input(prompt: str) -> str:
    """
    Solicita entrada del usuario con validación.
    """
    while True:
        try:
            user_input = input(prompt).strip().lower()
            if not user_input:
                print("No digitó nada, intente de nuevo.")
                continue
            return user_input
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario. Saliendo.")
            sys.exit(0)

def historial(diccionario: dict) -> None:
    """
    Guarda en un archivo de texto el historial de materias y calificaciones.
    """
    fecha = datetime.now().strftime("%d/%m/%y %H:%M:%S")
    archivo = "Historial.txt"
    existe = os.path.isfile(archivo)
    try:
        with open(archivo, "a", encoding="utf-8", newline="") as f:
            if not existe or os.stat(archivo).st_size == 0:
                f.write("Fecha,materia,calificación,estatus\n")
            for clave, valor in diccionario.items():
                estatus = "Aprobado" if valor >= 6 else "Reprobado"
                f.write(f"{fecha},{clave},{valor},{estatus}\n")
    except (IOError, OSError, FileNotFoundError) as e:
        print(f"No se pudo escribir en el archivo: {e}")

def normalizar(texto: str) -> str:
    """
    Normaliza un texto eliminando acentos.
    """
    texto = unicodedata.normalize("NFKD", texto)
    return ''.join(c for c in texto if not unicodedata.combining(c))

def diccionario() -> dict:
    """
    Pide al usuario materias y calificaciones. Retorna diccionario.
    """
    catalogo = {
        "fisica": "Física", "matematicas": "Matemáticas", "quimica": "Química", "biologia": "Biología",
        "historia": "Historia", "geografia": "Geografía", "espanol": "Español", "ingles": "Inglés",
        "etica": "Ética", "filosofia": "Filosofía", "computacion": "Computación", "programacion": "Programación",
        "algebra": "Álgebra", "geometria": "Geometría", "calculo": "Cálculo", "trigonometria": "Trigonometría",
        "estadistica": "Estadística", "probabilidad": "Probabilidad", "literatura": "Literatura",
        "educacion_fisica": "Educación Física", "artes": "Artes", "musica": "Música", "economia": "Economía",
        "derecho": "Derecho", "civismo": "Civismo", "robotica": "Robótica", "electronica": "Electrónica",
        "mecanica": "Mecánica", "astronomia": "Astronomía", "psicologia": "Psicología", "sociologia": "Sociología",
        "logica": "Lógica", "administracion": "Administración", "contabilidad": "Contabilidad"
    }

    datos = {}
    while True:
        clave = get_input("Digite la materia que cursó (o escriba 'salir' para terminar): ")
        if clave == "salir":
            break
        clave_normalizada = normalizar(clave)
        if clave_normalizada not in catalogo:
            print("Materia incorrecta.")
            continue
        materia = catalogo[clave_normalizada]
        if materia in datos:
            print("Ya ingresó esa materia.")
            continue

        while True:
            try:
                valor = int(get_input(f"Digite la calificación que obtuvo en {materia} (0-10): "))
                if 0 <= valor <= 10:
                    datos[materia] = valor
                    break
                else:
                    print("Calificación fuera de rango.")
            except ValueError:
                print("Calificación no válida.")
    return datos

def main():
    """
    Función principal del programa.
    """
    datos = diccionario()
    if not datos:
        print("No ingresó ninguna materia.")
        return

    historial(datos)

    # Filtra materias reprobadas
    reprobadas = [clave for clave, valor in datos.items() if valor < 6]

    if reprobadas:
        print("Las asignaturas que tiene que repetir son: " + ", ".join(reprobadas))
    else:
        print("¡Felicidades! No tiene asignaturas que repetir.")

if __name__ == "__main__":
    while True:
        main()
        repetir = input("¿Desea repetir el programa? (y/n): ").strip().lower()
        if repetir != "y":
            print("¡Adiós!")
            break
