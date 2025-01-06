# Jogo de luta
import random

personagem_one = []
dano = []

def Inicial_Start():
    print('\n', 'FANTASY OF DEATH', '', sep='____')

def Genero_Personagem():
    print('\nLOADING...')
    print('\nCRIAÇÃO DE PERSONAGEM:')
    print('Gênero:')
    print('1 - Masculino')
    print('2 - Feminino')

def Classe_Personagem():
    print('\nCLASSE DO PERSONAGEM:')
    print('1 - Cavaleiro !')
    print('2 - Mago @')
    print('3 - Arqueiro /->')

def Nome_Personagem():
    print('\nESCOLHA O NOME DO SEU PERSONAGEM')

def Boss_Iniciando():
    print('\nLOADING...')
    print('\nBATALHA CONTRA O BOSS INICIANDO...')
    print('\nREADY')

def Boss_Fighte():
    print('\nBOSS')
    hp_boss = print(f'HP: {5000}')

    print(f'\n{personagem_one[2]}')
    hp_jogador = print(f'HP: {1000}')
    print('ARMAMENTOS:')
    print('1 - Atacar')

    return hp_boss, hp_jogador

while True:
    Inicial_Start()
    Comecar_game = input('\n         START')
    Genero_Personagem()
    opcao_genero = int(input('Digite: '))

    if opcao_genero == 1:
        if opcao_genero:
            personagem_one.append('Gênero: Masculino')
            print(f'Personagem: {personagem_one}')

            Classe_Personagem()
            opcao_classe = int(input('Digite: '))
            if opcao_classe == 1:
                personagem_one.append('Classe: Cavaleiro')
                print(f'Personagem: {personagem_one}')

                Nome_Personagem()
                escolha_nome = input('Digite: ')
                personagem_one.append(f'Nome: {escolha_nome}')
                print(f'Personagem: {personagem_one}')
                print('\nCriação Concluída')
                Boss_Iniciando()
                Boss_Fighte()
                opcao_batalha = int(input('Selecione: '))
                if opcao_batalha == 1:
                    damage = random.randint(1, 100)
                    dano.append(damage)
                    print(f'Dano causado: {damage}')
                    
                    

        