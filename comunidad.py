import random
import pandas as pd
from persona import Persona

class Comunidad:
    def __init__(self, enfermedad):
        self.enfermedad = enfermedad
        self.personas = self.leer_personas('personas.csv')

    def leer_personas(self, csv_file):
        df = pd.read_csv(csv_file)
        print("~~~~~~~~~")

        #nota: usar numpy en este arreglo ~ chatgpts
        personas = []
        for index, row in df.iterrows():
            persona = Persona(row['id'], row['nombre'], row['apellido'], row["estado"])
            personas.append(persona)

        #se escoge una persona al azar para enfermarla
        personas = self.infectar_aleatoriamente(1, personas)
        print("\nSe crearon correctamente 500 personas")

        #se imprimen las personas
        i = 0
        for persona in personas:
            print(f"{persona.id} ~ {persona.nombre} ~ {persona.estado}")
            i += 1
        
        return personas

    def infectar_aleatoriamente(self, num_personas, personas):
        #se agarra la cantidad de num_personas de las 500 en personas
        personas_infectadas = random.sample(personas, num_personas)

        for persona in personas_infectadas:
            print(persona.id)
            persona.infectar(self.enfermedad)

        return personas

    def crear_comunidad_dia(self, num_personas):
        return random.sample(self.personas, num_personas)
    
#talca = Comunidad("enfermedad")
