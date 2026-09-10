class producto:
    def __init__(self,id,nombre,stock,precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock


    def aumentar_stock(self):
        self.stock +=1
        return self.stock 

    def disminuir_stock(self):
            self.stock -=1
            return self.stock 


    