class Funcionario:
    def __init__(self, nome, sobrenome, horas_trabalhadas, valor_hora):
        self.nome = nome
        self.sobrenome = sobrenome
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def NomeCompleto(self):
        print(f'Nome Completo: {self.nome + self.sobrenome}')

    def CalcularSalario(self):
        print(f'Salário do Mês: R${self.horas_trabalhadas * self.valor_hora}')
    
cliente1 = Funcionario('Jonh', ' Wick', 20, 10500)
cliente1.NomeCompleto()
cliente1.CalcularSalario()
