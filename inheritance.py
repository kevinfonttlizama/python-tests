#herencias en python 


class Vehiculos():

    def __init__(self, marca, modelo): #<--- constructor
        
        self.marca=marca
        self.modelo=modelo
        self.enMarcha=False
        self.acelera=False
        self.frena=False


        def arrancar(self):

            self.enmarcha=True  

        def acelerar(self):
            self.acelera=True

        def frenar(self):
            self.frena=True


        def estado(self):
            print("Marca;", self.marca, "\nModelo:", self.modelo)