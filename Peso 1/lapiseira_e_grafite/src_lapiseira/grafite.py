from lapiseira_e_grafite.src_lapiseira.dureza import Dureza


class Grafite:

    def __init__(self, calibre: float, dureza: Dureza, tamanho: int):
        self.calibre = calibre
        self.dureza = dureza
        self.tamanho = tamanho
        self.desgaste = self._calcularDesgaste()

    def _calcularDesgaste(self):
        if self.dureza.value == 1 or self.dureza.value == 2:
            return self.dureza.value
        elif self.dureza.value == 3:
            return 4
        else:
            return 6

    def desgastePorFolha(self):
        return self.desgaste

    def getDureza(self):
        return self.dureza

    def getCalibre(self):
        return self.calibre

    def getTamanho(self):
        return self.tamanho

    def setTamanho(self, tamanho: int):
        self.tamanho = tamanho




