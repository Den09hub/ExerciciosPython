numero = int(input('Digite um número: '))
num1 = 1
num2 = 2
num3 = 3
triangular = False

while(num1*num2*num3) <= numero:
    if (num1*num2*num3) == numero:
        triangular = True
        break

    num1 = num1+1
    num2 = num2+1
    num3 = num3+1

if triangular == True:
    print('O número é triangular')
else:
    print('O número não é triangular')