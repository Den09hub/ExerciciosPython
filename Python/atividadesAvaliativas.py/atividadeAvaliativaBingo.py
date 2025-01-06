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
                sorteio = random.randint(1, 75)

                if sorteio in self.numeros:
                    print('\nNúmero já sorteado.')
                    continue

                if sorteio not in self.numeros:
                    self.numeros.append(sorteio)
                    print(f'O número do sorteio foi {sorteio}\n')
                    print(self.numeros)

                if sorteio < 75 == len(self.numeros):
                    print('Concluído')
                    break

            elif opcao_bingo == 2:
                print('Saindo do sistema...\n\nFinalizado.')
                break

            else:
                print('Número Inválido. Por favor, selecione um número válido.')

bingo1 = Bingo()
bingo1.sorteio_de_numero()