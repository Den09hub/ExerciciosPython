caderno = 0
caneta = 0
lapis = 0
borracha = 0
regua = 0

while True:
    print('Escolha a operação:')
    print('E-Entrada no estoque')
    print('S-Saída no estoque')
    print('R-Relatório')
    print('X-Sair')

    menu = input('Digite: ')

    if menu == 'E' or menu == 'e':
        print('códigos:')
        print('10-Caderno')
        print('20-caneta')
        print('30-Lápis')
        print('40-Borracha')
        print('50-Régua')

        codigo = int(input('Digite um código: '))

        if codigo == 10:
            caderno = caderno + int(input('10-Digite uma quantidade: '))
        elif codigo == 20:
            caneta = caneta + int(input('20-Digite uma quantidade: '))
        elif codigo == 30:
            lapis = lapis + int(input('30-Digite uma quantidade: '))
        elif codigo == 40:
            borracha = borracha + int(input('40-Digite uma quantidade: '))
        elif codigo == 50:
            regua = regua + int(input('50-Digite uma quantidade: '))

    if menu == 'S' or menu == 's':
        print('códigos:')
        print('10-Caderno')
        print('20-caneta')
        print('30-Lápis')
        print('40-Borracha')
        print('50-Régua')

        codigo = int(input('Digite um código: '))

        if codigo == 10:
            caderno = caderno - int(input('10-Digite uma quantidade: '))
        elif codigo == 20:
            caneta = caneta - int(input('20-Digite uma quantidade: '))
        elif codigo == 30:
            lapis = lapis - int(input('30-Digite uma quantidade: '))
        elif codigo == 40:
            borracha = borracha - int(input('40-Digite uma quantidade: '))
        elif codigo == 50:
            regua = regua - int(input('50-Digite uma quantidade: '))

    if menu == 'R' or menu == 'r':
        print('Caderno:', caderno)
        print('Caneta:', caneta)
        print('Lápis:', lapis)
        print('Borracha::', borracha)
        print('regua:', regua)

    else: 
        if  menu == 'X' or menu == 'x':
            print('Saindo...')
            break
        
        #mostrar os codigos de produtos

        #verificar o codigo digitado
        #adicionar o estoque do produto escolhido