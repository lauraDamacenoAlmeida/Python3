
import random

def jogar():
    apresentacao_jogo()
    palavra_secreta = gera_palavra_secreta()

    #Acrescenta um  _ para cada letra encontrada na palavra
    #simplificacao de
    #          for i in palavra_secreta:
    #               letras_acertadas.append('_')
    print("É uma fruta....")
    letras_acertadas = ['_' for i in palavra_secreta]
    acertou = False
    enforcou = False
    erros = 0

    print(letras_acertadas)

    while (not enforcou and not acertou):
        print("jogando...")
        chute = input("Digite uma letra \n").strip().lower()
        index = 0
        erros = compara_palavras(chute, palavra_secreta, letras_acertadas, index, erros)
        enforcou = erros == 7
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)
    imprime_resultado(acertou, enforcou, palavra_secreta)


def apresentacao_jogo():
    print('                          `. ___')
    print("                        __,' __`.                _..----....____")
    print("            __...--.'``;.   ,.   ;``--..__     .'    ,-._    _.-'")
    print("      _..-''-------'   `'   `'   `'     O ``-''._   (,;') _,'")
    print("    ,'________________                          \`-._`-','")
    print("     `._              ```````````------...___   '-.._'-:")
    print("        ```--.._      ,.                     ````--...__\-.")
    print("                  `. `.                       ,'`````.  ;  ;`")
    print("                    `._`.        __________   `.      \ '__/`")
    print("                `.--. `-`                       ____    |  |`")
    print("                       `-:._____/______/___/____`.     \  `")
    print("                                   |       `._    `.    \ ")
    print("                                   `._________`-.   `.   `.___")
    print("                                                      `------'`")
    print("**********WELCOME TO FORCA GAME***********")

def gera_palavra_secreta():
    # se der algum erro, com a utilizacao do with, o arquivo eh encerrado e sendo assim, nao precisamos fecha-lo no final da leitura
    with open("teste.txt", "r") as arquivo:
        palavras = []
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    # gerado uma lista para armazenar os dados do arquivo,
    # e depois foi gerado randomicamente um index para escolher uma palavra da lista aleatoriamente
    index = random.randrange(0, len(palavras))
    palavra_secreta = palavras[index].lower()
    return palavra_secreta

def compara_palavras(chute,palavra_secreta,letras_acertadas,index,erros):
    if (chute in palavra_secreta):
        for letra in palavra_secreta:
            if (chute == letra):
                print("Voce acertou a letra \n")
                letras_acertadas[index] = chute
            index += 1
    else:
        erros = erros + 1
        print(erros)
        print('Que pena!!! A letra {} nao esta na palavra secreta '.format(chute))
        print('Voce tem {} chances'.format(6 - erros))
        desenha_forca(erros)

    return erros


def imprime_resultado(acertou,enforcou,palavra_secreta):
    print('Fim de jogo!!')
    if (acertou):
        print('********Parabens voce ganhou************')
    if (enforcou):
        print('******Que pena voce perdeu**********')
        print('A palavra secreta é: {}'.format(palavra_secreta))

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


##se o meu arquivo foi execitado no prompt de comando diretamente,o python cria internamente uma variavel chamada __name__
# e se ela estiver preenchida execute a funcao jogar()
if (__name__ == "__main__"):
    jogar()
