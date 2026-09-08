from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self,nombre,documento,salario):
        self.nombre = nombre #atributo
        self.documento = documento  #atributo
        self.__salario = salario #atributo


    @abstractmethod
    def calcular_bonificacion(self):
        pass 

    @property #accediendo a un atributo privado
    def salario(self):
        return self.__salario


    def mostrar_informacion(self): #metodo
        print(f"Nombre: {self.nombre}")
        print(f"Documento: {self.documento}")
        print(f"Salario: {self.salario:.0f}")



    
    def __str__(self): #metodo
        return f"Nombre: {self.nombre}, Documento: {self.documento}, Salario: {self.salario:.0f}"


    