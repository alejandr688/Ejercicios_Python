import sys
from datetime import datetime

ingredientes_base = ("Mozzarella", "Tomate")
ingredientes_vegetariano = {"pimiento": "Pimiento", "tofu": "Tofú"}
ingredientes_no_vegetariano = {"peperoni": "Peperoni", "jamon": "Jamón", "salmon": "Salmón"}

historial = []  # Guarda historial de pedidos


def get_input(prompt: str) -> str:
    """
    Solicita y valida la entrada del usuario.
    Convierte a minúsculas y elimina espacios.
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


def eleccion() -> tuple:
    """
    Pregunta si la pizza es vegetariana o no.
    Muestra ingredientes según el tipo.
    Devuelve el ingrediente elegido y el tipo de pizza.
    """
    while True:
        opcion = get_input("¿Desea una pizza vegetariana? (y/n): ")
        if opcion == "y":
            print("\nMenú de ingredientes vegetarianos:")
            for ingr in ingredientes_vegetariano.values():
                print(f"- {ingr}")
            ingrediente = get_input("Elija un ingrediente: ")
            ingrediente = normalizar_ingrediente(ingrediente, ingredientes_vegetariano)
            if ingrediente:
                return ingrediente, "vegetariana"
            else:
                print("Ingrediente no válido, intente de nuevo.\n")
        elif opcion == "n":
            print("\nMenú de ingredientes no vegetarianos:")
            for ingr in ingredientes_no_vegetariano.values():
                print(f"- {ingr}")
            ingrediente = get_input("Elija un ingrediente: ")
            ingrediente = normalizar_ingrediente(ingrediente, ingredientes_no_vegetariano)
            if ingrediente:
                return ingrediente, "no vegetariana"
            else:
                print("Ingrediente no válido, intente de nuevo.\n")
        else:
            print("Opción inválida. Use 'y' o 'n'.\n")


def normalizar_ingrediente(nombre: str, opciones: dict) -> str | None:
    """
    Intenta encontrar el ingrediente en el diccionario sin importar acentos.
    """
    nombre = nombre.lower().replace("á", "a").replace("é", "e").replace("í", "i")\
                           .replace("ó", "o").replace("ú", "u")
    return opciones.get(nombre, None)


def registrar_en_historial(tipo: str, ingrediente: str):
    """
    Guarda el pedido con la fecha y hora en el historial.
    """
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    historial.append(f"[{ahora}] Pizza {tipo} con Mozzarella, Tomate y {ingrediente}")


def mostrar_historial():
    """
    Muestra todos los pedidos guardados en el historial.
    """
    print("\n--- Historial de pedidos ---")
    if not historial:
        print("No hay pedidos aún.")
    else:
        for entrada in historial:
            print(entrada)
    print("-" * 30 + "\n")


def main():
    """
    Ejecuta una sesión del pedido de pizza.
    """
    ingrediente, tipo = eleccion()
    registrar_en_historial(tipo, ingrediente)
    print(f"\nPizza {tipo} con los siguientes ingredientes:")
    for i in ingredientes_base:
        print(f"- {i}")
    print(f"- {ingrediente}\n")


if __name__ == "__main__":
    while True:
        main()
        mostrar_historial()
        repetir = get_input("¿Desea hacer otro pedido? (y/n): ")
        if repetir != "y":
            print("¡Gracias por su visita a Bella Napoli!")
            break
