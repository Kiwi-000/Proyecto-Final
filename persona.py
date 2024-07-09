import random

class Persona:
    def __init__(self, id, nombre, apellido, comunidad):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.comunidad = comunidad
        self.estado = 's'  # susceptible (s), infectado (i), recuperado (r)

    # Métodos get para los atributos
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido

    def get_comunidad(self):
        return self.comunidad

    def get_estado(self):
        return self.estado

    def get_enfermedad(self):
        return self.enfermedad

    # Cambia el estado a infectado
    def infectar(self, enfermedad):
        if self.estado == 's':
            self.enfermedad = enfermedad
            self.estado = 'i'

    # Cambia el estado a recuperado
    def recuperar(self):
        if self.estado == 'i' and random.random() < self.enfermedad.tasa_recuperacion:
            self.estado = 'r'
            self.enfermedad = None