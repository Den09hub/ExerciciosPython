class Barbearia:
    def __init__(self):
        self.agendamentos = []

    def Agendar_cliente(self, agenda):
        self.agendamentos.append(agenda)

    def CancelarAgendamento(self):
        for i in self.agendamentos:
            print(i)
        cancelar_agenda = int(input('Digite o agendamento que queira cancelar começando pela posição 0 em diante: '))
        self.agendamentos.pop(cancelar_agenda)
        print('Cancelado com sucesso!')

    def VisualizarAgendamentos(self):
        if self.agendamentos:
            for i in self.agendamentos:
                print(i)

        else:
            print('\nNenhuma agenda!')