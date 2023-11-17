from gestao_universitaria.scr_gst_uni.cliente.irh_service import IRHService
from gestao_universitaria.scr_gst_uni.aluno.base.funcionario import Funcionario
from gestao_universitaria.scr_gst_uni.cliente.tipo import Tipo


from collections import defaultdict


class RHService(IRHService):
    def __init__(self):
        self.funcionarios = []
        self.diarias = defaultdict(int)
        self.partilha = 0

    def cadastrar(self, funcionario: Funcionario):
        tipos_validos = {
            Tipo.PROF: ['A', 'B', 'C', 'D', 'E'],
            Tipo.STA: list(range(1, 31))
        }

        if funcionario.getTipo() in tipos_validos:
            if funcionario.getTipo() == Tipo.PROF and funcionario.getClasse() not in tipos_validos[Tipo.PROF]:
                return False
            if funcionario.getTipo() == Tipo.STA and funcionario.getNivel() not in tipos_validos[Tipo.STA]:
                return False

        if funcionario.getCpf() in (f.getCpf() for f in self.funcionarios):
            return False

        self.funcionarios.append(funcionario)
        return True

    def remover(self, cpf: str):
        for funcionario in self.funcionarios:
            if funcionario.getCpf() == cpf:
                self.funcionarios.remove(funcionario)
                return True
        return False

    def obterFuncionario(self, cpf: str):
        return next((f for f in self.funcionarios if f.getCpf() == cpf), None)

    def getFuncionarios(self):
        return sorted(self.funcionarios, key=lambda f: f.getNome())

    def getFuncionariosPorCategorias(self, tipo):
        funcionarios_categoria = [funcionario for funcionario in self.funcionarios if funcionario.getTipo() == tipo]
        return sorted(funcionarios_categoria, key=lambda func: func.getNome())

    def getTotalFuncionarios(self):
        return len(self.funcionarios)

    def solicitarDiaria(self, cpf: str):
        for funcionario in self.funcionarios:
            if funcionario.getCpf() == cpf and funcionario.getTipo() != Tipo.TERC:
                nome_funcionario = funcionario.getNome()
                if nome_funcionario in self.diarias:
                    if funcionario.getTipo() == Tipo.PROF and self.diarias[nome_funcionario] < 3:
                        funcionario.salario += 100
                        self.diarias[nome_funcionario] += 1
                        return True
                    elif funcionario.getTipo() == Tipo.STA:
                        return False
                else:
                    self.diarias[nome_funcionario] = 1
                    funcionario.salario += 100
                    return True

        return False

    def partilharLucros(self, valor: float):
        self.partilha = valor / max(1, self.getTotalFuncionarios())
        for funcionario in self.funcionarios:
            funcionario.salario += self.partilha
        return bool(self.funcionarios)

    def iniciarMes(self):
        self.diarias.clear()
        for funcionario in self.funcionarios:
            funcionario.salario -= self.partilha
        return True

    def calcularSalarioDoFuncionario(self, cpf: str):
        funcionario = self.obterFuncionario(cpf)
        return funcionario.getSalario() if funcionario else None

    def calcularFolhaDePagamento(self):
        return sum(f.getSalario() for f in self.funcionarios)