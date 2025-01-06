class Aluno:
    def __init__(self, nome_aluno, RA_aluno, nota1, nota2, nota3, nota4):
        self.nome_aluno = nome_aluno
        self.RA_aluno = RA_aluno
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4

    def media_do_aluno(self):
        return (self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4
    
    def situacao_do_aluno(self):
        media = (self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4
        if media < 5:
            print('Reprovado')
        elif media > 5 and media < 7:
            print('Exame')
        elif media > 6.9:
            print('Aprovado')
        
    def mostrar_media(self):
        print(f'Aluno: {self.nome_aluno}, RA: {self.RA_aluno}, Média: {self.media_do_aluno()}')

aluno1 = Aluno('John', 201720040973, 10, 9, 9, 8)
aluno1.mostrar_media()
aluno1.situacao_do_aluno()

aluno2 = Aluno('Nina', 201820051884, 6, 7, 7, 7)
aluno2.mostrar_media()
aluno2.situacao_do_aluno()

aluno3 = Aluno('Wilson', 202019992965, 3, 4, 4, 4)
aluno3.mostrar_media()
aluno3.situacao_do_aluno()
    

        