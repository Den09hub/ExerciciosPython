from barbearia import Barbearia
from agendamento import Agendamentos

def ExibirMenu():
    print('\n','Bem-Vindo a Barbearia do John', '', sep= '____')
    print('\nO que deseja fazer nesse exato momento:')
    print('1 - Agendar')
    print('2 - Cancelar Agendamento')
    print('3 - Visualizar Agendamento')
    print('4 - Sair do Sistema')

barbearia = Barbearia()

while True:
    ExibirMenu()
    opcao = int(input('Digite conforme o que deseja: '))

    if opcao == 1:
        nome_cliente = input('Digite o nome do cliente: ')

        data_cliente = input('Digite a data no formato dd/mm/aaaa: ')

        if data_cliente[2] == '/' and data_cliente[5] == '/':
            d, m, a = int(data_cliente[:2]), int(data_cliente[3:5]), int(data_cliente[6:])

        if (d >= 0 and d <= 31) and (m >= 0 and m <= 12) and (a >= 0 and a <= 9999):
            print

        hora_cliente = input('Digite o horário no formato 00:00: ')

        if hora_cliente[2] == ':':
            hora, minuto = int(hora_cliente[:2]), int(hora_cliente[3:])

        if hora >= 0 and hora <= 24 and minuto >= 0 and minuto <= 60:
            print

        servico_cliente = input('Digite o serviço do cliente: ')

        agenda = Agendamentos(nome_cliente, data_cliente, hora_cliente, servico_cliente)
        barbearia.Agendar_cliente(agenda)
        print('Agendado com sucesso!')

    if opcao == 2:
        barbearia.CancelarAgendamento()

    if opcao == 3:
        barbearia.VisualizarAgendamentos()

    if opcao == 4:
        break
