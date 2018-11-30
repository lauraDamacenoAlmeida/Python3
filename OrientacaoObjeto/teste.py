
def metodos_conta():
    def criar_conta(numero, titular, saldo, agencia):
        conta = {"numero": numero, "titular": titular, "saldo": saldo, "agencia": agencia}
        return conta

    def depositar(conta,valor):
        conta["saldo"] += valor

    def saque(conta, valor):

        if(conta["saldo"]< valor):
            print("Saldo menor que o valor de saque")
            print("Saldo atual {}".format(conta["saldo"]))

        else:
            conta["saldo"] -=valor

    def extrato(conta):
        print("Conta numero: {}".format(conta["numero"]))
        print("Saldo: {}".format(conta["saldo"]))

