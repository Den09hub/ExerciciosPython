contas = []

def login_do_usuario():
    print('Bem-Vindo ao nosso Sistema.')
    print('Por favor, selecione uma opção abaixo.\n')
    print('1 - Iniciar Sessão')
    print('2 - Cadastrar-se')
    print('3 - Sair do Sistema')
    int(input('Digite: '))

def Cadastro_Usuario():
    while True:
        cadastrar_nome = input('Digite seu nome de usuário: ')
        if cadastrar_nome[2:] >= cadastrar_nome:
            print('Válido, prosseguindo...')
            cadastrar_senha = input('\nDigite sua senha: ')
            contas.append(cadastrar_nome)
            contas.append(cadastrar_senha)
            break

        elif cadastrar_nome[0:1] <= cadastrar_nome:
            print('Inválido, precisa ser no minímo três letras.')

Cadastro_Usuario()
print(contas)