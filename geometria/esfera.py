from figura import Figura


class Esfera(Figura):

    def __init__(self, radio):
        self.radio = radio

    def calcular_volumen(self):
        return (4 / 3) * 3.1416 * self.radio ** 3