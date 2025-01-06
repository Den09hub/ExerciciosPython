salarioatual = float(input("Digite o seu salário: "))
if salarioatual<500.00:
    a = salarioatual +(salarioatual*0.15)
    print(f"Você recebera 15% de aumento, seu novo salário será de R$:{a}")
elif salarioatual<=1000:
    b = salarioatual + (salarioatual*0.1)
    print(f"Você recebera 10% de aumento, seu novo salário será de R$:{b}")
else:
    c = salarioatual + (salarioatual*0.05)
    print(f" Você recebera 5% de aumento, seu novo salário será de R$:{c}")
    

