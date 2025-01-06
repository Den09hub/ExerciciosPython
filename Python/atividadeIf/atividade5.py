a =float(input("digite numero de a: "))
if a == 0:
    print("A equação não é do segundo grau.")
    exit()
b = float(input("Digite o número de b: "))
c = float(input("Digite o número de c: "))
delta = b ** 2 - 4 * a * c
if delta < 0:
    print("A equação não possui raízes reais.")
elif delta == 0:
    x = -b / (2 * a)
    print("A equação possui uma raiz real:", x)
else:
    x1 = (-b + delta ** 0.5) / (2 * a)
    x2 = (-b - delta ** 0.5) / (2 * a)
if delta > 0:
    print("A equação possui duas raízes reais:", x1, "e", x2)


