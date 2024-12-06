class Invoice():
    def __init__(self, numeroNota, dataEmissao, quantidadeItens, itensProdutos,clienteNota):
        self.numeroNota = numeroNota
        self.dataEmissao = dataEmissao
        self.quantidadeItens = quantidadeItens
        self.itensProdutos = itensProdutos
        self.debtoPago = False
        self.clienteNota = clienteNota

    def payDebt(self):
        self.debtoPago = True

    @property
    def informacoes(self):
        print(f"Nota {self.numeroNota}, Emitida em {self.dataEmissao}")