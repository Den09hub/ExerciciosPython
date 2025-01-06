notas = {}

notas['Nota 1'] = int(input('Digite a primeira nota: '))
notas['Nota 2'] = int(input('Digite a segunda nota: '))
notas['Nota 3'] = int(input('Digite a terceira nota: '))
notas['Nota 4'] = int(input('Digite a quarta nota: '))

media = sum(notas.values())/len(notas)

print(f'{notas}, a média: {media}')
    