def menuProdutos():
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
        case "1": cadastrarProduto()
        case "2": atualizarCadProduto()
        case "3": consultarProduto()
        case "4": excluirProduto()

#CADASTRAR PRODUTO
def cadastrarProduto():
    pass

#ATUALIZAR CADASTRO DE UM PRODUTO
def atualizarCadProduto():
    pass

#CONSULTAR UM PRODUTO
def consultarProduto():
    pass

#EXCLUIR UM PRODUTO
def excluirProduto():
    pass