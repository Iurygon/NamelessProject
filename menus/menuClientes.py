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
        input("Pressione Enter para continuar")
        menuClientes()
    match opMenuCli:
        case "1": cadastrarCliente()
        case "2": atualizarCadCliente()
        case "3": consultarCliente()
        case "4": excluirCLiente()

#CADASTRAR CLIENTE
def cadastrarCliente():
    os.system("cls")
    print("Digite os dados do cliente a serem cadastrados:")
    consultaCodigo = sql.cursor.execute("SELECT MAX(CLIENTES.CODIGO) FROM CLIENTES (NOLOCK)").fetchone()
    if consultaCodigo[0] is None:
        codigo = 1
    else:
        codigo = consultaCodigo[0] + 1
    nome    = input("Nome: ")
    cidade  = input("Cidade: ")
    estado  = input("Estado: ")
    cnpj    = input("CNPJ: ")
    cliente = Client(codigo, nome, cidade, estado, cnpj)
    try:
        sql.cursor.execute(f"INSERT INTO CLIENTES VALUES ({codigo},'{nome}','{cidade}','{estado}','{cnpj}')")
        sql.connection.commit()
        print("Cliente cadastrado com sucesso!")
    except:
        sql.connection.rollback()
        print("Falha na gravação dos dados! Revise os valores digitados e, caso o erro persista, entre em contato com o administrador ")
    menuClientes()

#ALTERAR CADASTRO DE CLIENTE
def atualizarCadCliente():
    # CARREGAR OS CLIENTES CADASTRADOS NA BASE DE DADOS
    # CRIAR UMA INSTANCIA PARA CADA CLIENTE E APRESENTAR OS DADOS
    pass

#CONSULTAR CLIENTE
def consultarCliente():

    pass

#EXCLUIR CLIENTE
def excluirCLiente():
    pass