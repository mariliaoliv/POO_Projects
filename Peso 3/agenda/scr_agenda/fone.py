from agenda.scr_agenda.identificador import Identificador


class Fone:

    def __init__(self, identificador: Identificador, numero: str):
        self.indentificador = identificador
        self.numero = numero

    @staticmethod
    def validarNumero(numero) -> bool:
        caracteres = "0123456789()-"
        for c in numero:
            if c not in caracteres:
                return False
        return True

    def getIdentificador(self) -> Identificador:
        return self.indentificador

    def getNumero(self) -> str:
        return self.numero
