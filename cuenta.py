class cuenta: 
    def __init__(self,numero,saldo):
        self.numero = numero
        self.__saldo = saldo
        self.__retiro = 0

    def depositar(self,cantidad):
        if cantidad > 0:
            self.__saldo += cantidad 


    def retirar (self,cantidad):
        if cantidad > self.__saldo:
            print("Saldo insuficiente")
        elif cantidad > 0: 
            self.__saldo -= cantidad

    def obtener_saldo(self):
        return self.__saldo
#creacion del objeto 


cuenta1 = cuenta(1111, 1000)

print (f"Numero de cuenta: {cuenta1.numero}")
print (f"Saldo inicial de la cuenta: {cuenta1.obtener_saldo()}")

cuenta1.retirar(300)
print (f"saldo despues de retirar 300: ${cuenta1.obtener_saldo()}")
    
cuenta1.retirar(1000)
print(f"Saldo actual: ${cuenta1.obtener_saldo()}")