from classes.client import Client
# from app import menuPrincipal
import connection       as sql
import os
import time

def menuClientes():
    dadosClientes = sql.cursor.execute("SELECT MAX(CLIENTES.CODIGO) OVER (), * FROM CLIENTES (NOLOCK)").fetchall()
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
        case "1": cadastrarCliente(dadosClientes)
        case "2": atualizarCadCliente(dadosClientes)
        case "3": consultarCliente(dadosClientes)
        case "4": excluirCLiente(dadosClientes)
        # case "5": menuPrincipal()

#CADASTRAR CLIENTE
def cadastrarCliente(dadosClientes):
    os.system("cls")
    print("Digite os dados do cliente a serem cadastrados:")
    if len(dadosClientes) == 0:
        codigo = 1
    else:
        codigo = dadosClientes[0][0] + 1
    nome    = input("Nome: ")
    cidade  = input("Cidade: ")
    estado  = input("Estado: ")
    cnpj    = input("CNPJ: ")
    cliente = Client(codigo, nome, cidade, estado, cnpj)
    try:
        sql.cursor.execute(f"INSERT INTO CLIENTES VALUES ({codigo},'{nome}','{cidade}','{estado}','{cnpj}')")
        sql.connection.commit()
        print(cliente.informacoes)
        print("Cliente cadastrado com sucesso!")
        time.sleep(5)
    except:
        sql.connection.rollback()
        print("Falha na gravação dos dados! Revise os valores digitados e, caso o erro persista, entre em contato com o administrador ")
        time.sleep(5)
    menuClientes()

#ALTERAR CADASTRO DE CLIENTE
def atualizarCadCliente(dadosClientes):
    # CARREGAR OS CLIENTES CADASTRADOS NA BASE DE DADOS
    # CRIAR UMA INSTANCIA PARA CADA CLIENTE E APRESENTAR OS DADOS
    pass

#CONSULTAR CLIENTE
def consultarCliente(dadosClientes):
    os.system("cls")
    print(f"Existem {0 if len(dadosClientes) == 0 else dadosClientes[0][0]} cliente(s) cadastrados no sistema.")
    visualizaTodos = input("Deseja visualizar todos? [1] Sim [2] Pesquisar por código\n")
    if visualizaTodos not in ["1","2"]:
        print("O valor digitado deve estar entre uma das opções informadas solicitadas!")
        time.sleep(3)
        menuClientes()
    else:
        if visualizaTodos == "1":
            for clienteInfo in dadosClientes:
                objCliente = Client(clienteInfo[1], clienteInfo[2], clienteInfo[3], clienteInfo[4], clienteInfo[5])
                print(objCliente.informacoes)
        else:
            codigoPesquisado = input("Qual código deseja pesquisar? ")
            clienteInfo = sql.cursor.execute(f"SELECT * FROM CLIENTES (NOLOCK) WHERE CODIGO = {codigoPesquisado}").fetchone()
            objCliente = Client(clienteInfo[0], clienteInfo[1], clienteInfo[2], clienteInfo[3], clienteInfo[4])
            print(objCliente.informacoes)
    input("Pressione Enter para seguir.")
    menuClientes()

#EXCLUIR CLIENTE
def excluirCLiente(dadosClientes):
    pass