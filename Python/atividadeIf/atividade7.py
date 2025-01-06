inteiro = int(input("Digite um número menor que 1000: "))

if inteiro < 1000:
    centenas = inteiro // 100
    dezenas = (inteiro % 100) // 10
    unidades = inteiro % 10

    print("Centenas: ", centenas)
    print("Dezenas: ", dezenas)
    print("Unidades: ", unidades)

else:
    print("O número não é menor que 1000")


        
            