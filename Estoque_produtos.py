import os
from manipulando_db.manipulacao import adicionar_produtos
from manipulando_db.manipulacao import visualizar_estoque
from manipulando_db.manipulacao import atualizar_estoque
from manipulando_db.manipulacao import atualizar_produto
from manipulando_db.manipulacao import verificador_codigo_produto

while True:

    print('\t\tControle de estoque')

    print('1 - Vizualizar estoque')
    print('2 - Atualizar estoque')
    print('3 - Adicionar produto ao estoque')
    print('4 - Atualizar produto ex:(Código, descrição...)')
    print('5 - Excluir protudo de estoque')

    opcao = int(input('> '))

    if opcao == 1:
        os.system('cls')
        visualizar_estoque()

    elif opcao == 2:
        os.system('cls')
        atualizar_estoque()
        os.system('cls')
        visualizar_estoque()

    elif opcao == 3:
        codigo_do_produto = int(input('Código do produto novo: '))
        while verificador_codigo_produto(codigo_do_produto) == False:
            if codigo_do_produto == 0:
                break
            print('O código do produto digitado já existe!')
            codigo_do_produto = int(input('Código do produto novo: '))

        if verificador_codigo_produto(codigo_do_produto) == False:
            pass
        else:
            descricao_do_produto = 'Brinco'
            preco_de_compra = 15
            preco_de_venda = 25
            quantidade_estoque = 4

            adicionar_produtos(codigo_do_produto,
                               descricao_do_produto,
                               preco_de_compra,
                               preco_de_venda,
                               quantidade_estoque)

    elif opcao == 5:
        atualizar_produto()