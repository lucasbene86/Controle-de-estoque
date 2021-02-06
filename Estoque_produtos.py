import os
from manipulando_db.manipulacao import adicionar_produtos
from manipulando_db.manipulacao import visualizar_estoque
from manipulando_db.manipulacao import atualizar_estoque
from manipulando_db.manipulacao import atualizar_produto
from manipulando_db.manipulacao import verificador_codigo_produto
from manipulando_db.manipulacao import excluir_produto_estoque

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
        os.system('cls')
        codigo_do_produto = int(input('Código do produto novo: '))
        while verificador_codigo_produto(codigo_do_produto) == False:
            if codigo_do_produto == 0:
                break
            print('O código do produto digitado já existe!')
            codigo_do_produto = int(input('Código do produto novo: '))

        if verificador_codigo_produto(codigo_do_produto) == False:
            pass
        else:
            descricao_do_produto = str(input('Nome do produto: '))
            preco_de_compra = float(input('Preço de compra: R$ '))
            preco_de_venda = float(input('Preço de venda: R$ '))
            quantidade_estoque = int(input('Qualidade de estoque disponivel: '))

            adicionar_produtos(codigo_do_produto,
                               descricao_do_produto,
                               preco_de_compra,
                               preco_de_venda,
                               quantidade_estoque)

    elif opcao == 4:
        os.system('cls')
        print('\tSelecione a opção para edição\n')
        print('1 - Editar código do produto:')
        print('2 - Editar descrição do produto:')
        print('3 - Editar Valor de compra do produto:')
        print('4 - Editar valor de venda do produto:')
        opcao = int(input('> '))
        atualizar_produto()

    elif opcao == 5:
        os.system('cls')
        visualizar_estoque()
        codigo = int(input('Digite o código do produto que deseja exluir: '))
        excluir_produto_estoque(codigo)
        os.system('cls')
