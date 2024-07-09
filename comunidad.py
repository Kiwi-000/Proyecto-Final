import random
import pandas as pd

class Comunidad:
    def __init__(self, num_persona, enfermedad, probabilidad_conexion):
        self.num_persona = num_persona
        self.enfermedad = enfermedad
        self.probabilidad_conexion= probabilidad_conexion

    #generar numero de personas dentro de una comunidad, deberias ser de 7 a 30 por dia 

    #def crear_persona(self):
        #df_nombres = pd.read_csv("personas.csv")
        #persona = []
        #for i in range(self.num_persona):
            #fila = df_nombres.sample()
            #nombre = fila['nombre'].values[0]
            #apellido = fila['apellido'].values[0]
            #persona.append(Persona(i, nombre, apellido, self))
        #return persona

