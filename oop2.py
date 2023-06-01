#object oriented programming part 2 

#---------Programacion orientada a objetos POO------------
#Object Oriented Programming OOP

class Car():
    #constructor de python
    def __init__(self): # <------ iniciando un constructor de clase eso crearia un estado por defecto de nuestro objeto con las siguientes propiedades
        self.chasisHeight=250
        self.chasisWidth=120
        self.__wheels=4 #dos guiones bajos encapsula la variable esto quiere decir que esta variable solo sera accesible para la clase y no fuera de ella.
        self.moving=False

    
    def carOn(self,powerOn): #metodo

        self.moving=powerOn
        
        
        if self.moving:
            return"car is moving"
        else: 
            return "car is off"  




    def carState(self): #method
        print("this car has",self.wheels,"wheels, a height of ", self.chasisHeight, "and a width of ",self.chasisWidth)



myCar=Car()  #<---- instanciar una clase, ejemplarizar clase, crear instancia, crear objeto etc....... es lomismo

print("car height is ",myCar.chasisHeight)
print("this car has ", myCar.wheels ," wheels" ) 

myCar.carOn(True)

print(myCar.carState())

#--- creando otra instancia ejemplo ------------
print("--------------------- car two ---------------")

myCar2 = Car()


print("car height is :", myCar2.chasisHeight)
print("this car has :", myCar2.wheels, "wheels")
myCar2.carState()
myCar2.carOn(False)

