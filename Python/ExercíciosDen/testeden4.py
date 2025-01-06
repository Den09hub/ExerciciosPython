# 1 - print('Hello World!')

# 2 - numero = int(input('Digite um número: '))
# print(f'O número informado foi {numero}')

# 3 - numero1 = int(input('Digite o primeiro número: '))
# numero2 = int(input('Digite o segundo número: '))
# print(f'A soma dos números informados é {numero1 + numero2}')

# 4 - nota1 = int(input('Digite a primeira nota: '))
# nota2 = int(input('Digite a segunda nota: '))
# nota3 = int(input('Digite a terceira nota: '))
# nota4 = int(input('Digite a quarta nota: '))
# print(f'\nA média do aluno é {(nota1 + nota2 + nota3 + nota4) / 4}')

# 5 - metros = int(input('Metros: '))
# print(f'Centímetros: {metros * 100}cm')

# 6 - raio = int(input('Digite o raio do círculo: '))
# print(f'A área do círculo é A = {raio**2}')

# 7 - base = 10
# altura = 10
# area = 10 * 10
# print(f'O comprimento da base: {base}')
# print(f'O comprimento da altura: {altura}')
# print(f'\nO dobro da área do quadrado é {area + area}')

# 8 - salario_por_hora = float(input('Digite o quanto você ganha por hora: R$'))
# horas_trabalhadas_mes = int(input('Digite o quanto você trabalha em um mês: '))
# print(f'\nO total que você ganha em um mês: R${salario_por_hora * horas_trabalhadas_mes:.2f}')

# 9 - temperatura_fahrenheit = int(input('Digite uma temperatura em grau fahrenheit: '))
# temperatura_celsius = (temperatura_fahrenheit - 32) * 5/9
# print(f'\nA temperatura em grau transformada em Celsius: {temperatura_celsius:.2f}ºC ')

# 10 - temperatura_celsius = int(input('Digite uma temperatura em grau Celsius: '))
# temperatura_fehrenheit = (temperatura_celsius * 9/5) + 32
# print(f'\nA temperatura em grau transformada em Fehrenheit: {temperatura_fehrenheit:.2f}ºF')

# 11 - numero_inteiro = int(input('Digite um número inteiro: '))
# numero_real = float(input('Digite um número real: '))
# produto = (numero_inteiro * 2) + (numero_real / 2)
# soma = (numero_inteiro * 3) + (produto * 3)
# print(f'Resultado: {soma * 3}')

# 12 - altura_usuario = float(input('Digite sua altura: '))
# peso_ideal = (72.7 * altura_usuario) - 58
# print(f'O peso ideal: {peso_ideal}')

# 13 - altura_homem = float(input('Digite a altura de um homem: '))
# peso_ideal_h = (72.7 * altura_homem) - 58

# altura_mulher = float(input('Digite a altura de uma mulher: '))
# peso_ideal_m = (62.1 * altura_mulher) - 44.7

# print(f'\nPeso ideal para o homem: {peso_ideal_h:.2f}\n')
# print(f'Peso ideal para a mulher: {peso_ideal_m:.2f}')

usuario_joao = int(input('Digite a quantidade de peixes em gramas: '))
peso_peixes = usuario_joao / 1000
multa = 4

if peso_peixes < 50:
    print('A quantidade está adequada. Não atingiu mais que 50 quilos')

else:
    if peso_peixes > 50:
        pass

    

