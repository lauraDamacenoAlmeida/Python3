# Problema: tenho uma super class chamada Funcionario, e subclasses Alura e Caelum, entretando eu posso
# ter funcionarios que estudam no Alura e trabalahm na caelum e temos subtipos Junior, Pleno e Senior
#Regra de negocio: Junior pode acessar somente Alura, enquanto pleno e Senior pode acessar os dois tipos

class Funcionario:
    def __init__(self,nome):
        self.nome = nome

    def registra_horas(self, horas):
        print('Horas registradas...')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')

class ToString:
    def __str__(self):
        return f'{self.nome}'

class Junior(Alura,ToString):
    pass

class Pleno(Alura, Caelum,ToString):
    pass

class Senior(Alura,Caelum,ToString):
    pass
#MRO (Method Resolution Order)
#Vai acessar minha classe atual, ver qual a classe mãe dela, se tiver + de uma, pego primeiro a da esquerda e procuro
# o metodo chamado, se eu não encontrar, eu acesso a classe ancestral da mãe e assim vai.
# Se nao encontrar em nenhuma delas ele vai para a proxima classe
#Pleno > Alura > Caelum > Funcionario

jose = Junior('JOSE')
jose.busca_perguntas_sem_resposta()
Paulo = Senior('Paulo')
print(Paulo, jose)

