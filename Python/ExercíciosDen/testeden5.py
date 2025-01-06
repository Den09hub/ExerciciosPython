# Loja de Games

carrinho = []
consoles = []
controles = []
jogos_fisicos = []

def Menu_Loja():
    print('\n', 'Bem-Vindo a Loja John Games', '', sep= '____')
    print('\nO que deseja fazer nesse exato momento?:')
    print('1 - Comprar')
    print('2 - Visualizar as compras')
    print('3 - Vaga como funcionário')
    print('4 - Descrição da loja')
    print('5 - Limpeza do console')
    print('6 - Adicionar ao estoque')
    print('7 - Sair do sistema')

def Menu_Comprar():
    print('O que deseja comprar?:')
    print('1 - Consoles')
    print('2 - Controles')
    print('3 - Jogos mídia física')

def Menu_Consoles():
    print('Disponíveis:')
    for p in consoles:
        print(p)

def Visualizar_compras():
    print('Compras feitas:')
    for v in carrinho:
        print(v)

def Menu_Abastecer():
    print('O que deseja comprar?:')
    print('1 - Consoles')
    print('2 - Controles')
    print('3 - Jogos mídia física')

while True:
    Menu_Loja()
    opcao_menu = int(input('Digite o que deseja: '))
    if opcao_menu == 1:
        Menu_Comprar()
        opcao_comprar = int(input('Digite o que deseja: '))
        if opcao_comprar == 1:
            Menu_Consoles()
            opcao_consoles = int(input('Selecione sua compra: '))
            carrinho.append(abastecer_consoles)
            del consoles[opcao_consoles]
            print('Comprado!')

    if opcao_menu == 2:
        Visualizar_compras()

    if opcao_menu == 6:
        Menu_Abastecer()
        opcao_abastecer = int(input('Digite o que deseja abastecer: '))
        if opcao_abastecer == 1:
            abastecer_consoles = input('Digite a ordem e o novo console: ')
            consoles.append(abastecer_consoles)

    if opcao_menu == 7:
        print('O sistema foi finalizado! Agradecemos pela sua presença.')
        print(f'Compras que saíram do estoque:\n{carrinho}')
        break
        
