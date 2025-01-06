tarefas = []

while True:
    print('Olá. Bem vindo ao nosso sistema.\n')
    print('1 - Adicionar tarefa')
    print('2 - Listar tarefas')
    print('3 - Marcar tarefa como concluído')
    print('4 - Remover tarefa')
    print('5 - Sair')
    opcao = int(input('Digite a opção de sua preferência: '))
    
    tarefas_adicionadas = {}
    
    match opcao:
        case 1:
            print('Digite a descrição da tarefa')
            tarefas_adicionadas['Descrição'] = input('Digite: ')
            tarefas_adicionadas['Status'] = 'Não Concluído'
            tarefas.append(tarefas_adicionadas.copy())

        case 2:
            for listar in tarefas:
                print(listar)

        case 3:
            for listar in tarefas:
                print(listar)
            
            adicionar_concluido = int(input('Selecione uma tarefa para concluído: '))
            tarefas[adicionar_concluido]['Status'] = 'Concluído'

            for listar in tarefas:
                print(listar)

        case 4:
            for listar in tarefas:
                print(listar)

            remover_tarefa = int(input('Digite uma tarefa que deseja remover: '))
            tarefas.pop(remover_tarefa)

            for listar in tarefas:
                print(listar)
            
        case 5:
            print('Agradecemos por usar nosso sistema\n')
            print('Saindo...')
            break

        case _:
            print('Inválido') 
     