funcionario = []
maior = 0

for i in range(4):
    informacoes = {}
    informacoes['nome'] = input('Digite o nome: ')
    informacoes['funcao'] = input('Digite a função: ')
    informacoes['salario'] = float(input('Digite o salário: '))
    funcionario.append(informacoes)

    if informacoes['salario'] > maior:
        maior = informacoes['salario']

for pessoa in funcionario:
    if pessoa['salario'] == maior:
        print(f'O funcionario com maior salário é {pessoa['nome']}')
        
