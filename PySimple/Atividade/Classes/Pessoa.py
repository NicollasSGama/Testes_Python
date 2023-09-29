from PySimple.Atividade.Validacao.validacao import *

class Pessoa:
    def __init__(self, nome, sobrenome, cpf, senha, calendario):
        self._nome = nome
        self._sobrenome = sobrenome
        self._cpf = cpf
        self._senha = senha
        self._calendario = calendario

    # ------------------------------------------------------------
    # Definir o getter e o setter
    # ------------------------------------------------------------
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    # ------------------------------------------------------------
    # Sobrenome
    # ------------------------------------------------------------
    @property
    def sobrenome(self):
        return self._sobrenome

    @sobrenome.setter
    def sobrenome(self, sobrenome):
        self._sobrenome = sobrenome

    # ------------------------------------------------------------
    # CPF
    # ------------------------------------------------------------
    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        match cpf:
            case None:
                print('CPF inválido')
            case _:
                self._cpf = validacao_cpf(cpf)

    # ------------------------------------------------------------
    # Senha
    # ------------------------------------------------------------

    @property
    def senha(self):
        return self._senha

    @sobrenome.setter
    def senha(self, senha):
        self._senha = senha

    # ------------------------------------------------------------
    # Calendário
    # ------------------------------------------------------------

    @property
    def calendario(self):
        return self._calendario

    @sobrenome.setter
    def calendario(self, calendario):
        self._calendario = calendario

    # ------------------------------------------------------------
    def __str__(self):
        return f'{self.nome} {self.sobrenome} {self.cpf} {self.senha} {self.calendario}'

print(Pessoa(nome='nicolas', sobrenome='souza', cpf='', senha='123', calendario='1234'))