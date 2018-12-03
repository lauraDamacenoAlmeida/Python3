

class Cliente:
    def __init__(self,nome):
        self.__nome = nome

        #ao colocar um metodo como @property, eu digo para o python que o metodo em questao trata-se de uma propriedade
        #onde poderei chama-lo sem os paremnteses no console
    @property
    def nome(self):
        return self.__nome

    #set
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

