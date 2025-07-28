"""Escribir un programa que muestre la tabla de multiplicar del 1 al 10."""

def main():
    for i in range(1,11):
        print(f"Tabla del {i}")
        for j in range(1,11):
            print(f"{i}*{j}={i*j}")
        print("-"*20)
        
if __name__=="__main__":
    main()