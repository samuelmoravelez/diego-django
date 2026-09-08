class vehicle:
    def __init__(self,brand,color,plate):
        self.brand = brand
        self.color = color
        self.plate = plate
        self.speed = 0 

    def acelerar (self):
        self.speed += 10
        print(f"El vehículo {self.brand} ha acelerado a {self.speed} km/h.")

    def desacelerar (self):
        if self.speed >= 10:
            self.speed -= 10
            print(f"El vehículo {self.brand} ha desacelerado a {self.speed} km/h.")
        else:
            print(f"El vehículo {self.brand} ya está detenido.")

    


#creacion de los objetos 



mi_auto = vehicle("Toyota", "Rojo", "ABC123")

print(f"Marca: {mi_auto.brand}")
print(f"Color: {mi_auto.color}")
print(f"Placa: {mi_auto.plate}")

    
mi_auto.acelerar()
mi_auto.acelerar()
mi_auto.acelerar()
mi_auto.desacelerar()
mi_auto.desacelerar()
mi_auto.desacelerar()


#agregar el atributo placa
#agregar el metodo desacelerar
#subir a git enviar el enlace al correo


class vehicle:
    def __init__ (self, plate,color, brand): #constructor
        self.plate = plate
        self.color = color
        self.brand = brand

    def mover(self):
        print(f"el vehiculo se mueve")

class car(vehicle): #herencia 
    pass
class motorbike(bike):
    def desplegar_gato(self):
        print(f"el vehiculo {self.plate} ha desplegado el gato")


car1 = car ('666aaa','rojo', 'toyota')
car1.mover()



motorbike1 = motorbike('777bbb','azul', 'honda')
motorbike1.mover()
motorbike1.desplegar_gato()
