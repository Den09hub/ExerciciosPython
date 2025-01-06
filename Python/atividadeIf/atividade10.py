sanduiche = int(input("Digite o código do lanche de sua preferência: "))
bebida = int(input("Digite o código da bebida de sua preferência: "))

if sanduiche == 100:
    preco = 11.20
elif sanduiche == 101:
    preco = 8.30
elif sanduiche == 102:
    preco = 11.50
elif sanduiche == 103:
    preco = 16.20

if bebida == 201:
        preco += 6.00
elif bebida == 202:
        preco += 7.50
elif bebida == 203:
        preco += 4.74

print(f"O valor total é R${preco}")

