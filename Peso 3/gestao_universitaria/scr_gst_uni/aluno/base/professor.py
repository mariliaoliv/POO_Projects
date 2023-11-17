
from gestao_universitaria.scr_gst_uni.aluno.base.funcionario import Funcionario
from gestao_universitaria.scr_gst_uni.cliente.tipo import Tipo


class Professor(Funcionario):  # Supondo que você já tenha importado ou definido a classe Funcionario
    SALARIOS_POR_CLASSE = {'A': 3000, 'B': 5000, 'C': 7000, 'D': 9000, 'E': 11000}

    def __init__(self, cpf: str, nome: str, classe: str):
        super().__init__(cpf, nome)
        self.classe = classe
        self.tipo = Tipo.PROF
        self.salario = self.SALARIOS_POR_CLASSE.get(classe, 0)