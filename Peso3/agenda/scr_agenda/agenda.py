
from agenda.scr_agenda.contato import Contato
from agenda.scr_agenda.identificador import Identificador

class Agenda:

    def __init__(self):
        self.contatos = []

    def getContatos(self) -> list:
        nomes = sorted([contato.getName() for contato in self.contatos])
        ctt_em_ordem = []
        for nome in nomes:
            for ctt in self.contatos:
                if nome == ctt.nome:
                    ctt_em_ordem.append(ctt)
        return ctt_em_ordem

    def getQuantidadeDeContatos(self) -> int:
        return len(self.contatos)

    def getContato(self, nome:str) -> Contato:
        for ctt in self.contatos:
            if ctt.nome == nome:
                return ctt
        return None

    def adicionarContato(self, contato: Contato) -> bool:
        nome_ex = False
        if self.getQuantidadeDeContatos() > 0:
           for existente in self.contatos:
              if existente.nome == contato.nome:
                  for fone in contato.getFones():
                      existente.adicionarFone(fone)
                  nome_ex = True
           if nome_ex:
               return False
           else:
               self.contatos.append(contato)
               return True
        else:
            self.contatos.append(contato)
            return True

    def removerContato(self, nome: str) -> bool:
        for contato in self.contatos:
            if contato.nome == nome:
                self.contatos.remove(contato)
                return True
        return False

    def removerFone(self, nome:str, index: int) -> bool:
        for contato in self.contatos:
            if contato.nome == nome:
                if 0 <= index < len(contato.fones):
                    contato.fones.pop(index)
                    return True
        return False

    def getQuantidadeDeFonesIdentificador(self, identificador: Identificador) -> int:
      quantidade = 0
      for contato in self.contatos:
          for fone in contato.getFones():
              if fone.getIdentificador() == identificador:
                  quantidade += 1
      return quantidade

    def getQuantidadeDeFones(self) -> int:
        quantidade = 0
        for contato in self.contatos:
            quantidade += contato.getQuantidadeFones()
        return quantidade

    def pesquisar(self, expressao:str) -> list:
        resultados = [contato for contato in self.contatos if expressao.lower() in contato.nome.lower()]
        for contato in self.contatos:
            for fone in contato.getFones():
                if expressao.lower() in fone.numero.lower():
                    resultados.append(contato)
                    break
        return sorted(resultados, key=lambda x: x.nome)


