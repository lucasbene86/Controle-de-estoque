import pandas as pd
import sqlite3
   
banco = sqlite3.connect('D:/Python/Estoque/Banco.db')
cursor = banco.cursor()

cursor.execute('SELECT * FROM produtos')
lista = cursor.fetchall()
lista1 = []
contagem = 0
codigo = []
descricao = []
preco_compra = []
preco_venda = []
estoque = []

for i in range(len(lista)):
    lista1.append(list(lista[contagem]))

    lista_dividida = lista1[contagem]
    codigo.append(lista_dividida[0])
    descricao.append(lista_dividida[1])
    preco_compra.append(lista_dividida[2])
    preco_venda.append(lista_dividida[3])
    estoque.append(lista_dividida[4])

    contagem = contagem + 1

print(type(codigo))

tabela = {'Codigo':codigo,
          'Descrição':descricao,
          'PreçoCompra':preco_compra,
          'PreçoVenda':preco_venda,
          'Estoque':estoque}

dados = pd.DataFrame(tabela)
print(dados)