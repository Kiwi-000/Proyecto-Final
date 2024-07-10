import pandas as pd
from simulador import Simulador
from enfermedad import Enfermedad

def main():
    infeccion_probable= 0.3  
    tasa_recuperacion = 0.1   

    enfermedad = Enfermedad(infeccion_probable, tasa_recuperacion)
    simulador = Simulador(num_dias=30, enfermedad=enfermedad)

if __name__ == "__main__":
    main()


















































3
