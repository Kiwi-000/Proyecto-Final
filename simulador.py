import random 
from persona import Persona
from comunidad import Comunidad
from enfermedad import Enfermedad

class Simulador:
    def __init__(self, num_dias, enfermedad):
        self.num_dias = num_dias 
        self.comunidad = Comunidad(enfermedad) 
        self.enfermedad = enfermedad
        self.resultados = [] 

    #iniciar la simulacion de propagacion 
    def ejecutar_simulacion(self):

        for dia in range(1, self.num_dias):
            comunidad_dia = self.comunidad.crear_comunidad_dia(50)

            self.propagacion_enfermedad(comunidad_dia)
            self.recuperar_persona(self.comunidad.personas)
            self.guardar_comunidad(dia, self.comunidad.personas)

            for persona in comunidad_dia:
                #print(persona.id, persona.estado)
                if persona.estado == "i":
                    persona.contador += 1
                    #print( persona.contador, persona.id )

        print("\n Datos finales de la simulacion\n")
    
        for persona in self.comunidad.personas:
            print(f"{persona.id} ~ {persona.estado} ~ {persona.contador} ~ {persona.nombre}")



    #Propagar gente 
    def propagacion_enfermedad(self, comunidad_dia):
        for persona in comunidad_dia:
            if persona.estado == 'i':
                for otra_persona in comunidad_dia:
                    if otra_persona.estado == 's' and random.random() < self.enfermedad.tasa_transmision:
                        otra_persona.infectar(self.enfermedad)
    


    #tratar de recuperar gente 
    def recuperar_persona(self, comunidad):
        for persona in comunidad:
            if persona.estado == 'i':
                if persona.contador == 5 :  #dias que la persona pasa enferma
                    persona.recuperar()



    #funcion para cada día muestra los suceptibles, infectados y recuperados por dia
    def guardar_comunidad(self, dia, comunidad):
        suceptibles = len([p for p in comunidad if p.estado == 's'])
        infectados = len([p for p in comunidad if p.estado == 'i'])
        recuperados = len([p for p in comunidad if p.estado == 'r'])
        print(f"Día {dia}: Suceptibles={suceptibles}, Infectados={infectados}, Recuperados={recuperados}")



    # calcular promedio infectados en toda la simulacion 
    def calcular_infectados_totales(self):
        total_personas = len(self.comunidad[0])
        infectados_totales = sum(len([p for p in comunidad if p.estado == 'i']) for comunidad in self.comunidad)
        return infectados_totales / total_personas



    # calcular preomedio recuperados en toda la simulasion 
    def calcular_recuperados_totales(self):
        total_personas = len(self.comunidad[0])
        recuperados_totales = sum(len([p for p in comunidad if p.estado == 's']) for comunidad in self.comunidad)
        return recuperados_totales / total_personas
    
    def calcular_resultados(self):
        total_personas = len(self.comunidades[0])
        infectados_totales = sum(len([p for p in comunidad if p.estado == 'i']) for comunidad in self.comunidades)
        recuperados_totales = sum(len([p for p in comunidad if p.estado == 'r']) for comunidad in self.comunidades)
        return infectados_totales / total_personas
