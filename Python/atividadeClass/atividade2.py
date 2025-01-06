class Pessoa:
    nome = 'John'
    idade = 0
    endereco = 'Rua: Aicas, Número da casa: 1635'

    def detalhes(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Endereço: {self.endereco}')

    def idade_pessoa(self):
        self.idade = int(input('Alterar idade: '))

pessoa_detalhes = Pessoa()
pessoa_detalhes.detalhes()
pessoa_detalhes.idade_pessoa()
pessoa_detalhes.detalhes()

    

