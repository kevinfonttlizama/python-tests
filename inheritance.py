#herencias en python 


class Vehiculos(): # definiendo la clase <----

    def __init__(self, marca, modelo): #<--- constructor
        
        self.marca=marca
        self.modelo=modelo
        self.enMarcha=False
        self.acelera=False
        self.frena=False


    def arrancar(self):

            self.enMarcha=True  

    def acelerar(self):
            self.acelera=True

    def frenar(self):
            self.frena=True

    def estado(self):
        print("Marca:", self.marca, "\nModelo: ", self.modelo,"\nEn Marcha: ", self.enMarcha, "\nAcelerando: ",self.acelera,"\nFrenando: ", self.frena)  




class Moto(Vehiculos):
    hCaballito=""
    def caballito(self):
          self.hCaballito="Voy haciendo el caballito"
          
          
    def estado(self):
        print("Marca:", self.marca, "\nModelo: ", self.modelo,"\nEn Marcha: ", self.enMarcha, "\nAcelerando: ",self.acelera,"\nFrenando: ", self.frena, "\n",self.hCaballito)



class VElectricos(Vehiculos):
        def __init__(self, marca, modelo):
            
                super().__init__(marca ,modelo)

                self.autonomia=100

        def cargarEnergia(self):
            
                self.cargando=True


miMoto=Moto("Honda","CBR")

miMoto.caballito()

miMoto.estado()

    