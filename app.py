import connection       as sql
import classes.client   as cli
import classes.product  as prd
import classes.invoice  as nf
import os

def menuPrincipal():
    os.system("cls")
    print("Bem vindo ao menu principal! Qual função deseja acessar:")
    acessoMenu = input( "1 - Cadastro de Clientes\n"
                        "2 - Cadastro de Produto\n"
                        "3 - Notas Fiscais\n"
                        "4 - Sair do Sistema")
    return acessoMenu

def menuClientes(opcaoAcesso):
    pass

def menuProdutos(opcaoAcesso):
    pass

def notasFiscais(opcaoAcesso):
    pass

def sairPrograma(opcaoAcesso):
    pass


menuPrincipal()