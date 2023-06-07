class Persona():
    def __init__(self, nombre, edad, lugar_residencia):

        self.nombre=nombre
        self.edad=edad
        self.lugar_residencia=lugar_residencia


    def descripcion(self):

        print("nombre: ",self.nombre," Edad: ",self.edad, " Residencia: ",self.lugar_residencia)


class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
        super().__init__(nombre_empleado,edad_empleado,residencia_empleado)

        self.salario=salario

        self.antiguedad=antiguedad

    def descripcion(self):
        super().descripcion()
        print("salario: ",self.salario,"Antiguedad: ",self.antiguedad)


Kevin = Empleado (1200, 1, "Kevin", 22, "Santiago")

Kevin.descripcion()
print(isinstance(Kevin,Empleado))