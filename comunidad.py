import random
import pandas as pd
from persona import Persona

class Comunidad:
    def __init__(self, enfermedad):
        self.enfermedad = enfermedad
        self.personas = self.leer_personas('personas.csv')

#-----------------------------------------------------------------------------------------------------------------------------------
    #crear personas

    def leer_personas(self, csv_file):
        df = pd.read_csv(csv_file)

        personas = []
        for index, row in df.iterrows():
            persona = Persona(row['id'], row['nombre'], row['apellido'], row["estado"])
            personas.append(persona)

        #se infecta persona del arreglo personas
        personas = self.infectar_aleatoriamente(1, personas) #se puede cambiar la cantidad de personas a infectar
        return personas

#-----------------------------------------------------------------------------------------------------------------------------------
    #metodo para infectar personas

    def infectar_aleatoriamente(self, num_personas, personas):
        #se agarra la cantidad de num_personas de las 500 en personas
        personas_infectadas = random.sample(personas, num_personas)
        for persona in personas_infectadas:
            print(persona.id) #imprimir id de la persona elegida
            persona.infectar(self.enfermedad)
        return personas

    #metodo para crear una sub comunidad

    def crear_comunidad_dia(self, num_personas):
        return random.sample(self.personas, num_personas)
    
    
