
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
        self._likes += 1

    def __str__(self):
        return f'{sel._nome} - {self.ano} : {self._likes}'

#Como é herança, pssamos o nome da classe mae como parametro na criacao de outra classe
#para acessar atributos e metodos da classe mae, precisamos usar o algoritmo "super()"
class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.__duracao = duracao

    @property
    def duracao(self):
        return self.__duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min: {self._likes}'

#str é usado para imprimir o nosso objeto em forma textual, na hora de testa-lo no console, só imorimir o nome da minha
# variavel/lista
class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.__temporadas = temporadas

    @property
    def temporadas(self):
        return self.__temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas: {self._likes}'

#como a minha playlist nao é iterable, para facilitar o seu manuseio fazemos com que ela herde da classe List,
# onde ela terá todos os componentes de uma lista. Pegamos o metodo __init__ e passamos como parametro a lista que receberemos

class Playlist(list):
    def __init__(self, nome, programas):
        self.nome = nome
        super().__init__(programas)







