import random

class Persona:
    def __init__(self, id, nombre, apellido, estado):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.estado = estado
        self.contador = 0

    # get
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido

    def get_estado(self):
        return self.estado

    # Cambia el estado a infectado
    def infectar(self, enfermedad):
        if self.estado == 's':
            self.enfermedad = enfermedad
            self.estado = 'i'

    # Cambia el estado a recuperado
    def recuperar(self):
            self.estado = 'r'
            self.enfermedad = None
