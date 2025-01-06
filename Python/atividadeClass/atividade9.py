class Triangulo:
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def calculo_perimetro(self):
        self.ladoA = float(input('Digite a medida do lado A: '))
        self.ladoB = float(input('Digite a medida do lado B: '))
        self.ladoC = float(input('Digite a medida do lado C: '))
        print(f'\nPerímetro total: {self.ladoA + self.ladoB + self.ladoC}cm')

    def maior_lado(self):
        print('O maior lado é')
        print(max(self.ladoA, self.ladoB, self.ladoC))

triangulo1 = Triangulo(0, 0, 0)
triangulo1.calculo_perimetro()
triangulo1.maior_lado()