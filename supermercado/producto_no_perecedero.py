from producto import Producto


class Producto_no_perecedero(Producto):
    def __init__(self,id,nombre,precio,stock,fecha_vencimiento):
        super().__init__(id,nombre,precio,stock)
        self.fecha_vencimiento = fecha_vencimiento

        