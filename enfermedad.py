class Enfermedad:
    def __init__(self, tasa_transmision, tasa_recuperacion):
        #probabilidad de contagio
        self.tasa_transmision = tasa_transmision
        #cuantos dias va a estar enfermo hasta que se recupere
        self.tasa_recuperacion = tasa_recuperacion

    #get
    def get_tasa_transmision(self):
        return self.tasa_transmision 
    
    def get_tasa_recuperacion(self):
        return self.tasa_recuperacion
    

    #set
    
