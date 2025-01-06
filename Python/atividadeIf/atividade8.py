valor_saque = int(input("Digite o valor que deseja sacar (entre 10 a 600 reais): "))

if valor_saque < 10 or valor_saque > 600:
        print("O valor do saque invalido. O mínimo é 10 reais e o máximo é 600 reais.")
    
notas_100 = valor_saque // 100
valor_saque %= 100
notas_50 = valor_saque // 50
valor_saque %= 50
notas_10 = valor_saque // 10
valor_saque %= 10
notas_5 = valor_saque // 5
notas_1 = valor_saque

print("\nQuantidade de notas: ")
print("Notas de 100 reais: ", notas_100)
print("Notas de 50 reais: ", notas_50)
print("Notas de 10 reais: ", notas_10)
print("Notas de 5 reais: ", notas_5)
print("Notas de 1 real: ", notas_1)