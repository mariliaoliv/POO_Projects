class Carro:

    def __init__(self):
        self.tanque = 0
        self.passageiros = 0
        self.quilometragem = 0

    def getPassageiros(self):
        return self.passageiros

    def getCombustivel(self):
        return self.tanque

    def getQuilometragem(self):
        return self.quilometragem

    def embarcar(self):
        if self.passageiros < 2:
            self.passageiros += 1
            print("uma pessoa embarcou no carro!")
            return True
        else:
            print("O carro está cheio!")
        return False

    def desembarcar(self):
        if self.passageiros > 0:
            self.passageiros -= 1
            print("Uma pessoa desembarcou!")
            return True
        else:
            print("O carro está vazio!")
            return False

    def dirigir(self, distancia):
        if distancia <= self.tanque:
            if self.passageiros > 0 and self.tanque > 0:
                distancia_maxima = self.tanque
                if distancia <= distancia_maxima:
                    self.tanque -= distancia
                    self.quilometragem += distancia
                    print(f"Dirigiu {distancia} quilômetros.")
                    return True
                if self.passageiros > 0 and self.tanque == 0:
                    print("Não há combustível suficiente!")
                    return False
        else:
            if self.passageiros > 0:
                self.quilometragem += self.tanque
                self.tanque = 0
                print(f"O carro ficou sem água após dirigir {self.quilometragem} quilômetros!")
                return False

    def abastecer(self, quantidade):
        if quantidade > 0:
            if self.tanque == 0:
                if self.tanque + quantidade <= 100:
                    self.tanque += quantidade
                    print(f"Abastecido com {quantidade} litros de água!")
                    return True
                else:
                    excesso = quantidade - (100 - self.tanque)
                    self.tanque = 100
                print("Abastecido com 100 litros água. {excesso} litros água foram descartados!")
                return True
            else:
                if self.tanque + quantidade >= 100:
                    self.tanque = 100
                    return True
                else:
                    self.tanque += quantidade
                    return True
        else:
            print("Não é possível fazer esse abastecimento, pois ele é negativo!")
        return False