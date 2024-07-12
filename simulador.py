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

    #Ejecutar la simulacion de propagacion 
    def ejecutar_simulacion(self):

        for dia in range(1, self.num_dias):
            comunidad_dia = self.comunidad.crear_comunidad_dia(50) #Crear sub comunidades

            #Funciones que deben iterar sobre cada dia
            self.propagacion_enfermedad(comunidad_dia)
            self.recuperar_persona(self.comunidad.personas)
            self.guardar_comunidad(dia, self.comunidad.personas)

            for persona in self.comunidad.personas:
                if persona.estado == "i":
                    persona.contador += 1

        print("\n Datos finales de la simulacion\n")
    
        for persona in self.comunidad.personas:
            print(f"{persona.id} ~ {persona.nombre} ~ {persona.estado} ~ {persona.contador}")

        self.calcular_suceptibles_totales()
        self.calcular_infectados_totales()
        self.calcular_recuperados_totales()



    #Propagar enfermedad en la comunidad del dia
    def propagacion_enfermedad(self, comunidad_dia):
        for persona in comunidad_dia:
            if persona.estado == 'i':
                for otra_persona in comunidad_dia:                          
                    if otra_persona.estado == 's' and random.random() < self.enfermedad.tasa_transmision:
                        otra_persona.infectar(self.enfermedad)
    
    # Recuperacion de las personas 
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
        return suceptibles, infectados , recuperados

#____________________________________________________________________________________________________________________________
    #Porcentajes finales de toda la comunidad

    # calcular preomedio recuperados en toda la simulasion 
    def calcular_suceptibles_totales(self):
        total_personas = len(self.comunidad.personas)
        suceptibles_totales = 0

        for persona in self.comunidad.personas:
            if persona.estado == "s":
                suceptibles_totales += 1

        porcentaje_suceptible = (suceptibles_totales / total_personas) * 100
        print (f"El {porcentaje_suceptible} % nunca se enfermo")    

        return porcentaje_suceptible


    # calcular promedio infectados en toda la simulacion 
    def calcular_infectados_totales(self):
        total_personas = len(self.comunidad.personas)
        infectados_totales = 0

        for persona in self.comunidad.personas:
            if persona.estado == "i":
                infectados_totales += 1

        porcentaje_infectados = (infectados_totales / total_personas)* 100
        print (f"Quedaron enfermos el {porcentaje_infectados} %")

        return porcentaje_infectados


    # calcular preomedio recuperados en toda la simulasion 
    def calcular_recuperados_totales(self):
        total_personas = len(self.comunidad.personas)
        recuperados_totales = 0

        for persona in self.comunidad.personas:
            if persona.estado == "r":
                recuperados_totales += 1

        porcentaje_recuperadas = (recuperados_totales / total_personas)* 100
        print (f"Está recuperado el {porcentaje_recuperadas}%")    

        return porcentaje_recuperadas



