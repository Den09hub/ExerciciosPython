import random

class Bingo:
    def __init__(self):
        self.numeros = []

    def sorteio_de_numero(self):
        while True:
            print('\nBem vindo ao BINGO')
            print('Selecione uma opção conforme sua preferência:')
            print('1 - Sortear um número')
            print('2 - Sair do sistema')
            opcao_bingo = int(input('Digite aqui: '))

            if opcao_bingo == 1:
                for i in range(1):
                    num = random.randint(1,5)
                    
                    if num not in self.numeros:
                        self.numeros.append(num)
                    
                    if num in self.numeros:
                        num1 = random.randint(1,5)
                        if num1 not in self.numeros:
                            self.numeros.append(num1)
                        print(f'\n{self.numeros}')

                    if num < 5 == len(self.numeros):
                        print('Concluído')

            elif opcao_bingo == 2:
                print('Saindo do sistema...\n\nFinalizado.')
                break

            else:
                print('Número Inválido. Por favor, selecione um número válido.')

bingo1 = Bingo()
bingo1.sorteio_de_numero()