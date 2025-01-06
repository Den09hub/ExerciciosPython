salario_inicial = 1000

salario_atual = salario_inicial + (salario_inicial * 0.015)

ano = 1997
percentual_aumento = 0.015 * 2

while ano <= 2024:
    print(f"{salario_atual} = {salario_atual} + {salario_atual} * {percentual_aumento}")
    salrio_inicial = salario_atual + (salario_atual * percentual_aumento)
    percentual_aumento = percentual_aumento * 2
    ano = ano + 1

print(f"O salário atual do funcionario em 2024 é R$ {salario_atual:.2f}")