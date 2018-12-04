
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome
        self._ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome.title()
    @property
    def ano(self):
        return self._ano
    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()

    def dar_like(self):
        self.__likes += 1
#Como é herança, pssamos o nome da classe mae como parametro na criacao de outra classe
#para acessar atributos e metodos da classe mae, precisamos usar o algoritmo "super()"
class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.__duracao = duracao

    @property
    def duracao(self):
        return self.__duracao

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.__temporadas = temporadas

    @property
    def temporadas(self):
        return self.__temporadas

    filmes_e_series = ['Got',]



