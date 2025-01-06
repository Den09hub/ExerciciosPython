while True:
    nome = input("Digite um nome de usuário maior que três caracteres: ")
    idade = input("Digite uma idade entre 0 e 150: ")
    salario = input("Digite um salário acima de 0: ")

    if len(nome) < 4:
        print("Inválido, o nome precisa ter mais de três caracteres")
    elif not (0 <= int(idade) <= 150):
        print("A idade precisa estar entre 0 e 150")
    elif float(salario) <= 0:
        print("O salário precisa ser maior que 0")
    else:
        print("Válido")

    sexo = input("Digite seu sexo (F - Feminino, M - Masculino, O - Outro): ")
    if sexo.lower() == "f":
        print("Feminino")
    elif sexo.lower() == "m":
        print("Masculino")
    elif sexo.lower() == "o":
        print("Outro")

    estado_civil = input("Digite seu estado civil (S - Solteiro, C - Casado, V - Viúvo, D - Divorciado): ")
    if estado_civil.lower() == "s":
        print("Solteiro")
    elif estado_civil.lower() == "c":
        print("Casado")
    elif estado_civil.lower() == "v":
        print("Viúvo")
    elif estado_civil.lower() == "d":
        print("Divorciado")
        break

           