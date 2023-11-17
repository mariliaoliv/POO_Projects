from topic_de_luxo.src_topic.passageiro import Passageiro

class Topic:
    def __init__(self, capacidade: int, qtdPrioritarios):
        self.capacidade = capacidade
        self.qtdprioritarios = qtdPrioritarios
        self.ass_normais = self.capacidade - self.qtdprioritarios
        self.psg_n = []
        self.psg_p = []
        self.vagas = capacidade
        self.lista_str = []

    def getNumeroAssentosPrioritarios(self):
        return self.qtdprioritarios

    def getNumeroAssentosNormais(self):
        return self.ass_normais

    def getPassageiroAssentoNormal(self, lugar):
        if lugar >= 0 and lugar < len(self.psg_n):
            return self.psg_n[lugar]
        else:
            return None

    def getPassageiroAssentoPrioritario(self, lugar):
        if lugar >= 0 and lugar < len(self.psg_p):
            return self.psg_p[lugar]
        else:
            return None

    def getVagas(self):
        return self.vagas

    def subir(self, passageiro: Passageiro):
        vagas_disp = self.capacidade - (len(self.psg_n) + len(self.psg_p))
        if vagas_disp > 0:
            if passageiro.ePrioridade():
                if len(self.psg_p) < self.qtdprioritarios:
                    self.vagas -= 1
                    self.psg_p.append(passageiro)
                    return True
                else:
                    self.psg_n.append(passageiro)
                    self.vagas -= 1
                    return True
            elif not passageiro.ePrioridade():
                if len(self.psg_n) < self.ass_normais:
                    self.vagas -= 1
                    self.psg_n.append(passageiro)
                    return True
                else:
                    self.psg_p.append(passageiro)
                    self.vagas -= 1
                    return True
        return False

    def descer(self, nome):
        for passageiro in self.psg_n:
            if passageiro.getNome() == nome:
                self.vagas += 1
                self.psg_n.remove(passageiro)
                return True
        for passageiro in self.psg_p:
            if passageiro.getNome() == nome:
                self.vagas += 1
                self.psg_p.remove(passageiro)
                return True
        return False

    def toString(self):
        for passageiro in self.psg_p:
            if passageiro.ePrioridade():
                self.lista_str.insert(0, '@' + passageiro.nome)
                return True
            else:
                self.lista_str.append('@')
                return True

        for passageiro in self.psg_n:
            if not passageiro.ePrioridade():
                self.lista_str.insert(0, '=' + passageiro.nome)
                return True
            else:
                self.lista_str.append('=')
                return True

        lista = ' '.join(self.lista_str)
        return '[' + lista + ' ]'
