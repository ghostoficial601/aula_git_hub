livros = []

while True:
    adicionar = str(input('\nGostaria de adicionar +1 livro?\n -> '))

    if adicionar in ['s', 'sim']:
# essa parte abaixo "livros" para vc pode escrever as descrições
        titulo = str(input('\nEscreva o nome do titulo do Livro: '))
        autor = str(input('\nEscreva o nome do autor do Livro: '))
        ano = int(input('\nEm que ano esse livro foi escrito?\n -> '))

        livro = {
            'Titulo': titulo,
            'Autor': autor,
            'Ano': ano
        }

        livros.append(livro)

    if adicionar == 'vizualizar':
        print('\n')
        for i, p in enumerate(livros, 1):
            print(f'{i}. Titulo:{p["Titulo"]}, Autor:{p["Autor"]}, Ano:{p["Ano"]}')
    if adicionar in ['n', 'não']:
        print('\nencerrando')
        break
