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
    #BUSCAR NUMERO DA NOTA
    numNotaFiscal = sql.cursor.execute("SELECT MAX(NUMERO) FROM NOTASFISCAIS (NOLOCK)").fetchone()
    if numNotaFiscal[0] == None:
        numNotaFiscal[0] = 0
    numNotaFiscal = int(numNotaFiscal[0]) + 1
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
        valorProduto = sql.cursor.execute(f"SELECT PRECO FROM PRODUTOS (NOLOCK) WHERE CODIGO = {codProduto}").fetchone()
        dictInfoProdutos.update({codProduto: [quantProduto,valorProduto[0]]})
        insereProduto = input("Deseja inserir um novo produto? 0 para Sim; 1 para Não\n")     
    #ENVIAR DADOS DA NOTA
    try:
        for produto in dictInfoProdutos:
            print(f"Cliente: {cliente}, Produto: {produto}, Quantidade: {dictInfoProdutos[produto][0]}, Valor: {dictInfoProdutos[produto][0] * dictInfoProdutos[produto][1]}")
            sql.cursor.execute(f"INSERT INTO NOTASFISCAIS VALUES ('{str(numNotaFiscal).zfill(9)}', GETDATE(),{produto},{dictInfoProdutos[produto][0]},{cliente},{dictInfoProdutos[produto][0] * dictInfoProdutos[produto][1]},0)")
            sql.connection.commit()
    except:
        sql.connection.rollback()
        print("Falha na gravação dos dados! Revise os valores e, caso o erro persistir, entre em contato com o administrador.")
    input("Pressione Enter para continuar")
    menuNotas()

#PAGAR NOTAS EM ABERTO
def pagarNotas(dadosClientes, dadosProdutos, dadosNotas):
    #ALTERAR O ESTADO DA NOTA DE EM ABERTO PARA FECHADO#
    #CRIAR UMA FORMA DE VERIFICAR AS NOTAS EM ABERTO PENDENTES PARA AQUELE CLIENTE, VENDO UM SOMATÓRIO TOTAL E POSSIBILITANDO QUITAR MAIS DE UMA NOTA#
    pass

#CONSULTAR NOTAS
def consultarNotas(dadosClientes, dadosProdutos, dadosNotas):
    #CRIAR UM OBJETO INVOICE E REALIAR A CONSULTA SOBRE ELE#
    pass

#EXCLUIR NOTAS
def excluirNotas(dadosClientes, dadosProdutos, dadosNotas):
    numeroNota = input("Digite o número da nota a ser excluída:\n")
    consultaNota = sql.cursor.execute(f"SELECT * FROM NOTASFISCAIS (NOLOCK) WHERE NUMERO = {numeroNota}").fetchall()
    print(consultaNota)
    #DELETAR UMA NOTA DA BASE DE DADOS#