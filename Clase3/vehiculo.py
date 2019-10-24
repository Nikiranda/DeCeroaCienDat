import os
import sys

class Vehiculo(object):
    def __init__(self):
        print("instanciando vehiculo")
        self.numdellantas = 0
        self.mensaje = ""

    def set_numdellantas(self, nodellantas):
        self.numdellantas = nodellantas
        print("Numero de llantas setteado con exito")

    def set_muevete(self, mensaje):
        self.mensaje = mensaje
        print("Mensaje seteado con exito")

    def get_numdellantas(self):
        print(self.numdellantas)

    def get_muevete(self):
        print(self.mensaje)
