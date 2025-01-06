class Livro:
    def __init__(self, nome, autor, editora, paginas ):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas

    def detalhes(self):
        print(f'Nome: {self.nome}')
        print(f'Autor: {self.autor}')
        print(f'Editora: {self.editora}')

    def alterar_detalhes(self):
        self.editora = input('Alterar editora: ')
        print(f'Nome: {self.nome}')
        print(f'Autor: {self.autor}')
        print(f'Editora: {self.editora}')
        print(f'Páginas: {self.paginas}')

    def listar_paginas(self):
        print(f'Páginas: {self.paginas}')

livro1 = Livro('John', 'William Gibson', 'Públicado por Wick', 250)
livro1.detalhes()
livro1.listar_paginas()
livro1.alterar_detalhes()