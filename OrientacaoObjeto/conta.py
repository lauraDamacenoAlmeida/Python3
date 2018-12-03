
class Conta:

    def __init__(self, numero, titular, saldo, agencia):
        print("construindo objeto..{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__agencia = agencia

    def extrato(self):
        print("Conta numero: {}".format(self.__numero))
        print("Saldo: {}".format(self.__saldo))

    def depositar(self, valor):
        self.__saldo += valor

    def saque(self, valor):

        if (self.__pode_sacar(valor)):
            print("Saldo menor que o valor de saque")
            print("Saldo atual {}".format(self.__saldo))

        else:
            self.__saldo -= valor

    def transferir(self, valor, destino):
        self.saque(valor)
        destino.depositar(valor)

    def __pode_sacar(self, valor):
        return self.__saldo <= valor

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def numero(self):
        return self.__numero

    @property
    def agencia(self):
        return self.__agencia
    #acessar o valor do metodo sem precisar depender de um objeto criado
    #ex: Conta.condigo_bancario()
    @staticmethod
    def codigo_bancario():
        return "001"

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo




