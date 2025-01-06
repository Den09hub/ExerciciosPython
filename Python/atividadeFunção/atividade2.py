lampada = False

def ligarLampada():
    return True

def desligarLampada():
    return False

def consultarLampada():
    if lampada:
        print('acessa')
    else:
        print('Desligada')

while True:
    print('1 - Ligar lampada')
    print('2 - Desligar lampada')
    print('3 - Consultar lampada')
    opcao = int(input('Digite uma opção: '))

    if opcao == 1:
        lampada = ligarLampada()
    elif opcao == 2:
        lampada = desligarLampada()
    elif opcao == 3:
        consultarLampada()



