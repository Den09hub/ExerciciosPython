carrinho = []
preco = []

while True:
    print('Escolha uma forma de usuário')
    print('1 - Cliente')
    print('2 - Funcionário')
    usuario = int(input('Digite o número: '))
    if usuario == 1:
        nome_cliente = input('Digite seu nome: ')
        cpf_cliente = int(input('Digite seu CPF: '))
        print('Concluído')
    elif usuario == 2:
        matricula_funcionario = int(input('Matrícula: '))
        nome_funcionario = input('Digite seu nome: ')
        data_funcionario = int(input('Digite sua data de nascimento: '))
        cpf_funcionario = int(input('Digite seu CPF: '))
        print('Concluído')

    while True:
        if usuario > 2 or usuario < 1:
            print('Inválido')
            break

        print('1 - Seção de Alimentos')
        print('2 - Seção de Higiene')
        print('3 - Seção de Produtos de casa')
        print('4 - Finalizar as compras')
        print('5 - Retirar os produtos do carrinho')
        print('6 - Sair do Usuário')
        menu = int(input('Digite um número de acordo com sua preferência: '))
        if menu == 6:
            print('Saindo do Usuário...')
            break
        
        while True:
            if menu > 6 or menu < 1:
                print('Inválido')
                break


            if menu == 1:
                print('1 - Arroz R$20')
                print('2 - Frango R$22')
                print('3 - Carne R$25')
                print('4 - Sair')
                alimentos = int(input('Digite um númeto de acordo com o item de sua preferência: '))
                if alimentos == 1:
                    carrinho.append('Arroz R$20')
                    preco.append(20)
                elif alimentos == 2:
                    carrinho.append('Frango R$22')
                    preco.append(22)
                elif alimentos == 3:
                    carrinho.append('Carne R$25')
                    preco.append(25)
                elif alimentos == 4:
                    print('Deseja: ')
                    print('1 - Continuar as compras')
                    print('2 - Retirar os produtos do carrinho')
                    print('3 - Ir para o menu principal')
                    decisao = int(input('Digite: '))
                    if decisao == 1:
                        print
                    elif decisao == 2:
                        print(carrinho)
                        retirar = int(input('O que deseja retirar (digite um número de 0 em diante de acordo com a ordem dos seus produtos): '))
                        del carrinho[retirar]
                        del preco[retirar]
                        print(carrinho)
                        print('Removido com sucesso')
                    elif decisao == 3:
                        break                    

            elif menu == 2:
                print('1 - Creme dental R$7')
                print('2 - Fio dental R$5')
                print('3 - Sabonete R$3')
                print('4 - Sair')
                higiene = int(input('Digite um número de acordo com o item de sua preferência: '))
                if higiene == 1:
                    carrinho.append('Creme dental R$7')
                    preco.append(7)
                elif higiene == 2:
                    carrinho.append('Fio dental R$5')
                    preco.append(5)
                elif higiene == 3:
                    carrinho.append('Sabonete R$3')
                    preco.append(3)
                elif higiene == 4:
                    print('Deseja: ')
                    print('1 - Continuar as compras')
                    print('2 - Retirar os produtos do carrinho')
                    print('3 - Ir para o menu principal')
                    decisao2 = int(input('Digite: '))
                    if decisao2 == 1:
                        print
                    elif decisao2 == 2:
                        print(carrinho)
                        retirar2 = int(input('O que deseja retirar (Digite um número de 0 em diante de acordo com a ordem de seus produtos): '))
                        del carrinho[retirar2]
                        del carrinho[retirar2]
                        print(carrinho)
                        print('Removido com sucesso')
                    elif decisao2 == 3:
                        break
                        
            elif menu == 3:
                print('1 - Água sanitária R$10')
                print('2 - Detergente R$4')
                print('3 - Sabão em pó R$8')
                print('4 - Sair')
                produtos_de_casa = int(input('Digite um número de acordo com o item de sua preferência: '))
                if produtos_de_casa == 1:
                    carrinho.append('Água sanitária R$10')
                    preco.append(10)
                elif produtos_de_casa == 2:
                    carrinho.append('Detergente R$4')
                    preco.append(4)
                elif produtos_de_casa == 3:
                    carrinho.append('Sabão em pó R$8')
                    preco.append(8)
                elif produtos_de_casa == 4:
                    print('Deseja: ')
                    print('1 - Continuar as compras')
                    print('2 - Retirar os produtos do carrinho')
                    print('3 - Ir para o menu principal')
                    decisao3 = int(input('Digite: '))
                    if decisao3 == 1:
                        print
                    elif decisao3 == 2:
                        print(carrinho)
                        retirar3 = int(input('O que deseja retirar (Digite um número de 0 em diante de acordo com a ordem de seus produtos): '))
                        del carrinho[retirar3]
                        del carrinho[retirar3]
                        print(carrinho)
                        print('Removido com sucesso')
                    elif decisao3 == 3:
                        break

            elif menu == 4:
                for ordem in carrinho:
                    print(ordem)
                
                soma = sum(preco)
                print(f'Preço total dos produtos: R${soma}')
                print('Selecione uma forma de pagamento:')
                print('1 - Dinheiro')
                print('2 - Pix')
                print('3 - Cartão')
                print('4 - Voucher')
                print('5 - Sair')
                pagamento = int(input('Digite: '))
                if pagamento == 1:
                    dinheiro_entregue = float(input('Digite a quantidade de dinheiro que deseja: '))
                    if dinheiro_entregue == soma:
                        calculo_dinheiro = dinheiro_entregue - soma
                        print('Pagamento concluído')
                        print(f'Troco: R${calculo_dinheiro}')
                        break
                    elif dinheiro_entregue > soma:
                        calculo_dinheiro2 = dinheiro_entregue - soma
                        print('Pagamento concluído')
                        print(f'Troco: R${calculo_dinheiro2}')
                        break
                    elif dinheiro_entregue < soma:
                        print('Dinheiro insuficiente, solicite outra forma de pagamento')
                elif pagamento == 2:
                    saldo_existente = float(input('Qual saldo existente: '))
                    if saldo_existente == soma:
                        calculo_saldo = saldo_existente - soma
                        print('Pagamento com sucesso')
                        break
                    elif saldo_existente > soma:
                        calculo_saldo2 = saldo_existente - soma
                        print('Pagamneto com sucesso')
                        break
                    elif saldo_existente < soma:
                        print('Insuficiente, selecione outra forma de pagamento')
                elif pagamento == 3:
                    print('1 - Crédito')
                    print('2 - Débito')
                    cartao_escolha = int(input('Qual tipo de cartão deseja usar: '))
                    if cartao_escolha == 1:
                        saldo_credito = float(input('Qual saldo existente: '))
                        if saldo_credito == soma:
                            calculo_credito = saldo_credito - soma
                            print('Pagamento com sucesso')
                            break
                        elif saldo_credito > soma:
                            calculo_credito2 = saldo_credito - soma
                            print('Pagamento com sucesso')
                            break
                        elif saldo_credito < soma:
                            print('Insuficiente, selecione outra forma de pagamento')
                    elif cartao_escolha == 2:
                        saldo_debito = float(input('Qual saldo existente: '))
                        if saldo_debito == soma:
                            calculo_debito = saldo_debito - soma
                            print('Pagamento com sucesso')
                            break
                        elif saldo_debito > soma:
                            calculo_debito2 = saldo_debito - soma
                            print('Pagamento com sucesso')
                            break
                        elif saldo_debito < soma:
                            print('Insuficiente, selecione outra forma de pagamento')
                elif pagamento == 4:
                    print('Pagamento com sucesso')
                    break
                elif pagamento == 5:
                    break
            
            elif menu == 5:
                print(carrinho)
                retirar4 = int(input('O que deseja retirar (Digite um número de 0 em diante de acordo com a ordem de seus produtos): '))
                del carrinho[retirar4]
                del preco[retirar4]
                print(carrinho)
                print('Removido com sucesso')
                break