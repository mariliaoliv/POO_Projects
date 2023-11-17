from pula_pula.src_pulapula.crianca import Crianca
class PulaPula:

    def __init__(self, limiteMax):
        self.limiteMax = limiteMax
        self.fila_de_espera = []
        self.crianca_pulando = []
        self.caixa = 0
        self.conta = 0
    def getFilaDeEspera(self):
        return self.fila_de_espera

    def getCriancasPulando(self):
        return self.crianca_pulando

    def getLimiteMax(self):
        return self.limiteMax

    def getCaixa(self):
        return self.caixa

    def getConta(self, nome):
        for c in self.crianca_pulando:
            if c.nome == nome:
                return self.conta

    def entrarNaFila(self, crianca: Crianca):
        if crianca.getNome() not in [c.getNome() for c in self.fila_de_espera]:
            self.fila_de_espera.append(crianca)
            return True
        else:
            return False

    def entrar(self):
        if len(self.crianca_pulando) < self.limiteMax:
            if len(self.fila_de_espera) > 0:
                self.crianca_pulando.append(self.fila_de_espera[0])
                self.fila_de_espera.pop(0)
                self.conta += 2.50
                return True
            return False
        return False

    def sair(self):
        if len(self.crianca_pulando) > 0:
            self.fila_de_espera.append(self.crianca_pulando[-1])
            self.crianca_pulando.pop()
            return True
        else:
            return False

    def papaiChegou(self, nome):
        for c_pulando in self.fila_de_espera:
            if c_pulando.getNome() == nome:
                self.fila_de_espera.remove(c_pulando)
                self.caixa += self.conta
                self.conta = 0
                return True
        for c_pulando in self.crianca_pulando:
            if c_pulando.getNome() == nome:
                self.crianca_pulando.remove(c_pulando)
                self.caixa += self.conta
                self.conta = 0
                return True

    def fechar(self):
        if len(self.fila_de_espera) > 0 and len(self.crianca_pulando) > 0:
            self.fila_de_espera.clear()
            self.crianca_pulando.clear()
            self.conta = None
            return True


