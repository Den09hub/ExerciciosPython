class Filme_Cinema:
    def __init__(self, nome, duracao):
        self.nome = nome
        self.duracao = duracao

    def play_filme(self):
        print(f'Play...Iníciando {self.nome}')
        print(f'Duração: {self.duracao}')

class Acao(Filme_Cinema):
    def __init__(self, nome, duracao):
        super().__init__(nome, duracao)
        print('\nExplosão')

class Drama(Filme_Cinema):
    def __init__(self, nome, duracao):
        super().__init__(nome, duracao)
        print('\nLágrimas')

class Suspense(Filme_Cinema):
    def __init__(self, nome, duracao):
        super().__init__(nome, duracao)
        print('\nAflição')

primeiro_filme_acao = Acao('John Wick 4', '2:49:00')
primeiro_filme_acao.play_filme()
segundo_filme_drama = Drama('A Origem', '2:28:00')
segundo_filme_drama.play_filme()
terceiro_filme_suspense = Suspense('Onde os Fracos Não Têm Vez', '2:02:00')
terceiro_filme_suspense.play_filme()


 

