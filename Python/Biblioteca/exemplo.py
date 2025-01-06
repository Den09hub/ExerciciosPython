lista = [1, 2, 3]
dicionario = {'a': 1, 'b': 2}

try:
    resultado = dicionario['c']

except Exception as e:
    print(f'Erro foi {e}')