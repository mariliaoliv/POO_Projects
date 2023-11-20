class Espiral:
    def __init__(self):
        self.nome_produto = ' - '
        self.quantidade = 0
        self.preco = 0

    def resetar(self):
        self.nome_produto = ' - '
        self.quantidade = 0
        self.preco = 0

    def getNomeDoProduto(self):
        return self.nome_produto

    def setNomeDoProduto(self, nome: str):
        self.nome_produto = nome

    def getQuantidade(self):
        return self.quantidade

    def setQuantidade(self, qtd: int):
        self.quantidade = qtd

    def getPreco(self):
        return self.preco

    def setPreco(self, preco: float):
        self.preco = preco
