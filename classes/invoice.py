class Invoice():
    def __init__(self, numeroNota, dataEmissao, quantidadeItens, itensProdutos,valorItens,clienteNota):
        self.numeroNota = numeroNota
        self.dataEmissao = dataEmissao
        self.quantidadeItens = quantidadeItens
        self.itensProdutos = itensProdutos
        self.valorItens = valorItens
        self.debtoPago = False
        self.clienteNota = clienteNota

    def payDebt(self):
        self.debtoPago = True

    @property
    def informacoes(self):
        print(f"Nota {self.numeroNota}, Emitida em {self.dataEmissao}")