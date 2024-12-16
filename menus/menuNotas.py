import os

def menuNotas():
    os.system("cls")
    print("Menu de notas!\n Selecione qual opção deseja seguir:\n"
          "1 - Lançar notas\n"
          "2 - Pagar notas em aberto\n"
          "2 - Consultar notas\n"
          "3 - Excluir nota\n")
    opMenuNotas = input("Selecione qual opção deseja seguir: ")
    if opMenuNotas not in ("1","2","3","4"):
        print("O valor digitado deve estar entre as opções acima.")
        input("Pressione Enter para prosseguir.")
        menuNotas()


#LANÇAR NOTAS

#PAGAR NOTAS EM ABERTO


#CONSULTAR NOTAS


#EXCLUIR NOTAS