numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1>numero2:
    print(f"O {numero1} é maior que o {numero2}")
    
else:
    if numero2>numero1:
        print(f"O {numero2} é maior que o {numero1}")
    if numero1 == numero2:
        print(f"O {numero1} e {numero2} tem o mesmo valor")