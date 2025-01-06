tarefas = []

def Adicionar_tarefa():
    texto = input('Informe a descrição da atividade: ')
    tarefa = {'Descrição':texto, 'Status':False}
    tarefas.append(tarefa)
    print('Adicionado com sucesso!')

def Listar_tarefa():
    if len(tarefas) == 0:
        print('Não há nenhuma tarefa registrada')
    else:
        for i, tarefa in enumerate(tarefas):
            mensagem = 'Concluído'
            if not tarefa['Status']:
                mensagem = 'Não concluído'

            print(f'{i+1} {tarefa['Descrição']} {mensagem}')

def Marcar_Concluido():
    Listar_tarefa()
    numero = int(input('Digite o numero que deseja marcar: ')) -1
    if numero < len(tarefas):
        tarefas[numero]['Status'] = True
        print('Tarefa concluída')

def Remover_tarefa():
    Listar_tarefa()
    numero = int(input('Digite o número que quer remover: ')) -1
    if numero < len(tarefas):
        tarefas.pop(numero)
        print('Removido com sucesso!')
    else:
        print('Número inválido')

while True:
    print('1 - Adicione tarefa')
    print('2 - Listar tarefa')
    print('3 - Marcar tarefa como concluído')
    print('4 - Remover tarefa')
    print('5 - Sair')
    opcao = int(input('Escolha a opção: '))

    if opcao == 1:
        Adicionar_tarefa()
    elif opcao == 2:
        Listar_tarefa()
    elif opcao == 3:
        Marcar_Concluido()
    elif opcao == 4:
        Remover_tarefa()
    elif opcao == 5:
        print('Saindo...')
        break
