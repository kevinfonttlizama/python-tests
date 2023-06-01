#object oriented programming part 2 

#---------Programacion orientada a objetos POO------------
#Object Oriented Programming OOP

class Car():
    #constructor de python
    def __init__(self): # <------ iniciando un constructor de clase eso crearia un estado por defecto de nuestro objeto con las siguientes propiedades
        self.__chasisHeight=250
        self.__chasisWidth=120
        self.__wheels=4 #dos guiones bajos encapsula la variable esto quiere decir que esta variable solo sera accesible para la clase y no fuera de ella.
        self.__moving=False

    
    def carOn(self,powerOn): #metodo

        self.__moving=powerOn
        
        if self.__moving:
            check=self.__carCheck()

        if self.__moving and check:
            return"car is moving"
        
        elif self.__moving and check == False:
            return "something wrong"
        else: 
            return "car is off"  




    def carState(self): #method
        print("this car has",self.__wheels,"wheels, a height of ", self.__chasisHeight, "and a width of ",self.__chasisWidth)


    def __carCheck(self): #method encapsulado quiere decir que este metodo no se puede llamar a imprimir fuera de nuestra clase
        print("realizando chequeo interno")
        
        self.gas="ok"
        self.oil="ok"
        self.doors="closed"

        if self.gas=="ok" and self.oil == "ok" and self.doors == "closed" : 
            return True
        else:
            return False



myCar=Car()  #<---- instanciar una clase, ejemplarizar clase, crear instancia, crear objeto etc....... es lo mismo


myCar.carOn(True)

myCar.carState()

#--- creando otra instancia ejemplo ------------
print("--------------------- car two ---------------")

myCar2 = Car()


myCar2.carState()
myCar2.carOn(False)
myCar2.wheels=2 # <------ aunque intentemos modificar la variable esta no se vera afectada ya que la hemos encapsulado anteriormente con los dos guiones bajos que es como se hace el encapsulamiento de una variable en python, si la variable no estuviera encapsulada el valor de nuestra variable wheels cambiaria de 4 a 2 y no existe por lo que yo se un auto con dos ruedas (no lo se enserio).

# __variable <-----  esto es una variable encapsulada





