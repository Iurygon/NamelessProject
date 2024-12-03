class Client():
    def __init__(self, codCliente, nomeCliente, cidadeCliente, estadoCliente, cnpjCliente):
        self.codCliente = codCliente
        self.nomeCliente = nomeCliente
        self.cidadeCliente = cidadeCliente
        self.estadoCliente = estadoCliente
        self.cnpjCliente = cnpjCliente

    @property
    def informacoes(self):
        print(f'Cliente: {self.codCliente} - {self.nomeCliente.ljust(25)}, Cidade/Estado: {self.cidadeCliente.ljust(20)}/{self.estadoCliente}')