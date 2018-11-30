
def jogar():


    import random

    print("Hello word, bem vindo ao jogo de adivinhaço!!")
    print("▓▓▓")
    print("▒▒▒▓▓")
    print("▒▒▒▒▒▓")
    print("▒▒▒▒▒▒▓")
    print("▒▒▒▒▒▒▓")
    print("▒▒▒▒▒▒▒▓")
    print("▒▒▒▒▒▒▒▓▓▓")
    print("▒▓▓▓▓▓▓░░░▓")
    print("▒▓░░░░▓░░░░▓")
    print("▓░░░░░░▓░▓░▓")
    print("▓░░░░░░▓░░░▓")
    print("▓░░▓░░░▓▓▓▓")
    print("▒▓░░░░▓▒▒▒▒▓")
    print("▒▒▓▓▓▓▒▒▒▒▒▓")
    print("▒▒▒▒▒▒▒▒▓▓▓▓")
    print("▒▒▒▒▒▓▓▓▒▒▒▒▓")
    print("▒▒▒▒▓▒▒▒▒▒▒▒▒▓")
    print("▒▒▒▓▒▒▒▒▒▒▒▒▒▓")
    print("▒▒▓▒▒▒▒▒▒▒▒▒▒▒▓")
    print("▒▓▒▓▒▒▒▒▒▒▒▒▒▓")
    print("▒▓▒▓▓▓▓▓▓▓▓▓▓")
    print("▒▓▒▒▒▒▒▒▒▓")
    print("****************************************")

    numero_secreto = round(random.randrange(100) + 1)
    print(numero_secreto)
    tentativas = 0

    nivel = int(input('Selecione um nivel \n 1-Facil \n 2-Medio \n 3-Dificil \n'))
    if (nivel == 1):
        tentativas = 20
    elif (nivel == 2):
        tentativas = 10
    elif (nivel == 3):
        tentativas = 5
    else:
        print('Digite um nivel correto')

    print('Voce tem {} tentativas!!Boa sorteee'.format(tentativas))
    for rodada in range(1, tentativas + 1):
        chute = int(input("Digite um numero \n"))
        if (chute > 1):
            chute_maior = numero_secreto < chute
            chute_menor = numero_secreto > chute
            print("Voce digitou {}".format(chute))

            if (numero_secreto == chute):
                print("Certou mizeravi, voce precisou de {} tentativas ".format(rodada))
                break

            elif (chute_menor):
                print("O numero secreto eh maior que este")
                print("Mas nao desista, continue tentando")

            elif (chute_maior):
                print("o numero secreto eh menor que este")

            print('Tentativa {} de {}'.format(rodada, tentativas))

        else:
            print("Digite um numero maior que 1, por favoor")

##se o meu arquivo foi execitado no prompt de comando diretamente,o python cria internamente uma variavel chamada __name__
# e se ela estiver preenchida execute a funcao jogar()
if(__name__ == "__main__"):
    jogar()