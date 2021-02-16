import sqlite3

from prettytable import PrettyTable


# Essa função converte a tebela do banco de dados para visualização
def visualizar_estoque():
    # Conectenando ao banco de dados
    banco = sqlite3.connect('D:/Python/Estoque/Banco.db')
    cursor = banco.cursor()
    cursor.execute('SELECT * FROM produtos')
    dados_db = cursor.fetchall()  # Essa variavel recebe o banco de dados

    lista1 = []
    codigo = []
    descricao_produto = []
    preco_compra = []
    preco_venda = []
    estoque = []

    # Cria a tabela
    tabela = PrettyTable(['Código',
                          'Descrição',
                          'Preço Compra',
                          'Preço Venda',
                          'Estoque'])

    # Alinha as colunas
    tabela.align["Código"] = "l"  # lado esquero
    tabela.align["Descrição"] = "l"  # lado esquerdo
    tabela.align["Preço Compra"] = "c"  # centro
    tabela.align["Preço Venda"] = "r"  # lado direito
    tabela.align["Estoque"] = "r"  # lado direito

    contagem = 0
    '''Esse FOR o banco de dados é convertido para listas
     e assim separando os valores para cada variavel'''
    for _ in range(len(dados_db)):
        lista1.append(list(dados_db[contagem]))

        lista_dividida = lista1[contagem]
        # Cada lista irá receber um valor referente
        codigo.append(lista_dividida[0])
        descricao_produto.append(lista_dividida[1])
        preco_compra.append(lista_dividida[2])
        preco_venda.append(lista_dividida[3])
        estoque.append(lista_dividida[4])
        
        tabela = PrettyTable()
        tabela.add_column('Código', codigo)
        tabela.add_column('Descrição', descricao_produto)
        tabela.add_column('Preço de compra', preco_compra)
        tabela.add_column('Preço de venda', preco_venda)
        tabela.add_column('Estoque', estoque)

        contagem = contagem + 1
    
    # Deixa um espaço entre a borda das colunas e o conteúdo
    tabela.padding_width = 1

    # Determina se a primeira linha vem em letras maiúsculas ou não
    tabela.header_style = 'upper'  # Todas maiúsculas
    print(tabela)


# Essa função adiciona produtos na tabela de controle de estoque
def adicionar_produtos(codigo, descricao, preco_compra, preco_venda, estoque):
    banco = sqlite3.connect('D:/Python/Estoque/Banco.db')
    cursor = banco.cursor()
    cursor.execute(f'INSERT INTO produtos VALUES({codigo}, "{descricao}",'
                   f'{preco_compra},{preco_venda}, {estoque})')

    banco.commit()
    banco.close()


# Essa função atualiza as unidades dos produtos do estoque
def atualizar_estoque():
    visualizar_estoque()

    codigo_produto = int(input('Código do produto ou 0 para sair da opção: '))

    if codigo_produto != 0:
        while verificador_codigo_produto(codigo_produto) is not True:
            print('Código não existente!\n')
            codigo_produto = int(input('Código do produto: '))

            if codigo_produto == 0:
                return print('Função cancelada!')

        quantidade = int(input('Quantidade para o estoque: '))

        # Conectando ao banco
        banco = sqlite3.connect('D:/Python/Estoque/Banco.db')
        cursor = banco.cursor()
        cursor.execute(f'SELECT Quantidade_estoque FROM produtos '
                       f'WHERE Codigo_produto = "{codigo_produto}"')

        dados_db = cursor.fetchall()
        dados_em_lista = list(dados_db[0])
        quantidade_do_estoque = dados_em_lista[0]

        cursor.execute(f'UPDATE produtos SET Quantidade_estoque = {quantidade + quantidade_do_estoque} WHERE Codigo_produto = {codigo_produto}')

        banco.commit()
        banco.close()
    
    else:
        return print('Função cancelada!')


# Essa função possibilita a alteração de algo de um produto especifico.
def atualizar_produto(codigo_para_alteracao, valor, opcao):
    banco = sqlite3.connect('D:/Python/Estoque/Banco.db')
    cursor = banco.cursor()

    # Altera o codigo do produto.
    if opcao == 1:
        cursor.execute('UPDATE produtos SET Codigo_produto = '
                f'{valor} WHERE Codigo_produto = {codigo_para_alteracao}')

    # Altera a descrição do produto.
    elif opcao == 2:
        cursor.execute('UPDATE produtos SET Descrição_produto = '
                f'"{valor}" WHERE Codigo_produto = {codigo_para_alteracao}')

    # altera o preço de compra do produto.
    elif opcao == 3:
        cursor.execute('UPDATE produtos SET Preço_compra = '
                f'{valor} WHERE Codigo_produto = {codigo_para_alteracao}')

    elif opcao == 4:
        cursor.execute('UPDATE produtos SET Preço_venda = '
                f'{valor} WHERE Codigo_produto = {codigo_para_alteracao}')

    banco.commit()
    banco.close()


# Essa função verifica se já existe algum produto no estoque para não se repetir
def verificador_codigo_produto(codigo_produto):
    lista_codigos = []

    banco = sqlite3.connect('D:/Python/Estoque/Banco.db')
    cursor = banco.cursor()
    cursor.execute('SELECT Codigo_produto FROM produtos')
    dados_db = cursor.fetchall()

    for contagem in range(len(dados_db)):
        lista_codigos.append(list(dados_db[contagem]))

        if lista_codigos[contagem] != [codigo_produto]:
            pass
        else:
            return True


# Essa função possibilita excluir algum produto do estoque.
def excluir_produto_estoque():
    codigo = int(input('Digite o código do produto'
                       'que deseja exluir ou 0 para cancelar: '))
    
    if codigo != 0:
        #Enquanto o codigo digitado não existir, ficar no loop while.
        while verificador_codigo_produto(codigo) is not True:
            print('Código não existente!!!\n')
            codigo = int(input('Digite o código do produto'
                               'que deseja exluir ou 0 para cancelar: '))
            if codigo == 0:
                return

        banco = sqlite3.connect('D:/Python/Estoque/Banco.db')
        cursor = banco.cursor()
        cursor.execute(f'DELETE FROM produtos WHERE Codigo_produto = "{codigo}"')

        banco.commit()
        banco.close()
    
    else:
        return 
