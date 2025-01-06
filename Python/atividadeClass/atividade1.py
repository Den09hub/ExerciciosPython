class Carro:
    cor = 'Sem cor'
    marca = 'Sem marca'
    modelo = 'Sem modelo'
    ano = 2010
    km_rodados = 0
    status_motor = 'Desligado'
    status_movimento = 'Parado'

    def detalhes(self):
        print(f'{self.cor}')
        print(f'{self.marca}')
        print(f'{self.modelo}')
        print(f'{self.ano}')
        print(f'{self.km_rodados}')

    def Adicionarkm(self,km):
        self.km_rodados += km

    def metodos(self):
        self.status_motor = 'Ligado'
        self.status_movimento = 'Andando'
        print(f'Status do motor: {self.status_motor}')
        print(f'Status do movimento do carro: {self.status_movimento}')
                
carro1 = Carro()
carro1.cor = 'Amarelo'
carro1.marca = 'Honda'
carro1.modelo = 'HR-V'
carro1.ano = 2024
carro1.Adicionarkm(50)
carro1.detalhes()
carro1.metodos()

carro2 = Carro()
carro2.cor = 'Vermelho'
carro2.marca = 'NISSAN'
carro2.modelo = 'GTR'
carro2.ano = 2024
carro2.Adicionarkm(10)
carro2.detalhes()
carro2.metodos()
