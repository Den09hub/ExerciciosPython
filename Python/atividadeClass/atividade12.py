class Pessoa:
    def __init__(self, matricula, nome, idade):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade

class Aluno:
    def __init__(self, matricula, nome, idade):
        super().__init__(matricula, nome, idade)
    def __init__(self, nota1, nota2, nota3, media):
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.media = media

    def aluno_estudar(self):
        print(f'O aluno {self.nome} está estudando')

class Professor:
    def __init__(self, matricula, nome, idade):
        super().__init__(matricula, nome, idade)
    def __init__(self, formacao, disciplina, carga_horaria, salario):
        self.formacao = formacao
        self.disciplina = disciplina
        self.carga_horaria = carga_horaria
        self.salario = salario

    def calcular_media_aluno(self):
        self.media = (self.nota1 + self.nota2 + self.nota3) / 3
        print(f'A média do aluno {self.nome} é {self.media}')

aluno1 = Pessoa(124, 'Jason', 18)
aluno1 = Aluno(7, 6, 8, 0)
aluno1.aluno_estudar()

Professor1 = Pessoa(1024, 'Chucky', 33)
Professor1 = Professor('Professor', 'Física', 15, 5000)
Professor1.calcular_media_aluno()


