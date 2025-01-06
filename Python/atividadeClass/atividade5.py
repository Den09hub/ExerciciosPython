class Conta:
    def __init__(self, nome_cliente, cpf_cliente, numero_codigo, saldo_cliente):
        self.nome_cliente = nome_cliente
        self.cpf_cliente = cpf_cliente
        self.numero_codigo = numero_codigo
        self.saldo_cliente = saldo_cliente

    def depositar_conta(self):
        self.saldo_cliente += float(input('Deposite uma quantidade: '))
        print('Depositado com sucesso')

    def sacar_conta(self):
        self.saldo_cliente -= float(input('Sacar: '))
        print('Concluído')

    def imprimir_informacoes(self):
        print(f'Nome: {self.nome_cliente}, CPF: {self.cpf_cliente}, Número: {self.numero_codigo}')
        print(f'Saldo Atual: R${self.saldo_cliente}')

cliente1 = Conta('John', 12345678912, 9876, 0)
cliente1.imprimir_informacoes()
cliente1.depositar_conta()
cliente1.imprimir_informacoes()
cliente1.sacar_conta()
cliente1.imprimir_informacoes()