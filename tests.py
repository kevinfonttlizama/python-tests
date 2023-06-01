import math # <--- importando una libreria en este caso math

#exceptions parte 2 ya que no queria hacer un documento mas largo solo eso, por eso este otro archivo

#function divide con dos Exceptions 

# def divide():
#     try:
#         option1=(float(input("Enter the first number:   ")))
#         option2=(float(input("Enter the second number:   ")))
    
#         print("the division is: " + str(option1/option2))

#     except ValueError:
#         print("incorrect values")

#     except ZeroDivisionError:
#         print("cannot divide zero!")

#     finally:
#         print("finished")

# divide()

#finally siempre se ejecuta aunque no tengamos definidas excepciones pero si hay un try sin except nos dara un error de sintaxis.
#finally es un bloque de codigo que se ejecuta despues de las excepciones, siempre se ejecuta si o si.


def evaluaEdad(edad):

    if edad < 0:
        raise TypeError("Una edad de valor negativa no tiene sentido...")
    #raise sirve para personalizar un mensaje de error
    if edad > 20:
        return "Eres muy joven"
    
    elif edad > 40:
        return "Eres joven"
    
    elif edad < 65: 
        return "Eres maduro"
    
    elif edad < 100:
        return "debes cuidarte..."
    

# print(evaluaEdad(-3))


def raizCuadrada(value):
    if value < 0:
        raise ValueError ("the number cannot be negative")
    else:
        return math.sqrt(value)
    

option1=(int(input("introduce un numero :")))
try:
    print(raizCuadrada(option1))
except ValueError as NegativeNumber:
#as NegativeNumber nos sirve como variable para definir nuestro error personalizado y la podemos usar en el siguiente ejemplo
    print(NegativeNumber)
#NegativeNumber tiene el valor de la cadena de "the number cannot be negative" y eso es lo que nos saldra en consola cuando nos salte el error que estamos capturando.

print("finished")






