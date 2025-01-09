import connection as sql
from classes.product import Product
import os
import time

def menuProdutos():
    dadosProdutos = sql.cursor.execute("SELECT MAX(CODIGO) OVER (), * FROM PRODUTOS (NOLOCK)").fetchall()
    os.system("cls")
    print("Menu de produtos!\n Selecione qual opção deseja seguir:\n"
          "1 - Cadastrar novo produto\n"
          "2 - Atualizar cadastro de produto\n"
          "3 - Consultar produtos\n"
          "4 - Excluir produtos\n")
    opMenuProd = input("Digite qual opção deseja seguir: ")
    if opMenuProd not in ("1","2","3","4"):
        print("O valor digitado deve estar entre as opções acima.")
        input("Pressione Enter para prosseguir")
        menuProdutos()
    match opMenuProd:
        case "1": cadastrarProduto(dadosProdutos)
        case "2": atualizarCadProduto(dadosProdutos)
        case "3": consultarProduto(dadosProdutos)
        case "4": excluirProduto(dadosProdutos)

#CADASTRAR PRODUTO
def cadastrarProduto(dadosProdutos):
    os.system("cls")
    print("Digite os dados do produto para cadastro: ")
    if len(dadosProdutos) == 0:
        codigo = 1
    else:
        codigo = dadosProdutos[0][0] + 1
    nome = input("Nome: ")
    valor = input("Preço: ")
    produto = Product(codigo, nome, valor)
    try:
        sql.cursor.execute(f"INSERT INTO PRODUTOS VALUES ({codigo}, '{nome}', '{valor}')")
        sql.connection.commit()
        print(produto.informacoes)
        print("Produto cadastrado com sucesso!")
        time.sleep(5)
    except:
        sql.connection.rollback()
        print("Falha na gravação dos dados! Verifique os valores digitados e, caso o erro persista, entre em contato com o administrador.")
        time.sleep(5)
    menuProdutos()

#ATUALIZAR CADASTRO DE UM PRODUTO
def atualizarCadProduto(dadosProdutos):
    pass

#CONSULTAR UM PRODUTO
def consultarProduto(dadosProdutos):
    pass

#EXCLUIR UM PRODUTO
def excluirProduto(dadosProdutos):
    os.system("cls")
    codProduto = int(input("Digite o código do produto a ser excluído: "))
    listaCodigos = []
    for produto in dadosProdutos:
        listaCodigos.append(produto[1])
    if codProduto not in listaCodigos:    
        print("O produto digitado não está presente no sistema!")
    else:
        produto = sql.cursor.execute(f"SELECT * FROM PRODUTOS (NOLOCK) WHERE CODIGO = {codProduto}").fetchone()
        objProduto = Product(produto[0], produto[1], produto[2])
        try:
            sql.cursor.execute(f"DELETE FROM PRODUTOS WHERE CODIGO = {codProduto}")
            print("O seguinte produto será removido:")
            print(objProduto.informacoes)
            sql.connection.commit()
            print("Produto removido com sucesso!")
        except:
            sql.cursor.rollback()
            print("Falha na remoção do produto! Verifique o valor digitado e, caso o problema persista, entre em contato com o administrador.")
    input("Pressione Enter para continuar")
    menuProdutos()