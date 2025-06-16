# Lista que vai armazenar as pessoas
pessoas = []
nome_femininos = []
idades = []
qtd = 0
p_acima = []
# Loop principal
while True:
    escolha = input('Quer adicionar +1 pessoa? (sim/não): ').strip().lower()
    
    if escolha in ['s', 'sim']:

        nome = input('Escreva um nome: ')
        idade = int(input('Escreva a idade: '))
        idades.append(idade)
        genero = input('Escreva o gênero: ')
        if genero == 'feminino':
            nome_femininos.append(nome)
        # Criando dicionário com os dados da pessoa
        pessoa = {
            'nome': nome,
            'idade': idade,
            'genero': genero
        }

        # Adiciona o dicionário na lista
        pessoas.append(pessoa)
        qtd += 1
        

    elif escolha in ['n', 'nao', 'não']:
        print('\nLista de pessoas cadastradas:')
        for i, p in enumerate(pessoas, 1):
            print(f'{i}. Nome: {p["nome"]}, Idade: {p["idade"]}, Gênero: {p["genero"]}')
        mediana = sum(idades) / qtd
        if idade > mediana:
            p_acima.append(nome)
        

        print(f'O numero de pessoas cadastradas foi {qtd} e a mediana das idade foi {mediana} e os nomes femininos são {nome_femininos} e as pessoas com idades acima da média são {p_acima}')
        break

    else:
        print('Resposta inválida. Digite "sim" ou "não".')
