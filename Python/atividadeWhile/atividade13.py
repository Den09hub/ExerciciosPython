while True:
    print("Digite o número da operação desejada")
    print("1. Multiplicação")
    print("2. Divisão")
    print("3. Adicão")
    print("4. Subtração")
    print("5. Sair")

    numero = int(input("Digite: "))
    if numero == 5:
        print("Saindo do sistema...")
        break
    elif numero < 1 or numero > 5:
        print("Inválido. Digite um número válido")

    elif numero == 1:
        valor1 = float(input("Digite o primeiro valor: "))
        valor2 = float(input("Digite o segundo valor: "))
        print(f"O resultado final é {valor1*valor2}")
    elif numero == 2:
        valor1 = float(input("Digite o primeiro valor: "))
        valor2 = float(input("Digite o segundo valor: "))
        print(f" O resultado final é {valor1/valor2}")
    elif numero == 3:
        valor1 = float(input("Digite o primeiro valor: "))
        valor2 = float(input("Digite o segundo valor: "))
        print(f"O resultado final é {valor1+valor2}")
    elif numero == 4:
        valor1 = float(input("Digite o primeiro valor: "))
        valor2 = float(input("Digite o segundo valor: "))
        print(f"O resultado final é {valor1-valor2}")

        

    