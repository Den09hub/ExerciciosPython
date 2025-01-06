# Pedindo o valor
produto1 = float(input("Digite o primeiro preço: "))
produto2 = float(input("Digite o segundo preço: "))
produto3 = float(input("Digite o terceiro preço: "))

# Decisão
if produto1 < produto2 and produto1 < produto3:
    print("O primeiro produto é o ideal")
elif produto2 < produto1 and produto2 < produto3:
    print("O segundo produto é o ideal")
else:
    print("Você deve comprar o terceiro produto")
