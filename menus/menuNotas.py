import connection as sql
import os
from classes.invoice import Invoice
from classes.client import Client
from classes.product import Product

def menuNotas():
    os.system("cls")
    dadosProdutos = sql.cursor.execute("SELECT * FROM PRODUTOS (NOLOCK)").fetchall()
    dadosClientes = sql.cursor.execute("SELECT * FROM CLIENTES (NOLOCK)").fetchall()
    dadosNotas = sql.cursor.execute("SELECT * FROM CONSDADOSNOTAS (NOLOCK)").fetchall()
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
def lancarNotas(dadosClientes, dadosProdutos):
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
    dadosNotas = query("situacao","0")
    valorConsulta = input("Informe o número da nota a ser paga:\n")
    listaNotas = []
    for nota in dadosNotas:
        listaNotas.append(nota[0])
    if valorConsulta not in listaNotas:
        print("O valor digitado não existe na base de dados! Favor, tente novamente.")
    else:
        try:
            sql.cursor.execute(f"UPDATE NOTASFISCAIS SET DEBTOPAGO = 1 WHERE NUMERO = '{valorConsulta}'")
            sql.connection.commit()
            print("Nota declarada como paga!")
        except:
            sql.connection.rollback()
            print("Não foi possível executar o processo. Tente novamente e, caso o erro persistir, entre em contato com o administrador!")
    input("Pressione Enter para continuar.")
    menuNotas()

#CONSULTAR NOTAS
def consultarNotas():
    tipoConsulta = input("Deseja realizar a busca de que forma?\n1-Numero da nota\n2-Cliente\n3-Notas abertas")
    if tipoConsulta not in ["1","2","3"]:
        print("A opção digitada não é válida! Favor, tentar novamente.")
        menuNotas
    else:
        match tipoConsulta:
            case "1": valorConsulta = input("Digite o número da nota\n")
            case "2": valorConsulta = input("Digite o código do cliente\n")
        match tipoConsulta:
            case "1": query("notas",valorConsulta)
            case "2": query("cliente",valorConsulta)
            case "3": query("situacao","0")
    input("Pressione Enter para continuar")
    menuNotas()

#EXCLUIR NOTAS
def excluirNotas(dadosNotas):
    numeroNota = input("Digite o número da nota a ser excluída:\n")
    query("notas",numeroNota)
    listaNumNota = []
    for nota in dadosNotas:
        listaNumNota.append(nota[0])
    if numeroNota not in listaNumNota:
        print("O número da nota digitada não existe no banco de dados. Favor, tente novamente.")
    else:
        try:
            sql.cursor.execute(f"DELETE FROM NOTASFISCAIS WHERE NUMERO = '{numeroNota}'")
            sql.connection.commit()
            print('Nota excluída com sucesso!')
        except:
            print("Falha na exclusão da nota. Se o erro persistir, entre em contato com o administrador!")
    input("Pressione Enter para continuar")
    menuNotas()

#REALIZA A CONSULTA NA BASE DE DADOS
def query(colunaFiltro, valorBuscado):
    queryGeral = "SELECT * FROM CONSDADOSNOTAS (NOLOCK) "
    queryComplemento = ""
    match colunaFiltro:
        case "cliente": queryComplemento = f"WHERE CODCLIENTE = {valorBuscado}"
        case "produto": queryComplemento = f"WHERE CODPRODUTO = {valorBuscado}"
        case "notas": queryComplemento = f"WHERE NUMERO = '{valorBuscado}'"
        case "situacao": queryComplemento = f"WHERE DEBTOPAGO = '{valorBuscado}'"
    if colunaFiltro != "geral":
        queryGeral = queryGeral + queryComplemento
    resultado = sql.cursor.execute(queryGeral).fetchall()
    for nota in resultado:
        print(f"Nota: {nota[0]}| Emissão: {nota[1]}|CodCliente: {str(nota[2]).ljust(3)}| NomeCliente: {nota[3].ljust(20)}| CodProduto: {str(nota[4]).ljust(3)}| Produto: {nota[5].ljust(20)}| Quant: {nota[6]}| VlrUnitario: R${round(nota[7],2)}| VlrTotal: R${round(nota[8],2)}| Situação: {nota[9]}")