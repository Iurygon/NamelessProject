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
    pass