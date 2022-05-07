from pydoc import cli
from clases.Clientes import Clientes

def hacerTramiteBancario():
    cliente=Clientes("nombre", "apellido", "cedula", "ciudad", "numeroCuenta", "saldo")

    nombre=input("Ingrese el nombre: ")
    apellido=input("Ingrese el apellido: ")
    cedula=input("Ingrese la cedula: ")
    ciudad=input("Ingrese el ciudad: ")
    numeroCuenta=input("Ingrese el numero de cuenta: ")
    saldo=int(input("Ingrese el saldo: "))

    cliente.nombre=nombre
    cliente.apellido=apellido
    cliente.cedula=cedula
    cliente.ciudad=ciudad
    cliente.numeroCuenta=numeroCuenta
    cliente.saldo=saldo

    i=input("Ingrese 1 para consultar saldo")
    if(i=="1"):
        print(cliente.saldo)
        e=input("Ingrese 1 para consignar o 2 para retirar")
        if(i=="1"):
            cantidad=int(input("Ingrese la cantidad a consignar: "))
            cliente.saldo=cliente.saldo+cantidad
            print(f"La cantidad final es: {cliente.saldo} ")
        elif(i=="2"):
            cantidad=int(input("Ingrese la cantidad a consignar: "))
            cliente.saldo=cliente.saldo-cantidad
            print(f"La cantidad final es: {cliente.saldo} ")

    
hacerTramiteBancario()