class Producto:

    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def calcular_descuento(self):

        if self.cantidad <= 0:
            return "La cantidad no puede ser 0 o negativa"

        elif self.cantidad < 10:
            descuento = 0.05

        elif self.cantidad < 49:
            descuento = 0.10

        else:
            descuento = 0.125

        valor_descuento = self.precio * descuento
        precio_final = self.precio - valor_descuento

        return precio_final



producto1 = Producto(1, "Camisa", 5, 110000)
producto2 = Producto(2, "Pantalon", 20, 100000)



print("Producto:", producto1.nombre)
print("Precio final:", producto1.calcular_descuento())

print()

print("Producto:", producto2.nombre)
print("Precio final:", producto2.calcular_descuento())