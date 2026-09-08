


from empleado import Empleado 


class desarrollador(Empleado):
    def __init__(self,nombre,documento,salario,lenguajes_programacion):
        super().__init__(nombre,documento,salario)
        self.lenguajes_programacion = lenguajes_programacion
    def calcular_bonificacion(self):
        return self.salario * 0.15


    def __str__(self):
        return f"Desarrollador: {self.nombre}, Documento: {self.documento}, Salario: {self.salario:.0f}, Lenguajes de Programación: {self.lenguajes_programacion}"



""" realizar un programa orientado a objetos que permitar calcular 
    el volumen de un cilindro, esfera y cubo
    aplicar herencia,polimorfismo, abstraccion 
    crear objetos. crear una clase para un cilindro otrra para esfera y otro 
    para cubo


    cargar proyecto a git  """