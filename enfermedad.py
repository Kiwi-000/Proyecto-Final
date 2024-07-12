class Enfermedad:
    def __init__(self, tasa_transmision, tasa_recuperacion):
        self.tasa_transmision = tasa_transmision #La probabilidad por la que una persona suceptible se puede contagiar
        self.tasa_recuperacion = tasa_recuperacion 

    def get_tasa_transmision(self):
        return self.tasa_transmision 
    
    def get_tasa_recuperacion(self):
        return self.tasa_recuperacion
    

    
