tarefas = []
def menu_de_terafas():
    print('1 - Adicionar tarefa')
    print('2 - Listar tarefa')
    print('3 - Marcar tarefa como concluído')
    print('4 - Remover tarefa')
    print('5 - Sair')
    selecionar = int(input('Digite: '))
    return selecionar

def adicionar_tarefa():
    tarefas_adicionadas = {}
    print('Digite a descrição de tarefa: ')
    tarefas_adicionadas['Descrição'] = input('Digite: ')
    tarefas_adicionadas['Status'] = 'Não concluído'
    tarefas.append(tarefas_adicionadas.copy())
    return

def listar_tarefa():
    for listar in tarefas:
        print(listar)

def marcar_concluido():
    for listar in tarefas:
        print(listar)

    tarefa_concluido = int(input('Selecione a tarefa que deseja concluír '))
    tarefas[tarefa_concluido]['Status'] = 'Concluído'

    for listar in tarefas:
        print(listar)
    return

def remover_tarefa():
    for listar in tarefas:
        print(listar)

    excluir_tarefa = int(input('Selecione a tarefa para remover: '))
    tarefas.pop(excluir_tarefa)
    
    for listar in tarefas:
        print(listar)
        return
    
def sair_sistema():
    print('Obrigado por usar nosso sistema')
    print('Saindo...')
    return

while opcao != 0:
    opcao = menu_de_terafas()
    if opcao <= 0:
        break
    
    



