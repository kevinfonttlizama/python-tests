#bienvenido a mi guia personalizada de python en esta guia estan mis estudios personales de este lenguaje de programacion si te sirve de ayuda puedes ocuparlo para aprender y estudiar este mismo, gracias por leerlo y que te diviertas aprendiendo!

# esta guia no es para principiantes desde 0, por lo que hay algunas cosas que no entenderas si no conoces algun lenguaje de programacion, tengo contemplado subir una guia desde 0 pero este no es el caso ya que es una guia de estudios y investigaciones mia para autoaprendizaje continuo intentare detallar cada cosa para que sea entendible tanto para mi como para alguien que vaya a leer esto en algun momento.


#------------------- tipos de datos -----------------

#str = string ej: ----> cadena = "hello world" (las comillas van incluidas en el string o cadena de texto "hello world")
#int = numero ej: ----> numero = 1,2,3,4,5,2134,45,4344534 etc...
#float numeros decimales ----> numeroDecimal = 2.4 , 2.2 , 0.1 , 100.2 , 0.05 etc... 

# ------------------ Funciones ----------------------


#funcion simple de python para sumar dos numeros y
#imprimirlos en consola

def suma(a,b):
    print(a + b)

 # suma(5,6)

#funcion con condicional if para calcular nota de aprobacion en la educacion chilena
#pd la nota minina para aprobar en chile es un 4.0 
#la escala va desde el 1.0 nota minima a 7.0 nota maxima

#def promedioEstudiantil(calificacion):
    

    #if calificacion >= 4.0:
    #    print(valoracion)

    #else: 
    #    valoracion="reprueba"
    #    print(valoracion)



#llamar o usar funcion

# promedioEstudiantil(4.0) <-- Aprueba
# promedioEstudiantil(3.9) <-- Reprueba


# nota_alumno=int(input("introduce una nota :  "))

# def evaluacionInput(nota):
#     valoracion="aprueba"
#     if nota >= 4:
#         return(valoracion)
#     else:
#         valoracion="reprueba"
#         return(valoracion)



# print(evaluacionInput(int(nota_alumno)))  <--- aca le estamos especificando que el dato que le estamos dando al input cuando se ejecuta la funcion es de tipo entero ---->(int)<----

# las variables de una funcion solo funcionan cuando estas han sido declaradas dentro de la misma

# --- operadores logicos

# and ----- or ------ in 

# def soyMillonario():
#     empresas=int(input("introduce cuantas empresas tienes  :"))
#     patrimonio=int(input("Introduce tu patrimonio   :"))
#     resultado="eres millonario"
#     if empresas > 0 and patrimonio > 1000000:
#         print(resultado)

#     else:
#         resultado="no eres millonario"
#         print(resultado)

# soyMillonario()


# ----- bucles for -------

# email=False

# for i in "kevin.andresfontt@gmail.com":

#     if i == "@":
#         email=True


# if email:
#     print("el email es correcto")
# else:
#     print("el email es incorrecto")


# esto hace que i recorra cada caracter de nuestro string y si nuestra variable i coincide con nuestra cadena se le da el valor de verdadero a la variable email que esta declarada en false 


#metodo continue

# nombre = "arthas el caballero de la muerte"
# count = 0
# for i in nombre:
#     if i == " ":
#         continue
#     count+= 1
#     print(count)


#este metodo lo que hace es continuar como dice la palabra, en esta funcion usamos el metodo continue para ignorar los espacios de el valor de la variable nombre   
# 
# ---------- Generadores python -------------------  

# def generaPares(limite):
#     num= 1
#     while num < limite:
#         yield num*2 
#         num=num+1
    
# numerosPares = generaPares(10)

# for i in numerosPares:
#     print(i)

# def devuelve_ciudades(*ciudades):
#     for elemento in ciudades:
#         yield elemento

# ciudades_devueltas=devuelve_ciudades("Santiago","Madrid","Moscu","Berlin")

# print(next(ciudades_devueltas))
# print(next(ciudades_devueltas))


# el asterisco ----> * <----- de la funcion especifica que podemos darles los argumentos que queramos a la funcion es decir esta funcion no espera una cantidad especifica de parametros y podemos darle todos los parametros que queramos 
#el metodo next imprime el primer dato del objeto iterable y asi consecutivamente en el orden cada vez que se llame.
        

#-------------- Exceptions de python ----------------

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        print("zero cannot be divided")
        return("invalid operation")

while True:
    try:
        option1= (int(input("enter the first number:  ")))
        option2= (int(input("enter the second number:  ")))
        break
    except ValueError:
        print("invalid value")
        
        

operation=input("select one of the following operations methods  (add,subtract,multiply,divide)")


if operation == "add":
    print (add(option1,option2))
elif operation == "subtract":
    print(subtract(option1,option2))
elif operation == "multiply":
    print(multiply(option1,option2))
elif operation == "divide":
    print(divide(option1,option2))
else:
    print("invalid method")




# ------------- Diccionario en python ---------------

diccionarioPaises = {

    "Chile":"Santiago",
    "Estados Unidos":"Washington",
    "Francia":"Paris",
    "Brasil":"Brasilia",
    "Peru":"Lima",
    "Bolivia":"La Paz",
    "Argentina":"El cairo",
    "Pizza":"Napolitana"
}

#El cairo es la capital de egipto, no de argentina
# por lo tanto para sobreescribir este valor por el valor correcto usamos el siguiente metodo

diccionarioPaises["Argentina"]="Buenos Aires"

#ahora si imprimimos por consola Argentina tendra el valor Correcto de la Capital que en este caso es Buenos aires y NO El Cairo

#para borrar un elemento del diccionario de paises usamos el metodo ---> del <--- y especificamos el valor

del diccionarioPaises["Pizza"]

# print(diccionarioPaises)

#diccionario pero con valores distintos


diccionarioDiverso= {

    "pizzas":3,
    "completos":10,
    "sopaipillas":30,
    20:"años",
    "fideos con carne":{"ingredientes":["paquete de fideos","salsa de tomates","cebolla picada","zanahoria rallada","carne molida"]}

}

#el diccionario de arriba incluye una receta de fideos con carne por lo cual tenemos una lista dentro del diccionario 


#lista python (mutable)

miLista=["Fideos","Arroz","Manzana","Naranja"]

#tupla python (inmutable)

miTupla=("hola",123,"queso")


# print(diccionarioDiverso["fideos con carne"])
#imprime la lista dentro de el diccionario

# print(diccionarioDiverso) <--- imprime el diccionario completo

# print(diccionarioDiverso.keys()) <-- imprime las llaves del diccionario por ejemplo "pizzas"

# print(diccionarioDiverso.values) <--- imprime los valores del diccionario ejemplo 10

# print(len(diccionarioDiverso)) <-- imprime cuantos objetos tenemos dentro del diccionario

#continuacion de la guia en el archivo tests.py