while True:
    opcoes = input("Digite a letra da operação que deseja fazer o calculo, M-Multiplicação, D-Divisão, A-Adicão e S-Subtração ou O-Sair: ")

    if opcoes == "M" or opcoes == "m":
        valor1 = int(input("Digite o primeiro valor: "))
        valor2 = int(input("Digite o segundo valor: "))
        print(f"Resultado: {valor1*valor2} ")

    elif opcoes == "D" or opcoes == "d":
        valor1 = int(input("Digite o primeiro valor: "))
        valor2 = int(input("Digite o segundo valor: "))
        print(f"Resultado: {valor1/valor2} ")

    elif opcoes == "A" or opcoes == "a":
        valor1 = int(input("Digite o primeiro valor: "))
        valor2 = int(input("Digite o segundo valor: "))
        print(f"Resultado: {valor1+valor2} ")

    elif opcoes == "S" or opcoes == "s":
        valor1 = int(input("Digite o primeiro valor: "))
        valor2 = int(input("Digite o segundo valor: "))
        print(f"Resultado: {valor1-valor2} ")

    elif opcoes == "O" or opcoes == "o":
        print("Saindo...")
        break

