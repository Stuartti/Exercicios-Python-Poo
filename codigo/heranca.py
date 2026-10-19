class Pessoa:
    def __init__(self):
        self.__nome = ""
        self.__cpf = 0

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, cpf):
        self.__cpf = cpf


class Professor(Pessoa):
    def __init__(self):
        Pessoa.__init__(self)
        self.__titulacao = ""

    def get_titulacao(self):
        return self.__titulacao

    def set_titulacao(self, titulacao):
        self.__titulacao = titulacao

    def exibir_dados(self):
        return f"Nome: {self.get_nome()}, Titulação: {self.__titulacao}"


class Aluno(Pessoa):
    def __init__(self):
        Pessoa.__init__(self)
        self.__media = 0.0
        self.__matricula = 0

    def calcular_media(self, nota1, nota2):
        self.__media = (nota1 + nota2) / 2
        return self.__media

    def get_media(self):
        return self.__media

    def set_media(self, media):
        self.__media = media

    def get_matricula(self):
        return self.__matricula

    def set_matricula(self, matricula):
        self.__matricula = matricula



class AlunoEnsinoMedio(Aluno):
    def __init__(self):
        Aluno.__init__(self)

    def aprovacao(self):
        if self.get_media() >= 6:
            return True
        else:
            return False

    def exibir_dados(self):
        return f"Nome: {self.get_nome()}, Matrícula: {self.get_matricula()}, Aprovado: {self.aprovacao()}"


class AlunoGraduacao(Aluno):
    def __init__(self):
        Aluno.__init__(self)

    def aprovacao(self):
        if self.get_media() >= 7:
            return True
        else:
            return False

    def exibir_dados(self):
        return f"Nome: {self.get_nome()}, Matrícula: {self.get_matricula()}, Aprovado: {self.aprovacao()}"