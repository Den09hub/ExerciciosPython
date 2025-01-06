c1 = 0
c2 = 0
c3 = 0
c4 = 0
n = 0
b = 0

while True:
    voto = int(input("Digite um código para votar de 1, 2, 3, 4, 5 ou 6. Para encerrar digite 0: "))
    if voto == 0:
        print("Finalizado")
        break

    elif voto == 1:
        c1 = c1 + 1
    elif voto == 2:
        c2 = c2 + 1
    elif voto == 3:
        c3 = c3 + 1
    elif voto == 4:
        c4 = c4 + 1
    elif voto == 5:
        n = n + 1
    elif voto == 6:
        b = b + 1
    else:
        print("Inválido")

    print(f"O primeiro candidato tem: {c1}")
    print(f"O segundo candidato tem: {c2}")
    print(f"O terceiro candidato tem: {c3}")
    print(f"O quarto candidato tem: {c4}")
    print(f"Voto nulo: {n}")
    print(f"Voto em branco: {b}")


