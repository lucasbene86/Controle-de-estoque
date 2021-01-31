import pandas as pd
import sqlite3
   

#Essa função converte a tebela do banco de dados para visualização
def visualizar_tabela():
    #Conectenando ao banco de dados
    banco = sqlite3.connect('D:/Python/Estoque/Banco.db')
    cursor = banco.cursor()
    cursor.execute('SELECT * FROM produtos')
    lista = cursor.fetchall() #Essa variavel recebe o banco de dados

    lista1 = []
    contagem = 0
    codigo = []
    descricao_produto = []
    preco_compra = []
    preco_venda = []
    estoque = []
    
    #Esse FOR o banco de dados é convertido para listas
    #e assim separando os valores para cada variavel
    for _ in range(len(lista)):
        lista1.append(list(lista[contagem]))
        
        lista_dividida = lista1[contagem]
        #Cada lista irá receber um valor referente
        codigo.append(lista_dividida[0])
        descricao_produto.append(lista_dividida[1])
        preco_compra.append(lista_dividida[2])
        preco_venda.append(lista_dividida[3])
        estoque.append(lista_dividida[4])

        contagem = contagem + 1

    tabela = {'Codigo':codigo,
          'Descrição':descricao_produto,
          'PreçoCompra':preco_compra,
          'PreçoVenda':preco_venda,
          'Estoque':estoque}

    dados = pd.DataFrame(tabela)
    print(dados)

#Essa função adiciona produtos na tabela de controle de estoque
def adicionar_produtos(codigo, descricao, preco_compra, preco_venda, estoque):
    banco = sqlite3.connect('D:/Python/Estoque/Banco.db')
    cursor = banco.cursor()
    cursor.execute(f'INSERT INTO produtos VALUES({codigo}, "{descricao}", {preco_compra}, {preco_venda}, {estoque})')
    
    banco.commit()
    banco.close()

codigo_do_produto = 410
descricao_do_produto = 'Escada'
preco_de_compra = 50
preco_de_venda = 150
quantidade_estoque = 20

adicionar_produtos(codigo_do_produto, descricao_do_produto, preco_de_compra, preco_de_venda, quantidade_estoque)

visualizar_tabela()