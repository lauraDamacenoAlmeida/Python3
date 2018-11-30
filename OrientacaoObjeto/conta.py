
class Conta:

    def __init__(self,numero,titular,saldo,agencia):
        print("construindo objeto..{}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.agencia = agencia

    def extrato(self):
        print("Conta numero: {}".format(self.numero))
        print("Saldo: {}".format(self.saldo))

    def depositar(self, valor):
        self.saldo += valor

    def saque(self, valor):

        if (self.saldo < valor):
            print("Saldo menor que o valor de saque")
            print("Saldo atual {}".format(self.saldo))

        else:
            self.saldo -= valor