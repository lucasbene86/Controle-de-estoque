import os

from manipulando_db.manipulacao import adicionar_produtos
from manipulando_db.manipulacao import visualizar_estoque
from manipulando_db.manipulacao import atualizar_estoque
from manipulando_db.manipulacao import atualizar_produto
from manipulando_db.manipulacao import verificador_codigo_produto
from manipulando_db.manipulacao import excluir_produto_estoque

while True:
    os.system('cls')
    visualizar_estoque()

    print('\t\tControle de estoque\n')
    
    print('1 - Vizualizar estoque')
    print('2 - Atualizar estoque')
    print('3 - Adicionar produto ao estoque')
    print('4 - Atualizar produto ex:(Código, descrição...)')
    print('5 - Excluir protudo do estoque')

    opcao = int(input('> '))

    # Visualizar estoque
    if opcao == 1:
        os.system('cls')
        visualizar_estoque()

    # Atualizar estoque
    elif opcao == 2:
        os.system('cls')
        atualizar_estoque()
        os.system('cls')
        visualizar_estoque()

    # Adicionar produto ao estoque
    elif opcao == 3:
        os.system('cls')
        codigo_do_produto = int(input('Código do produto novo: '))
        while verificador_codigo_produto(codigo_do_produto) is False:
            if codigo_do_produto == 0:
                break
            print('O código do produto digitado já existe!')
            codigo_do_produto = int(input('Código do produto novo: '))

        if verificador_codigo_produto(codigo_do_produto) is False:
            pass
        else:
            descricao_do_produto = str(input('Nome do produto:'))
            preco_de_compra = float(input('Preço de compra: R$'))
            preco_de_venda = float(input('Preço de venda: R$'))
            quantidade_estoque = int(input('Qualidade de estoque disponivel:'))

            adicionar_produtos(codigo_do_produto,
                               descricao_do_produto,
                               preco_de_compra,
                               preco_de_venda,
                               quantidade_estoque)

    # Atualizar produto 
    elif opcao == 4:
        os.system('cls')
        print('\tSelecione a opção para edição\n')
        print('1 - Editar código do produto:')
        print('2 - Editar descrição do produto:')
        print('3 - Editar Valor de compra do produto:')
        print('4 - Editar valor de venda do produto:')
        opcao = int(input('> '))

        # Opção para editar o código do produto
        if opcao == 1:
            visualizar_estoque()
            codigo_para_alterar = int(input(
                    'Digite o código que será alterado: '))

            valor = int(input('Digite o novo código: '))
            while verificador_codigo_produto(valor) is True:
                print('Valor de código já existente!\n')
                valor = int(input('Digite o novo código: '))

            if verificador_codigo_produto(valor) is True:
                pass
            else:
                atualizar_produto(codigo_para_alterar, valor, opcao)
        
        # Opção para editar a descrição do produto
        elif opcao == 2:
            visualizar_estoque()
            codigo_para_alterar = int(input(
                    'Digite o código do produto que será alterado: '))
            descricao_nova = str(input('Digite a nova descrição: '))
            atualizar_produto(codigo_para_alterar, descricao_nova, opcao)

    # Excluir produto do estoque
    elif opcao == 5:
        os.system('cls')
        visualizar_estoque()
        excluir_produto_estoque()
        os.system('cls')
