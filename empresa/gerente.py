from empleado import Empleado


class gerente(Empleado):
    def calcular_bonificacion(self):
        return self.salario * 0.20