
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

class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        self._nome = nome
        self._ano = ano
        self.__duracao = duracao
        self._likes = 0

    @property
    def duracao(self):
        return self.__duracao

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        self._nome = nome
        self._ano = ano
        self.__temporadas = temporadas
        self._likes = 0

    @property
    def temporadas(self):
        return self.__temporadas



