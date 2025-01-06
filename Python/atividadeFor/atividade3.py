while True:
    usuario = input('Digite seu nome de usuário: ')
    senha1 = input('Digite sua senha de usuário: ')

    if senha1 == usuario:
        print('Inválido, nome de usuario e senha iguais' )

    elif usuario and senha1:
        print('Válido, Bem-Vindo')
        break