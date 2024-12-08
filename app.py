import connection       as sql
import classes.client   as cli
import classes.product  as prd
import classes.invoice  as nf
from menus.menuProdutos import menuProdutos
from menus.menuClientes import menuClientes
from menus.menuNotas    import menuNotas
import os

def menuPrincipal():
    os.system("cls")
    print("Bem vindo ao menu principal! Qual função deseja acessar:")
    acessoMenu = input( "1 - Cadastro de Clientes\n"
                        "2 - Cadastro de Produto\n"
                        "3 - Notas Fiscais\n"
                        "4 - Sair do Sistema")
    match acessoMenu:
        case "1": menuClientes()
        case "2": menuProdutos()
        case "3": menuNotas()
        case "4": sairPrograma()

def sairPrograma():
    os.system("cls")
    print("Fechando o programa!")

menuPrincipal()