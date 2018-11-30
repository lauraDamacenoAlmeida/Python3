
class Conta:

    def __init__(self,numero,titular,saldo,agencia):
        print("construindo objeto..{}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.agencia = agencia