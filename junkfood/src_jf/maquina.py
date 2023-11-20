from junkfood.src_jf.espiral import Espiral


class Maquina:
    def __init__(self, qtdEspirais: int, maximoProdutos: int):
        self.espirais = [Espiral() for _ in range(qtdEspirais)]
        self.qtdESpirais = qtdEspirais
        self.maximoProdutos = maximoProdutos
        self.faturamento_total = 0
        self.saldo = 0

    def getFaturamento(self) -> float:
        return self.faturamento_total

    def getMaximoProdutos(self) -> int:
        return self.maximoProdutos

    def getSaldoCliente(self) -> float:
        return self.saldo

    def getSizeEspirais(self) -> int:
        return len(self.espirais)

    def getEspiral(self, indice: int) -> Espiral:
        return self.espirais[indice] if 0 <= indice < self.getSizeEspirais() else None

    def inserirDinheiro(self, value: float) -> bool:
        if value > 0:
            self.saldo += value
            return True
        return False

    def receberTroco(self) -> float:
        troco = self.saldo - self.faturamento_total
        self.saldo = 0
        return troco

    def alterarEspiral(self, indice: int, nome: str, quantidade: int, preco: float) -> bool:
        if 0 <= indice < self.getSizeEspirais() and quantidade <= self.maximoProdutos:
            espiral = self.espirais[indice]
            espiral.setNomeDoProduto(nome)
            espiral.setQuantidade(quantidade)
            espiral.setPreco(preco)
            return True
        return False

    def limparEspiral(self, indice: int) -> bool:
        if 0 <= indice < self.getSizeEspirais():
            self.espirais[indice].resetar()
            return True
        return False

    def vender(self, indice: int) -> bool:
        if 0 <= indice < self.getSizeEspirais():
            espiral = self.espirais[indice]
            if self.saldo >= espiral.getPreco() and espiral.getQuantidade() > 0:
                espiral.quantidade -= 1
                self.faturamento_total += espiral.getPreco()
                if espiral.getQuantidade() == 0:
                    self.limparEspiral(indice)
                return True
        return False