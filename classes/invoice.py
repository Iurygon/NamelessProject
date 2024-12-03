class Invoice():
    def __init__(self, numeroNota, dataEmissao, quantidadeItens, itensProdutos):
        self.numeroNota = numeroNota
        self.dataEmissao = dataEmissao
        self.quantidadeItens = quantidadeItens
        self.itensProdutos = itensProdutos
        self.debtoPago = False

    def payDebt(self):
        self.debtoPago = True

    @property
    def informacoes(self):
        print(f"Nota {self.numeroNota}, Emitida em {self.dataEmissao}")