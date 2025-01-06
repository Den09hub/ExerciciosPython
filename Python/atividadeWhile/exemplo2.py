cont = 1
while True:
    nome = (input("Digite um nome: "))
    if nome == "rafael" or nome == "RAFAEL" or nome == "Rafael":
        break
    
    cont = cont + 1
    print(f"Tentativas: {nome}")

    