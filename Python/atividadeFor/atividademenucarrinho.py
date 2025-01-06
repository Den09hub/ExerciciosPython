
carrinho = []
while True:
    print('1 - Lista de produtos')
    print('2 - Visualizar o carrinho')
    print('3 - Sair')
    op = int(input('Digite um número: '))

    if op == 3:
        break
    elif op == 2:
        print(f'Produtos = {carrinho}')
    elif op == 1:
        print('1 - mouse')
        print('2 - teclado')
        print('3 - headset')
        codProduto = int(input('Digite um número: '))

        if codProduto == 1:
            carrinho.append('mouse')
        elif codProduto == 2:
            carrinho.append('teclado')
        elif codProduto == 3:
            carrinho.append('headset')