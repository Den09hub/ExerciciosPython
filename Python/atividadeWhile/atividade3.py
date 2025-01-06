while True:
    nota = int(input("Digite uma nota ente 0 e 10: "))
    if nota > 0 and nota < 10:
        print("Válido, obrigado por usar nosso sistema")
        break
    elif nota < 0 or nota > 10:
        print("Inválido") 