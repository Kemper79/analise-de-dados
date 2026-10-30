from time import process_time_ns

import matplotlib.pyplot as plt

class Livro:
    def __init__(self, titulo, autor, genero, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade = quantidade
livros = []

def cadastrar_livros():
    titulo = input('Digite o titulo do livro: ')
    autor = input('Qual o nome do autor do livro? ')
    genero = input('Digite o genero do livro: ')
    quantidade = int(input('Digite a quantidade de livros: '))

    livro = Livro(titulo, autor, genero, quantidade)
    livros.append(livro)

def listar_livros():
    if len(livros) == 0:
        print('Nenhum livro cadastrado')
        return
    print('\n--- LIVROS CADASTRADOS ---')

    for livro in livros:
        print(f'Titulo: {livro.titulo}')
        print(f'Autor: {livro.autor}')
        print(f'Genero: {livro.genero}')
        print(f'Quantidade: {livro.quantidade}')

def buscar_livro():

    buscar = input('Digite o livro que deseja buscar: ')
    encontrado = False

    for livro in livros:
        if livro.titulo.lower() == buscar.lower():
            print('\nLivro Encontrado!')
            print(f'Titulo: {livro.titulo}')
            print(f'Autor: {livro.autor}')
            print(f'Genero: {livro.genero}')
            print(f'Quantidade: {livro.quantidade}')
            encontrado = True
    if not encontrado:
        print('Livro nao encontrado')

def grafico():
    if len(livros) == 0:
        print('Nao existem livros cadastrados para gerar grafico. Por favor, cadastre um livro.')
        return
    generos = {}
    for livro in livros:
        if livro.genero in generos:
            generos[livro.genero] += livro.quantidade
        else:
            generos[livro.genero] = livro.quantidade
    plt.bar(generos.keys(), generos.values())

    plt.title('Quantidade de livros por Genero')
    plt.xlabel('Genero')
    plt.ylabel('Quantidade de livros')

    plt.show()

while True:
    print('\n===== SISTEMA DE CADASTROS E BUSCAS DE LIVROS =====')
    print('1 - Cadastrar livro')
    print('2 - Listar livro')
    print('3 - Buscar livro')
    print('4 - Gerar grafico')
    print('5 - Sair')

    opcao = input('Escolha uma opcao: ')

    if opcao == '1':
        cadastrar_livros()
    elif opcao == '2':
        listar_livros()
    elif opcao == '3':
        buscar_livro()
    elif opcao == '4':
        grafico()
    elif opcao == '5':
        print('SISTEMA ENCERRRADO')
        break
    else:
        print('Opcao invalida, tente novamente!')