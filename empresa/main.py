import administrativo


def main():
    admin = administrativo.administrativo("Juan", "123456789", 5000)
    admin.mostrar_informacion()

    print (administrativo)

    print(admin.salario)

    desarrollador = desarrollador('ana',6400,1100,'chatear')
    print (desarrollador)
    print (desarrollador.calcular_bonificacion())

    gerente = gerente('robert',2400,3100)
    print (gerente)
    print (gerente.calcular_bonificacion())

if __name__ == "__main__":
    main()