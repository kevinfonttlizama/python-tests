
# ----------------------- clase del objeto  ------------------------------------------------------------------------------------------

class Vehiculo():

    
# ......................... connstructor de la clase que define el estado inicial de un objeto .........................................
    def __init__(self):
       
        self.color="color"
        self.marca="marca"
        self.precioNormal=0
        self.precioConDescuento=0
        self.descuentos=0
        self.codigo="codigo"
        self.fechasCompatibles=["2023","2024","2025","2028"]
        self.codigoscompatibles=["1234","4321","admin"]

    # --------------- metodos para cambiar los valores del objeto o la instancia que estamos creando 


    # -------- cambia el color del auto ------------------------
    def definirColor(self):
        self.color=input("ingrese un color: ")
        return "color", self.color ,"agregado"

# .......................... define la marca del auto -----------------------------------
    def definirMarca(self):
        self.marca=input("ingrese una marca: ")
        return  "la marca del vehiculo es: ",self.marca

# -------------------------------- establece el precio del auto -----------------------------------------------
    def definirPrecio(self):
        self.precioNormal=int(input("ingrese el precio del vehiculo: "))
        return "el precio normal del vehiculo es: ", self.precioNormal

# ------------------------- establece si el cliente tiene un descuento de un vehiculo si existe una fecha compatible o un codigo compatible que se consulta en una lista con valores de fecha y otra lista con valores de codigo si una de estas cumple la condicion se genera un descuento y se imprime por consola el descuento con el precio descontado, si no se imprime un mensaje por consola que el descuento no aplica en el caso especifico
    def descuentoVip(self):
        self.codigo=input("ingrese su codigo: ")
        self.fecha=input("ingrese una fecha: ")
        if self.codigo in self.codigoscompatibles and self.fecha in self.fechasCompatibles:
            self.precioNormal=self.precioNormal
            self.precioConDescuento = self.precioNormal - self.descuentos
            return("descuento aplicado, el precio final es de :",self.precioConDescuento)
        else:
            return("no aplica para un descuento")


# -------------------------- definimos el monto del descuento --------------------------------------------------------
    def descuento(self):
        self.descuentos=int(input("ingrese el total de su descuento: "))
        return "el descuento a aplicar es de: ", self.descuentos


myVehiculo=Vehiculo()  #<----------- crea una instancia de vehiculo myVehiculo = new Vehiculo (color,marca-modelo,precio,decuento etc...)

# myVehiculo.descuento(300000)
# myVehiculo.definirColor("rojo")
# myVehiculo.definirMarca("jeep")
# myVehiculo.definirPrecio(1000000) <------ llamando metodos sin inputs y pasando valores a los metodos de manera manual
# myVehiculo.descuentoVip(,"2028")



# print("my vehiculo es de color",myVehiculo.color)
# print("my vehiculo es de la marca ", myVehiculo.marca)  <----- metodos manuales
# print("este vehiculo tiene un precio normal de ", myVehiculo.precioNormal) 

# print(myVehiculo.definirColor())
# print(myVehiculo.definirMarca())
# print(myVehiculo.descuento())
# print(myVehiculo.definirPrecio()) #<---------------- cambiando parametros con inputs
# print(myVehiculo.descuentoVip())



