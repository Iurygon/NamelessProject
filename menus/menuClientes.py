from classes.client import Client
import connection       as sql
import os

def menuClientes():
    os.system('cls')
    print("Bem-vindo ao menu de clientes!\n"
          "1 - Cadastrar novo cliente\n"
          "2 - Atualizar cadastro de cliente\n"
          "3 - Consultar cliente\n"
          "4 - Excluir cliente\n")
    opMenuCli = input("Digite qual opção deseja seguir: ")
    if opMenuCli not in ["1","2","3","4"]:
        print("O valor digitado deve estar entre as opções acima.")
        input("Pressione Enter tecla para continuar")
        menuClientes()
    match opMenuCli:
        case "1": cadastrarCliente()
        case "2": atualizarCadCliente()
        case "3": consultarCliente()
        case "4": excluirCLiente()

#CADASTRAR CLIENTE
def cadastrarCliente():
    print("Digite os dados do cliente a serem cadastrados:")
    # codigo  = PRECISA BUSCAR O ÚLTIMO CÓDIGO CADASTRADO NA BASE DE DADOS
    nome    = input("Nome: ")
    cidade  = input("Cidade: ")
    estado  = input("Estado: ")
    cnpj    = input("CNPJ: ")
    # cliente = Client("000001",nome, cidade, estado, cnpj)
    

#ALTERAR CADASTRO DE CLIENTE
def atualizarCadCliente():
    pass

#CONSULTAR CLIENTE
def consultarCliente():
    pass

#EXCLUIR CLIENTE
def excluirCLiente():
    pass