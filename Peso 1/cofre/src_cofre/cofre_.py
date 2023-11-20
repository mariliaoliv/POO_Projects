from cofre.src_cofre.item import Item
from cofre.src_cofre.moeda import Moeda


class Cofre:
    def __init__(self, volumeMaximo: int):
        self.__volumeMaximo = volumeMaximo
        self.volume = 0
        self.taInt = True
        self.itens = []
        self.moedas = []

    def getVolume(self):
        return self.volume

    def getVolumeMaximo(self):
        return self.__volumeMaximo

    def getVolumeRestante(self):
        return self.__volumeMaximo - self.volume

    def _adicionar(self, volume):
        if self.taInt:
            if volume <= self.getVolumeRestante():
                self.volume += volume
                return True
            else:
                print('Volume está maior que o volume restante!')
        else:
            print('O cofre não está inteiro!')
        return False

    def add(self, item: Item):
        if self.taInt and item.getVolume() <= self.getVolumeRestante():
            self.volume += item.getVolume()
            self.itens.append(item)
            return True
        elif not self.taInt:
            print('O cofre não está inteiro!')
        else:
            print('O volume do item está maior que o volume restante!')
        return False

    def addMoeda(self, moeda: Moeda):
        if self.taInt and moeda.getVolume() <= self.getVolumeRestante():
            self.volume += moeda.getVolume()
            self.moedas.append(moeda.getValor())
            return True
        else:
            print('O volume da moeda está maior que o volume restante!' if self.taInt else 'O cofre não está inteiro!')
            return False

    def obterItens(self):
        if not self.taInt:
            return ', '.join([item.getDescrição() for item in self.itens]) or 'vazio'

    def obterMoedas(self):
        if not self.taInt:
            return sum(self.moedas) if self.moedas else 0
        return -1

    def taInteiro(self):
        return self.taInt

    def quebrar(self):
        if self.taInt:
            self.taInt = False
            return True
        return False