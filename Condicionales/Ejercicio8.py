"""En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y
pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores 
intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero 
conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

Nivel	Puntuación
Inaceptable	0.0
Aceptable	0.4
Meritorio	0.6 o más

Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.
"""
import sys
from datetime import datetime
import os
puntuacion_valida=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]

def get_score(prompt:str)->float:
    while True:
        try:
            user_input=input(prompt).strip()
            if not user_input:
                print("No digitaste nada, intenta de nuevo. ")
                continue
            score=float(user_input)
            if score<0:
                print("El valor no puede ser negativo. ")
                continue
            if score in puntuacion_valida:
                return score
            else:
                print(f"Puntuación no válida. Las puntuaciones válidas son {puntuacion_valida} ")
                continue
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario. Saliendo ")
            sys.exit(0)
        except ValueError:
            print("Valor no válido.  ")
            
def get_nivel(score:float)->str:
    if score<0.4:
        return "Inaceptable"
    elif 0.4<=score<=0.6:
        return "Aceptable"
    elif score>0.6:
        return "Meritorio"
    
def historial(score:float,nivel,dinero:float):
    fecha=datetime.now().strftime("%d/%B/%y %H:%M:%S")
    archivo="Historial.csv"
    existe=os.path.isfile(archivo)
    with open(archivo,"a",newline="") as f:
        if not existe or os.stat(archivo).st_size==0:
            f.write(f"Fecha, Score, Nivel, Dinero_Recibido\n")
        f.write(f"{fecha}, {score}, {nivel}, {dinero}\n")
        
    
    

def main():
    score=get_score("Digite su puntuación por favor: ")
    nivel=get_nivel(score)
    dinero=2400*score
    print(f"Su nivel de rendimiento es {nivel}, recibirá {dinero}$")
    historial(score,nivel,dinero)
    
if __name__=="__main__":
    while True:
        main()
        rep=input("¿Quiere repetir el programa? (Y/N) ").strip().lower()
        if rep!="y":
            print("¡Adios!")
            break
    