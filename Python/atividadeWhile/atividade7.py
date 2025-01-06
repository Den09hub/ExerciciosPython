alto = 0
baixo = 0
magro = 0
gordo = 0
while True:
    codigo = int(input("Digite o código do cliente: "))
    altura = float(input("Digite a altura do cliente: "))
    peso = float(input("Digite o peso do cliente: "))
    if codigo == 0:
        break
    elif altura == 0:
        break
    elif peso == 0:
        break
    else:
        print(f"Código: {codigo}")
        if altura >= alto:
            print(f"O cliente mais alto: {altura}")
        elif altura <= baixo:
            print(f"O cliente mais baixo: {altura}")
        if  peso <= magro:
            print(f"O cliente mais magro: {peso}")
        elif peso >= gordo:
            print(f"O cliente mais gordo: {peso}")
        
