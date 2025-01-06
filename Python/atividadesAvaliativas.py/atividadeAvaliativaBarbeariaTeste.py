agendamentos_Armazenados = []

class Agendamento:
    def __init__(self, nome_cliente, data, hora, servico):
        self.nome_cliente = nome_cliente
        self.data = data
        self.hora = hora
        self.servico = servico

    def Menu_Usuario(self):
        while True:
            print('\n', 'BEM-VINDO', '', sep= '___')
            print('\n O que deseja fazer nesse exato momento:')
            print(' 1 - Agendar')
            print(' 2 - Cancelar Agendamentos')
            print(' 3 - Visualizar Agendamentos')

            opcao_usuario = int(input(' Digite conforme sua preferência: '))

            if opcao_usuario == 1:
                self.nome_cliente = input(' Digite o nome do cliente: ')
                print(' Registrado')

                self.data = input(' Digite a data do agendamento de acordo com dd/mm/aaaa: ')
                if self.data[2] == '/' and self.data[5] == '/':
                    d, m, a = int(self.data[:2]), int(self.data[3:5]), int(self.data[6:])
                    
                if (d >= 0 and d <= 31) and (m >= 0 and m <= 12) and (a >= 0 and a <= 9999):
                    print(' Registrado')

                else:
                    print(' Não registrado')

                self.hora = input('Digite o horário de acordo com 00:00: ')
                if self.hora[2] == ':':
                    i, f = int(self.hora[:2]), int(self.hora[3:])

                if (i >= 0 and i <= 24) and (f >= 0 and f <= 60):
                    print('Registrado')

                else:
                    print('Não registrado')

                self.servico = input('Digite o serviço do cliente: ')
                agendamentos_Armazenados.append(self.nome_cliente)
                agendamentos_Armazenados.append(self.data)
                agendamentos_Armazenados.append(self.hora)
                agendamentos_Armazenados.append(self.servico)
                print(f'\nAgendamento Feito!\n{agendamentos_Armazenados}')


    def Agendar(self):
        pass

    def Cancelar_Agendamentos(self):
        pass

    def Visualizar_Agendamentos(self):
        pass

cliente_one = Agendamento('', '', '', '')
cliente_one.Menu_Usuario()

        
        
