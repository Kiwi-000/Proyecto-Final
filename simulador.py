import random 
import pandas as ad
from enfermedad import Enfermedad
from persona import Persona
from comunidad import Comunidad

class Simulador:
    def __init__(self, num_dias, num_personas, infeccion_probable, promedio_pasos, tasa_recuperacion):
        self.num_dias = num_dias 
        self.enfermedad = Enfermedad(infeccion_probable, promedio_pasos, tasa_recuperacion)  
        self.comunidad = Comunidad(num_personas, self.enfermedad) 
        self.resultados = [] 

    def ejecutar_simulacion(self, csv_file):
        comunidad_total = Comunidad(self.enfermedad)
        comunidad_total.leer_personas(csv_file)
        comunidad_total.infectar_aleatoriamente()

        for dia in range(1, self.num_dias + 1):
            comunidad_dia = comunidad_total.crear_comunidad_dia(random.randint(7, 30))
            self.propagacion_enfermedad(comunidad_dia)
            self.guardar_comunidad(dia, comunidad_dia)
            self.comunidades.append(comunidad_dia)

    def propagacion_enfermedad(self, comunidad):
        for persona in comunidad:
            if persona.estado == 'i':
                for otra_persona in comunidad:
                    if otra_persona.estado == 's' and random.random() < self.enfermedad.tasa_transmision:
                        otra_persona.infectar(self.enfermedad)
            persona.recuperar()

    def guardar_comunidad(self, dia, comunidad):
        suceptibles = len([p for p in comunidad if p.estado == 's'])
        infectados = len([p for p in comunidad if p.estado == 'i'])
        recuperados = len([p for p in comunidad if p.estado == 'r'])
        print(f"Día {dia}: Suceptibles={suceptibles}, Infectados={infectados}, Recuperados={recuperados}")

    def calcular_resultados(self):
        total_personas = len(self.comunidades[0])
        infectados_totales = sum(len([p for p in comunidad if p.estado == 'i']) for comunidad in self.comunidades)
        recuperados_totales = sum(len([p for p in comunidad if p.estado == 'r']) for comunidad in self.comunidades)
        tasa_transmision = infectados_totales / (total_personas * self.num_dias)
        tasa_recuperacion = recuperados_totales / infectados_totales
        return infectados_totales / total_personas, tasa_transmision, tasa_recuperacion
