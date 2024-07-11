import pandas as pd
from simulador import Simulador
from enfermedad import Enfermedad

def main():
    num_dias = 30
    tasa_transmision= 0.3  
    tasa_recuperacion = 5

    #def __init__(self, num_dias, tasa_transmision, promedio_pasos, tasa_recuperacion):
    covid = Enfermedad(tasa_transmision, tasa_recuperacion)

    simulador = Simulador(num_dias=30, enfermedad=covid)

    simulador.ejecutar_simulacion()

if __name__ == "__main__":
    main()
  


















































3
