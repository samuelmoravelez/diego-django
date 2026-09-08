class Figura:
    def __init__(self, largo):
        self.largo = largo


class Circulo(Figura):

    def calcular_area(self):
        return 3.1416 * self.largo ** 2

    def calcular_perimetro(self):
        return 2 * 3.1416 * self.largo


class Cuadrado(Figura):

    def calcular_area(self):
        return self.largo ** 2

    def calcular_perimetro(self):
        return 4 * self.largo


circulo = Circulo(5)

print("Área del círculo:", circulo.calcular_area())
print("Perímetro del círculo:", circulo.calcular_perimetro())

cuadrado = Cuadrado(5)

print("Área del cuadrado:", cuadrado.calcular_area())
print("Perímetro del cuadrado:", cuadrado.calcular_perimetro())