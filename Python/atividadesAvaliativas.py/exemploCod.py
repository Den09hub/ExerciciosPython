a ={}
a['descrição'] = str(input("digite a descrição de sua tarefa: "))
s = int(input("digite o status da tarefa: 1-CONCLUIDO 2 - NÃO CONCLUIDO"))
if s ==1:
    a['status'] = 'CONCLUIDO'
elif s==2:
    a['status'] = 'NÃO CONCLUIDO'
print(a)
for t,x in a.items():
    print(f'{t} contem {x}')

