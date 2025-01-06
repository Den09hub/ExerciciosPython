class Agenda:
    def __init__(self, dia, mes, ano, anotacao):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.anotacao = anotacao

    def validacao_de_data(self):
        print(f'Data: {self.dia}/{self.mes}/{self.ano}')
        print('Válido')

    def anotacao_tarefa(self):
        self.anotacao = input('Anote uma tarefa: ')
        print('Anotação concluída')

    def mostrar_anotacao(self):
        print(f'Anotação: {self.anotacao}')

pessoa1 = Agenda(1, 7, 2024, '')
pessoa1.validacao_de_data()
pessoa1.anotacao_tarefa()
pessoa1.mostrar_anotacao()




