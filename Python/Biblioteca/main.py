from biblioteca import Biblioteca
from livros import Livros

def ExibirMenu():
    print('1. Adicionar Livro')
    print('2. Consultar destalhes do livro')
    print('3. Emprestar um livro')
    print('4. Listar todos os livros da biblioteca')
    print('5. Devolver livro')
    print('6. Sair')

biblioteca = Biblioteca()
while True:
    ExibirMenu()
    op = int(input('Digite a opção: '))

    if op == 1:
        titulo = input('Digite o titulo do livro: ')
        autor = input('Digite o autor do livro: ')
        livro = Livros(titulo, autor)
        biblioteca.AdicionarLivro(livro)

    elif op == 2:
        titulo = input('Digite o titulo que quer buscar: ')
        detalhes = biblioteca.ConsultarDetalhe(titulo)
        print(detalhes)

    elif op == 3:
        titulo = input('Digite o titulo que quer buscar: ')
        biblioteca.EmprestarLivro(titulo)

    elif op == 4:
        biblioteca.ListarLivros()
    
    elif op == 5:
        titulo = input('Digite o titulo que quer buscar: ')

    elif op == 6:
        break