from abc import ABC, abstractmethod


class Figura(ABC):

    @abstractmethod
    def calcular_volumen(self):
        pass