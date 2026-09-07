

from empleado import Empleado


class administrativo (Empleado):
    def calcular_bonificacion(self):
        return self.salario * 0.10
    
        