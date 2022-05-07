class Clientes:
    def __init__(self, nombre, apellido, cedula, ciudad, numeroCuenta, saldo):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__cedula=cedula
        self.__ciudad=ciudad
        self.__numeroCuenta=numeroCuenta
        self.__saldo=saldo

    @property
    def nombre(self):
        return self.__nombre

    @property
    def apellido(self):
        return self.__apellido

    @property
    def cedula(self):
        return self.__cedula

    @property
    def ciudad(self):
        return self.__ciudad

    @property
    def numeroCuenta(self):
        return self.__numeroCuenta

    @property
    def saldo(self):
        return self.__saldo



    @nombre.setter
    def nombre(self, nombre):
        self.__nombre=nombre

    @apellido.setter
    def apellido(self, apellido):
        self.__apellido=apellido

    @cedula.setter
    def cedula(self, cedula):
        self.__cedula=cedula

    @ciudad.setter
    def ciudad(self, ciudad):
        self.__ciudad=ciudad

    @numeroCuenta.setter
    def numeroCuenta(self, numeroCuenta):
        self.__numeroCuenta=numeroCuenta

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo=saldo