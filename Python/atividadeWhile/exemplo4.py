total = 0
while True:
    numero = int(input("Digite algum número inteiro positivo: "))

    if numero < 0:
        print("Número inválido. Digite outro valor")

    elif numero == 0:
        
        print(f"Total: {total}")
        break
    total = total + numero