def exibemenu():
    print('Menu\n')
    print('0 - Sair\n')
    print('1 - Somar\n')
    print('2 - Subtração\n')
    print('3 - Multiplicação\n')
    print('4 - Divisão\n')
    opcao = int(input('Escolha uma opção de sua preferência: '))
    return opcao

def somar(numero1, numero2):
    resultado = numero1+numero2
    return resultado
def subtracao(numero1, numero2):
    resultado = numero1-numero2
    return resultado
def multiplicacao(numero1, numero2):
    resultado = numero1*numero2
    return resultado
def divisao(numero1, numero2):
    resultado = numero1/numero2
    return resultado

i = 0
opcao = 1
num1 = 0
num2 = 0
resultado = 0

while opcao !=0:
    opcao = exibemenu()
    if opcao <= 0:
        break

    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    if opcao == 1:
        resultado = somar(num1, num2)
    elif opcao == 2:
        resultado = subtracao(num1, num2)
    elif opcao == 3:
        resultado = multiplicacao(num1, num2)
    elif opcao == 4:
        resultado = divisao(num1, num2)
    print('Resultado: %f\n\n' %resultado)