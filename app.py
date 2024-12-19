from menus.menuProdutos import menuProdutos
from menus.menuClientes import menuClientes
from menus.menuNotas    import menuNotas
import os

def menuPrincipal():
    os.system("cls")
    print(  "Bem-vindo ao menu principal!\n"
            "1 - Cadastro de Clientes\n"
            "2 - Cadastro de Produto\n"
            "3 - Notas Fiscais\n"
            "4 - Sair do Sistema\n")
    acessoMenu = input("Qual função deseja acessar: ")
    if acessoMenu not in ("1","2","3","4"):
        print("O valor digitado deve estar entre as opções acima.")
        input("Pressione Enter para prosseguir.")
        menuPrincipal()
    match acessoMenu:
        case "1": menuClientes()
        case "2": menuProdutos()
        case "3": menuNotas()
        case "4": sairPrograma()

def sairPrograma():
    os.system("cls")
    print("Fechando o programa!")

menuPrincipal()