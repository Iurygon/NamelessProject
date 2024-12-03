class Product():
    def __init__(self, codProduto, nomeProduto, precoProduto):
        self.codProduto = codProduto
        self.nomeProduto = nomeProduto
        self.precoProduto = precoProduto
    
    @property
    def informacoes(self):
        print(f"Produto: {self.codProduto} - {self.nomeProduto.ljust(25)}, Valor: R${self.precoProduto}")