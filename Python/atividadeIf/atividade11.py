def calcular_preco_final(preco_etiqueta, codigo_condicao_pagamento):
    if codigo_condicao_pagamento == 1:
        preco_final = preco_etiqueta * 0.9
    elif codigo_condicao_pagamento == 2:
        preco_final = preco_etiqueta * 0.95
    elif codigo_condicao_pagamento == 3:
        preco_final = preco_etiqueta
    elif codigo_condicao_pagamento == 4:
        preco_final = preco_etiqueta * 1.1
    
    else:
        preco_final = "Código de condição de pagamento inválido."

    return preco_final

preco_etiqueta = float(input("Digite o preço normal de etiqueta do produto: "))
codigo_condicao_pagamento = int(input("Digite o código da condição de pagamento (1 a 4): "))

preco_final = calcular_preco_final(preco_etiqueta, codigo_condicao_pagamento)
if isinstance(preco_final, str):
    print(preco_final)
else:
    print("O valor a ser pago pelo produto é: R${:.2f}".format(preco_final))
