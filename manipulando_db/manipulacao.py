import sqlite3
import pandas as pd

# Essa função converte a tebela do banco de dados para visualização
def visualizar_estoque():
    # Conectenando ao banco de dados
    banco = sqlite3.connect('D:/Python/Estoque/Banco.db')
    cursor = banco.cursor()
    cursor.execute('SELECT * FROM produtos')
    lista = cursor.fetchall()  # Essa variavel recebe o banco de dados

    lista1 = []
    contagem = 0
    codigo = []
    descricao_produto = []
    preco_compra = []
    preco_venda = []
    estoque = []

    # Esse FOR o banco de dados é convertido para listas
    # e assim separando os valores para cada variavel
    for _ in range(len(lista)):
        lista1.append(list(lista[contagem]))

        lista_dividida = lista1[contagem]
        # Cada lista irá receber um valor referente
        codigo.append(lista_dividida[0])
        descricao_produto.append(lista_dividida[1])
        preco_compra.append(lista_dividida[2])
        preco_venda.append(lista_dividida[3])
        estoque.append(lista_dividida[4])

        contagem = contagem + 1

    tabela = {'Codigo': codigo,
              'Descrição': descricao_produto,
              'PreçoCompra': preco_compra,
              'PreçoVenda': preco_venda,
              'Estoque': estoque}

    dados = pd.DataFrame(tabela)
    print(dados)


# Essa função adiciona produtos na tabela de controle de estoque
def adicionar_produtos(codigo, descricao, preco_compra, preco_venda, estoque):
    banco = sqlite3.connect('D:/Python/Estoque/Banco.db')
    cursor = banco.cursor()
    cursor.execute(f'INSERT INTO produtos VALUES({codigo}, "{descricao}", {preco_compra},{preco_venda}, {estoque})')

    banco.commit()
    banco.close()


# Essa função atualiza as unidades dos produtos do estoque
def atualizar_estoque():
    visualizar_estoque()
    produto = int(input('Código do produto: '))
    quantidade = int(input('Quantidade para o estoque: '))

    # Conectando ao banco
    banco = sqlite3.connect('D:/Python/Estoque/Banco.db')
    cursor = banco.cursor()

    cursor.execute(f'SELECT Quantidade_estoque FROM produtos WHERE Codigo_produto="{produto}"')
    lista = cursor.fetchall()
    lista1 = list(lista[0])
    lista2 = lista1[0]

    cursor.execute(f'UPDATE produtos SET Quantidade_estoque = {quantidade + lista2} WHERE Codigo_produto = {produto}')

    banco.commit()
    banco.close()


# Essa função possibilita a alteração de algo de um produto especifico
def atualizar_produto():
    banco = sqlite3.connect('D:/Python/Estoque/Banco.db')
    cursor = banco.cursor()


def verificador_codigo_produto(produto_codigo):
    lista1 = []
    banco = sqlite3.connect('D:/Python/Estoque/Banco.db')
    cursor = banco.cursor()
    cursor.execute(f'SELECT Codigo_produto FROM produtos')
    lista = cursor.fetchall()
    for i in range(len(lista)):
        lista1.append(list(lista[i]))
        if lista1[i] != [produto_codigo]:
            pass
        else:
            return False
