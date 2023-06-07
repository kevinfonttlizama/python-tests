class Auto():

    def desplazamiento(self):
        print("Me desplazo usando cuatro ruedas")


class Moto():

    def desplazamiento(self):
        print("me desplazo usando dos ruedas")


class Camion():

    def desplazamiento(self):
        print("me desplazo usando seis ruedas")


miVehiculo=Moto()
miVehiculo.desplazamiento() #mismo metodo

miVehiculo2=Auto()
miVehiculo2.desplazamiento() #mismo metodo diferente descripcion

miVehiculo3=Camion()
miVehiculo3.desplazamiento()

#----------- polimorfismo -----------------------

def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()



miVehiculo4=Auto() #si cambiamos el tipo de objeto o clase se transformara y llamara al metodo respectivo de cada clase por ejemplo todos los metodos se llaman de la misma forma que es desplazamiento y imprimen un mensaje correspondiente segun el tipo de vehiculo que sean (auto,moto,camion)

desplazamientoVehiculo(miVehiculo4)
#por lo tanto si llamamos a este metodo  