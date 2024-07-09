import random #aleatoriedad en infectado y conexion
import pandas as ad
from persona import Persona
from comunidad import Comunidad

class Simulador:
    def __init__(self, num_dias):
        self.num_dias = num_dias
        self.comunidades = []

    #Lee archico CSV y crea personas de una comunidad
    #def crear_persona(self):
        #df_nombres = pd.read_csv("personas.csv")
        #persona = []
        #for i in range(self.num_persona):
            #fila = df_nombres.sample()
            #nombre = fila['nombre'].values[0]
            #apellido = fila['apellido'].values[0]
            #persona.append(Persona(i, nombre, apellido, self))
        #return persona
     
     

    # analizar comunidad y ejecutar simulacion, con el paso de los dias.
    def ejecutar_simulacion(self, csv_file):
        comunidad_total = Comunidad()
        comunidad_total.leer_personas(csv_file)
        comunidad_total.infectar_aleatoriamente(1)  # Infectar aleatoriamente a una persona el primer día

        for dia in range(1, self.num_dias + 1):
            comunidad_dia = comunidad_total.crear_comunidad_dia(random.randint(7, 30))
            self.propagacion_enfermedad(comunidad_dia)
            self.guardar_comunidad(dia, comunidad_dia)
            self.comunidades.append(comunidad_dia)

    def propagacion_enfermedad(self, comunidad):
        for persona in comunidad:
            if persona.estado == 'i':    
                for otra_persona in comunidad: # O implementar funcion infectar() de persona 
                    if otra_persona.estado == 's' and random.random() < self.enfermedad.infeccion_probable:
                        otra_persona.infectar(self.enfermedad)
            persona.recuperar()

    def guardar_comunidad():
        pass

    #guardar datos y analisis