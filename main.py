import pandas as pd
from simulador import Simulador
from enfermedad import Enfermedad

def main():
    tasa_transmision= 0.3  
    tasa_recuperacion = 5

    covid = Enfermedad(tasa_transmision, tasa_recuperacion)

    simulador = Simulador(num_dias=50, enfermedad=covid)

    simulador.ejecutar_simulacion()

if __name__ == "__main__":
    main()
  
  


