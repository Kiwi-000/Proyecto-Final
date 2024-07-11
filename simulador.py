import random 
from comunidad import Comunidad

class Simulador:
    def __init__(self, num_dias, enfermedad):
        self.num_dias = num_dias 
        self.comunidad = Comunidad(enfermedad) 
        self.resultados = [] 

    #iniciar la simulacion de propagacion 
    def ejecutar_simulacion(self):
        
        for dia in range(1, self.num_dias):
            comunidad_dia = self.comunidad.crear_comunidad_dia(100)

            for persona in comunidad_dia:
                print(persona.id)

            print("")

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
        return infectados_totales / total_personas
