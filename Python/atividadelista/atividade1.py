nomes = []

while True:
    numero = int(input('Digite uma nota de 0 a 10: '))

    if numero > 0 and numero < 10:
        print('Válido, Obrigado por usar nosso sistema.')
        break

    elif numero < 0 or numero > 10:
        print('Inválido, digite uma nota de 0 a 10.')

