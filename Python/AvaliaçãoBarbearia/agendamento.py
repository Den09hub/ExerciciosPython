class Agendamentos:
    def __init__(self, nome, data, hora, servico):
        self.nome = nome
        self.data = data
        self.hora = hora
        self.servico = servico

    def __str__(self):
        return f'Agendado = Nome: {self.nome}; Data: {self.data}; Horário: {self.hora}; Serviço: {self.servico}.'
        