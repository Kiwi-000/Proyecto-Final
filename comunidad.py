import random
import pandas as pd
from persona import Persona

class Comunidad:
    def __init__(self, enfermedad):
        self.personas = []
        self.enfermedad = enfermedad

    def leer_personas(self, csv_file):
        df = pd.read_csv(csv_file)
        for i, row in df.iterrows():
            persona = Persona(i, row['nombre'], row['apellido'])
            self.personas.append(persona)

    def infectar_aleatoriamente(self, num_infectados):
        for _ in range(num_infectados):
            persona = random.choice(self.personas)
            persona.infectar(self.enfermedad)

    def crear_comunidad_dia(self, num_personas):
        return random.sample(self.personas, num_personas)

