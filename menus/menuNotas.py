import connection as sql
import os
from classes.invoice import Invoice

def menuNotas():
    os.system("cls")
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
            case "1": lancarNotas()
            case "2": pagarNotas()
            case "3": consultarNotas()
            case "4": excluirNotas()

#LANÇAR NOTAS
def lancarNotas():
    pass

#PAGAR NOTAS EM ABERTO
def pagarNotas():
    pass

#CONSULTAR NOTAS
def consultarNotas():
    pass

#EXCLUIR NOTAS
def excluirNotas():
    pass