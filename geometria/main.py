"""el volumen de un cilindro, esfera y cubo
    aplicar herencia,polimorfismo, abstraccion 
    crear objetos. crear una clase para un cilindro otrra para esfera y otro 
    para cubo


    cargar proyecto a git  """


from cilindro import Cilindro
from esfera import Esfera
from cubo import Cubo


cilindro = Cilindro(5, 10)
esfera = Esfera(5)
cubo = Cubo(5)


figuras = [cilindro, esfera, cubo]

for figura in figuras:
    print("Volumen:", figura.calcular_volumen())