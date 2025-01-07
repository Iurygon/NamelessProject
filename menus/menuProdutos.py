import connection as sql
import os

def menuProdutos():
    dadosProdutos = sql.cursor.execute("SELECT MAX(CODIGO), * FROM PRODUTOS (NOLOCK)").fetchall()
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
    pass

#ATUALIZAR CADASTRO DE UM PRODUTO
def atualizarCadProduto(dadosProdutos):
    pass

#CONSULTAR UM PRODUTO
def consultarProduto(dadosProdutos):
    pass

#EXCLUIR UM PRODUTO
def excluirProduto(dadosProdutos):
    pass