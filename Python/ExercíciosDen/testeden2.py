def exibirMenu():
    print('Selecione uma opção para calcular:')
    print('1 - Adição')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Expressões')
    print('6 - Sair do sistema')

def somaCalculo(primeiro, segundo):
    soma = primeiro + segundo
    return soma

def subtracaoCalculo(a, b):
    subtracao = a - b
    return subtracao

def multiplicaoCalculo(a, b):
    multiplicacao = a * b
    return multiplicacao

def divisaoCalculo(a, b):
    divisao = a / b
    return divisao

def inserirValores():
    primeiro = float(input("Digite o primeiro valor: "))
    segundo = float(input("Digite o segundo valor: "))
    return primeiro, segundo

while True:
    exibirMenu()
    opcao = int(input('Digite: '))
    if opcao == 1:
        primeiro, segundo = inserirValores()
        print(somaCalculo(primeiro, segundo))

    elif opcao == 2:
        inserirValores()
        print(subtracaoCalculo())

    elif opcao == 3:
        inserirValores()
        print(multiplicaoCalculo())

    elif opcao == 4:
        inserirValores()
        print(divisaoCalculo())

    elif opcao == 5:
        pass
            

    elif opcao == 6:
        print('\nObrigado por usar nosso sistema!\nFINALIZADO.')
        break

    else:
        print('Inválido, digite conforme o menu.\n')