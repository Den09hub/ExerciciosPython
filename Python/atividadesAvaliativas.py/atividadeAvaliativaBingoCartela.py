import random

class CartelaBingo:
    def __init__(self):
        self.cartelaB = []
        self.cartelaI = []
        self.cartelaN = []
        self.cartelaG = []
        self.cartelaO = []
    
    def gerando_cartela(self):
        while len(self.cartelaB) != 5:
            b = random.randint(1, 15)
            if b not in self.cartelaB:
                self.cartelaB.append(b)

        while len(self.cartelaI) != 5:
            i = random.randint(16, 30)
            if i not in self.cartelaI:
                self.cartelaI.append(i)

        while len(self.cartelaN) != 5:
            n = random.randint(31, 45)
            if n not in self.cartelaN:
                self.cartelaN.append(n)

        while len(self.cartelaG) != 5:
            g = random.randint(46, 60)
            if g not in self.cartelaG:
                self.cartelaG.append(g)

        while len(self.cartelaO) != 5:
            o = random.randint(61, 75)
            if o not in self.cartelaO:
                self.cartelaO.append(o)
        
        self.cartelaN[2] = 'X'

    def exibir_cartela(self):
        print('BEM', 'VINDO AO BINGO!', sep= '-')
        print('B  I  N  G  O')
        print(self.cartelaB[0],self.cartelaI[0],self.cartelaN[0],self.cartelaG[0],self.cartelaO[0])
        print(self.cartelaB[1],self.cartelaI[1],self.cartelaN[1],self.cartelaG[1],self.cartelaO[1])
        print(self.cartelaB[2],self.cartelaI[2],self.cartelaN[2],self.cartelaG[2],self.cartelaO[2])
        print(self.cartelaB[3],self.cartelaI[3],self.cartelaN[3],self.cartelaG[3],self.cartelaO[3])
        print(self.cartelaB[4],self.cartelaI[4],self.cartelaN[4],self.cartelaG[4],self.cartelaO[4])

    def verificar_numero(self):
        marcacao = int(input('Digite a fim de marcar o número sorteado: '))
        if marcacao >= 1 and marcacao <= 15:
            for i in range(len(self.cartelaB)):
                if marcacao == self.cartelaB[i]:
                    self.cartelaB[i] = 'X'

        if marcacao >= 16 and marcacao <= 30:
            for i in range(len(self.cartelaI)):
                if marcacao == self.cartelaI[i]:
                    self.cartelaI[i] = 'X'

        if marcacao >= 31 and marcacao <= 45:
            for i in range(len(self.cartelaN)):
                if marcacao == self.cartelaN[i]:
                    self.cartelaN[i] = 'X'

        if marcacao >= 46 and marcacao <= 60:
            for i in range(len(self.cartelaI)):
                if marcacao == self.cartelaG[i]:
                    self.cartelaG[i] = 'X'

        if marcacao >= 61 and marcacao <= 75:
            for i in range(len(self.cartelaO)):
                if marcacao == self.cartelaO[i]:
                    self.cartelaO[i] = 'X'

    def verificar_coluna(self):
        if self.cartelaB[0] == 'X' and self.cartelaB[1] == 'X' and self.cartelaB[2] == 'X' and self.cartelaB[3] == 'X' and self.cartelaB[4] == 'X':
            print('BINGO!')
        if self.cartelaI[0] == 'X' and self.cartelaI[1] == 'X' and self.cartelaI[2] == 'X' and self.cartelaI[3] == 'X' and self.cartelaI[4] == 'X':
            print('BINGO!')
        if self.cartelaN[0] == 'X' and self.cartelaN[1] == 'X' and self.cartelaN[2] == 'X' and self.cartelaI[3] == 'X' and self.cartelaN[4] == 'X':
            print('BINGO!')
        if self.cartelaG[0] == 'X' and self.cartelaG[1] == 'X' and self.cartelaG[2] == 'X' and self.cartelaG[3] == 'X' and self.cartelaG[4] == 'X':
            print('BINGO!')
        if self.cartelaO[0] == 'X' and self.cartelaO[1] == 'X' and self.cartelaO[2] == 'X' and self.cartelaO[3] == 'X' and self.cartelaO[4] == 'X':
            print('BINGO!')

    def verificar_linha(self):
        if self.cartelaB[0] == 'X' and self.cartelaI[0] == 'X' and self.cartelaN[0] == 'X' and self.cartelaG[0] == 'X' and self.cartelaO[0] == 'X':
            print('BINGO!')
        if self.cartelaB[1] == 'X' and self.cartelaI[1] == 'X' and self.cartelaN[1] == 'X' and self.cartelaG[1] == 'X' and self.cartelaO[1] == 'X':
            print('BINGO!')
        if self.cartelaB[2] == 'X' and self.cartelaI[2] == 'X' and self.cartelaN[2] == 'X' and self.cartelaG[2] == 'X' and self.cartelaO[2] == 'X':
            print('BINGO!')
        if self.cartelaB[3] == 'X' and self.cartelaI[3] == 'X' and self.cartelaN[3] == 'X' and self.cartelaG[3] == 'X' and self.cartelaO[3] == 'X':
            print('BINGO!')
        if self.cartelaB[4] == 'X' and self.cartelaI[4] == 'X' and self.cartelaN[4] == 'X' and self.cartelaG[4] == 'X' and self.cartelaO[4] == 'X':
            print('BINGO!')

    def verificar_diagonal(self):
        if self.cartelaB[0] == 'X' and self.cartelaI[1] == 'X' and self.cartelaN[2] == 'X' and self.cartelaG[3] == 'X' and self.cartelaO[4] == 'X':
            print('BINGO!')
        if self.cartelaB[4] == 'X' and self.cartelaI[3] == 'X' and self.cartelaN[2] == 'X' and self.cartelaG[1] == 'X' and self.cartelaO[0] == 'X':
            print('BINGO!')

        


cartela1 = CartelaBingo()
cartela1.gerando_cartela()
while True:
    cartela1.exibir_cartela()
    cartela1.verificar_coluna()
    cartela1.verificar_linha()
    cartela1.verificar_diagonal()
    cartela1.verificar_numero()

