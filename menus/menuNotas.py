import connection as sql
import os
from classes.invoice import Invoice
from classes.client import Client
from classes.product import Product

def menuNotas():
    os.system("cls")
    dadosProdutos = sql.cursor.execute("SELECT * FROM PRODUTOS (NOLOCK)").fetchall()
    dadosClientes = sql.cursor.execute("SELECT * FROM CLIENTES (NOLOCK)").fetchall()
    dadosNotas = sql.cursor.execute("SELECT * FROM NOTASFISCAIS (NOLOCK)").fetchall()
    print("Menu de notas!\n Selecione qual opção deseja seguir:\n"
          "1 - Lançar notas\n"
          "2 - Pagar notas em aberto\n"
          "3 - Consultar notas\n"
          "4 - Excluir nota\n")
    opMenuNotas = input("Selecione qual opção deseja seguir: ")
    if opMenuNotas not in ("1","2","3","4"):
        print("O valor digitado deve estar entre as opções acima.")
        input("Pressione Enter para prosseguir.")
        menuNotas()
    else:
        match  opMenuNotas:
            case "1": lancarNotas(dadosClientes, dadosProdutos, dadosNotas)
            case "2": pagarNotas(dadosClientes, dadosProdutos, dadosNotas)
            case "3": consultarNotas(dadosClientes, dadosProdutos, dadosNotas)
            case "4": excluirNotas(dadosClientes, dadosProdutos, dadosNotas)

#LANÇAR NOTAS
def lancarNotas(dadosClientes, dadosProdutos, dadosNotas):
    os.system("cls")
    print("Digite os dados para preencher a nota:")
    #PREENCHER DADOS DO CLIENTE
    for clienteInfo in dadosClientes:
        objCliente = Client(clienteInfo[0],clienteInfo[1],clienteInfo[2],clienteInfo[3],clienteInfo[4])
        print(objCliente.informacoes)
    cliente = input("Digite o código do cliente:\n")
    #PREENCHER DADOS DOS PRODUTOS
    dictInfoProdutos = {}
    insereProduto = 0
    os.system("cls")
    print("Digite os dados para preencher a nota:")
    for produtoInfo in dadosProdutos:
        objProduto = Product(produtoInfo[0],produtoInfo[1],produtoInfo[2])
        print(objProduto.informacoes)
    while insereProduto != "1":
        codProduto = int(input("Digite o código do produto:\n"))
        quantProduto = int(input("Digite a quantidade do produto:\n"))
        dictInfoProdutos.update({codProduto: quantProduto})
        insereProduto = input("Deseja inserir um novo produto? 0 para Sim; 1 para Não\n")
    #ENVIAR DADOS DA NOTA
    '''CÓDIGO PARA FAZER O ENVIO DOS DADOS DA NOTA'''
    print(dictInfoProdutos)
    print(len(dictInfoProdutos))
    input("Pressione Enter para continuar")
    menuNotas()

#PAGAR NOTAS EM ABERTO
def pagarNotas(dadosClientes, dadosProdutos, dadosNotas):
    pass

#CONSULTAR NOTAS
def consultarNotas(dadosClientes, dadosProdutos, dadosNotas):
    pass

#EXCLUIR NOTAS
def excluirNotas(dadosClientes, dadosProdutos, dadosNotas):
    pass