class Tamagotchi:

    def __init__(self, energiaMax:int, saciedadeMax:int, limpezaMax:int, idadeMax:int ):
        self.energiaMax = energiaMax
        self.saciedadeMax = saciedadeMax
        self.limpezaMax = limpezaMax
        self.idadeMax = idadeMax
        self.diamantes = 0
        self.idade = 0
        self.energia = energiaMax
        self.saciedade = saciedadeMax
        self.limpeza = limpezaMax

    def getEnergiaMax(self):
        return self.energiaMax

    def getSaciedadeMax(self):
        return self.saciedadeMax

    def getLimpezaMax(self):
        return self.limpezaMax

    def getIdadeMax(self):
        return self.idadeMax

    def getEnergiaAtual(self):
        return self.energia

    def getSaciedadeAtual(self):
        return self.saciedade

    def getLimpezaAtual(self):
        return self.limpeza

    def getIdadeAtual(self):
        return self.idade

    def getDiamantes(self):
        return self.diamantes

    def getEstaVivo(self):
        if self.energia <= 0:
            print("Seu Tamagotchi morreu!:(")
            self.energia = 0
            return False

        elif self.saciedade <= 0:
            print("Seu Tamagotchi morreu! :(")
            self.saciedade = 0
            return False

        elif self.limpeza <= 0:
            print("Seu Tamagotchi morreu! :(")
            self.limpeza = 0
            return False

        elif self.idade > self.idadeMax:
            print("Seu Tamagotchi morreu! :(")
            self.idade = self.idadeMax
            return False

        else:
            print(f"Energia: {self.energiaMax}, Saciedade: {self.saciedadeMax},"
                  f" Limpeza: {self.limpezaMax}")
            return True

    def brincar(self):
        if self.getEstaVivo():
            self.energia -= 2
            self.saciedade -= 1
            self.limpeza -= 3
            self.diamantes += 1
            self.idade += 1
            return True
        else:
            print("Não é possível realizar esta ação!")
            return False

    def comer(self):
        if self.getEstaVivo():
            self.energia -= 1
            if self.saciedadeMax > self.saciedade + 4:
                self.saciedade += 4
            else:
                self.saciedade = self.saciedadeMax

            self.limpeza -= 2
            self.diamantes = self.diamantes
            self.idade += 1
            return True
        else:
            print("Não é possível dar comida ao seu Tamagotchi!")
            return False

    def dormir(self):
        if self.getEstaVivo():
            if self.energiaMax - self.energia >= 5:
                turnos = self.energiaMax - self.energia
                self.saciedade -= 2
                self.idade += turnos
                self.energia = self.energiaMax
                return True
            else:
                print("Seu Tamagocthi não está cansado o suficiente!")
                return False
        else:
            print("Seu Tamagotchi não está cansado o suficiente para dormir!")
            return False

    def banhar(self):
        if self.getEstaVivo():
            self.energia -= 3
            self.saciedade -= 1
            self.limpeza = self.limpezaMax
            self.diamantes = self.diamantes
            self.idade += 2
            return True
        else:
            print("Não é possível banhar seu Tamagochi!")
            return False




