class Carro:
    def __init__(self, modelo, marca, cor, ano, valor, nivel, consumo):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.ano = ano
        self.valor = valor
        self.nivel = nivel
        self.consumo = consumo

    def abastecer_carro(self):
        self.nivel = int(input('Digite uma quantidade para abastecer o Carro: '))
        print(f'Carro abastecido. Nível: {self.nivel}')

    def andar_carro(self):
        self.consumo = int(input('Digite o quanto o carro percorrerá em km: '))
        print(f'O carro percorreu {self.consumo}km')
    
    def verificar_carro(self):
        self.consumo = self.consumo // self.nivel
        print(f'Foram gasto {self.consumo} litros')

    def calcular_imposto(self):
        print(f'O imposto do IPVA do carro será R${(190900*2.5)//190:.2f}')

carro1 = Carro('SUV', 'Hyundai Creta Action', 'Preto', 2024, 'R$190.900', 0, 0)
carro1.abastecer_carro()
carro1.andar_carro()
carro1.verificar_carro()
carro1.calcular_imposto()
        