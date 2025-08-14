import sys
import re
import csv
from datetime import datetime

ARCHIVO_HISTORIAL = "historial_clientes.csv"

def get_input(prompt: str) -> str:
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("No digitó nada, intente de nuevo.")
                continue
            return user_input
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario. Saliendo")
            sys.exit(0)

def get_opcion() -> int:
    while True:
        try:
            entrada = get_input(
                "Escoja una de las siguientes opciones"
                "\n(1) Añadir cliente"
                "\n(2) Eliminar cliente"
                "\n(3) Mostrar cliente"
                "\n(4) Listar todos los clientes"
                "\n(5) Listar clientes preferentes"
                "\n(6) Terminar"
                "\n-> "
            )
            opcion = int(entrada)
            if 1 <= opcion <= 6:
                return opcion
            print("Opción no válida.")
        except ValueError:
            print("Debe ingresar un número.")

def get_NIF() -> str:
    while True:
        patron_nif = r'^\d{8}[A-Z]$'
        NIF = get_input("Digite su NIF (8 dígitos y una letra mayúscula): ").upper()
        if re.fullmatch(patron_nif, NIF):
            return NIF
        print("NIF no válido.")

def get_telefono() -> str:
    while True:
        patron_telefono = r'^\d{10}$'
        numero = get_input("Digite su número (10 dígitos): ")
        if re.fullmatch(patron_telefono, numero):
            return numero
        print("Número inválido.")

def get_correo() -> str:
    while True:
        patron_correo = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
        correo = get_input("Digite su correo: ")
        if re.fullmatch(patron_correo, correo):
            return correo
        print("Correo inválido.")

def get_preferente() -> bool:
    while True:
        es_pref = get_input("¿Es cliente preferente? (s/n): ").lower()
        if es_pref in ("s", "n"):
            return es_pref == "s"
        print("Respuesta no válida.")

def guardar_historial(accion: str, nif: str, datos: dict = None):
    """Guarda en un archivo CSV la acción realizada."""
    with open(ARCHIVO_HISTORIAL, mode="a", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)
        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if datos:
            writer.writerow([fecha_hora, accion, nif, datos.get("nombre", ""), datos.get("direccion", ""), datos.get("telefono", ""), datos.get("correo", ""), datos.get("preferente", "")])
        else:
            writer.writerow([fecha_hora, accion, nif])

def diccionario(registro: dict) -> bool:
    opcion = get_opcion()

    if opcion == 1:  # Añadir cliente
        NIF = get_NIF()
        nombre = get_input("Nombre: ")
        direccion = get_input("Dirección: ")
        telefono = get_telefono()
        correo = get_correo()
        preferente = get_preferente()

        registro[NIF] = {
            "nombre": nombre,
            "direccion": direccion,
            "telefono": telefono,
            "correo": correo,
            "preferente": preferente
        }
        print("Cliente guardado con éxito.")
        guardar_historial("Añadir", NIF, registro[NIF])

    elif opcion == 2:  # Eliminar cliente
        NIF = get_NIF()
        if NIF in registro:
            datos_cliente = registro[NIF]
            del registro[NIF]
            print("Cliente eliminado.")
            guardar_historial("Eliminar", NIF, datos_cliente)
        else:
            print("NIF no encontrado.")

    elif opcion == 3:  # Mostrar cliente
        NIF = get_NIF()
        if NIF in registro:
            cliente = registro[NIF]
            print(f"NIF: {NIF}")
            for k, v in cliente.items():
                print(f"{k.capitalize()}: {v}")
            guardar_historial("Mostrar", NIF, cliente)
        else:
            print("NIF no encontrado.")

    elif opcion == 4:  # Listar todos
        if registro:
            for nif, datos in registro.items():
                print(f"NIF: {nif} | Nombre: {datos['nombre']}")
            guardar_historial("Listar todos", "-", {})
        else:
            print("No hay clientes registrados.")

    elif opcion == 5:  # Listar preferentes
        pref = [(nif, datos) for nif, datos in registro.items() if datos["preferente"]]
        if pref:
            for nif, datos in pref:
                print(f"NIF: {nif} | Nombre: {datos['nombre']}")
            guardar_historial("Listar preferentes", "-", {})
        else:
            print("No hay clientes preferentes.")

    elif opcion == 6:
        print("Fin del programa.")
        guardar_historial("Salir", "-", {})
        return True

    return False

def main():
    # Crear el archivo CSV con encabezados si no existe
    try:
        with open(ARCHIVO_HISTORIAL, mode="x", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)
            writer.writerow(["FechaHora", "Accion", "NIF", "Nombre", "Direccion", "Telefono", "Correo", "Preferente"])
    except FileExistsError:
        pass  # Si ya existe, no lo sobrescribimos

    registro = {}
    while True:
        if diccionario(registro):
            break

if __name__ == "__main__":
    main()
