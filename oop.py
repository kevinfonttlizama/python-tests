#---------Programacion orientada a objetos POO------------
#Object Oriented Programming OOP


#nomenclatura del punto
#esta nomenclatura sirve para acceder a las caracteristicas, atributos, valores de los datos para modificarlos, añadirlos, actualizarlos etc..

#la programacion orientada a objetos como dice su nombre es un paradigma de la programacion que se creo para reemplazar o mejorar la forma de programar a lo que era el paradigma de la programacion orientada a procesos en lenguajes antiguos como cobol o visual basic por ej.

#la programamcion orientada a objetos tiene como finalidad simular objetos de la vida real para hacer mas simple a los programadores construir programas/software basado en los comportamientos de estos objetos usando sus caracteristicas, comportamiento,aspecto etc...

class Car():
    chasisHeight=250
    chasisWidth=120
    wheels=4
    moving=False

    def carOn(self): #metodo
        self.moving=True            # <---- self hace referencia al mismo objeto podemos asimilarlo con el this de otros lenguajes de programacion
    
    def carState(self): #metodo
        if (self.moving):
            return "car is moving"
        else:
            return "car is off"

#----- Funcion vs metodo --------------------------

#diferencia entre funcion y metodo 
#Una Funcion no es exclusiva de una clase
#un Metodo es una funcion especial que pertenece a una clase 

myCar=Car()  #<---- instanciar una clase, ejemplarizar clase, crear instancia, crear objeto etc....... es lomismo

print("car height is ",myCar.chasisHeight) #<---- accediendo al valor del chasisHeight por consola lo que nos deberia devolver el valor de este, que en este caso es 250

print("this car has ", myCar.wheels ," wheels" ) #nos devuelve por consola la cadena y el valor de myCar.wheels que es 4 

myCar.carOn() #<--- encendiendo el auto, si omitimos esta parte no encenderemos el auto y la consola nos devolvera "car is off" ya que con este metodo estamos simulando que estamos encendiendo el auto, omite este metodo comentandolo y llama el metodo que tenemos a continuacion para comprobarlo.

print(myCar.carState()) # <---- estado de el auto para ver si esta encendido o apagado


#--- creando otra instancia ejemplo ------------
print("--------------------- car 2 ---------------")

myCar2 = Car()
print("car height is :", myCar2.chasisHeight)
print("this car has :", myCar2.wheels, "wheels")
print(myCar2.carState())





    
    



