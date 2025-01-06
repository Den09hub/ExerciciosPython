historico_do_paciente = []

while True:
    print('Entrar como:')
    print('1 - Usuário')
    print('2 - Médico')
    entrar_como = int(input('Digite: '))
    match entrar_como:
        case 1:
            print('Entrando como usuário...')
            print('Bem vindo')
            informacoes_do_paciente = {}

            informacoes_do_paciente['Nome'] = input('Digite seu nome: ')
            informacoes_do_paciente['CPF'] = int(input('Digite seu CPF: '))
            informacoes_do_paciente['Idade'] = int(input('Digite sua idade: '))
            informacoes_do_paciente['Horario da consulta'] = int(input('Digite o horario da consulta: '))
            historico_do_paciente.append(informacoes_do_paciente)

            print('Concluído')
            print('1 - Verificar suas consultas: ')
            print('2 - Sair do sistema')
            decisao_paciente = int(input('Digite: '))

            if decisao_paciente == 1:
                print(historico_do_paciente)
            elif decisao_paciente == 2:
                print('Obrigado por usar nosso sistema')
                break
        case 2:
            print('Entrando como médico')
            print('Bem vindo')
            print(f'Pacientes: {historico_do_paciente}')
            print('1 - Realizar a consulta')
            print('2 - Sair')
            realizar_consulta = int(input('Digite: '))
            if realizar_consulta == 1:
                print('Paciente:')
                print(historico_do_paciente)
                historico_do_paciente.pop
                print('Liberando o paciente...')
                print('Concluído')
            elif realizar_consulta == 2:
                print

        case _:
            print('Inválido')                        


        



    
