class Funcionario:
    def __init__(self):
        self.__salario = 0
        self.__calcular_pagamento = 0

    def get_salario(self):
        return self.__salario
    def set_salario(self, salario):
        self.__salario = salario
    def get_calcular_pagamento(self):
        return self.__calcular_pagamento
    def set_calcular_pagamento(self, calcular_pagamento):
        self.__calcular_pagamento = calcular_pagamento

    def calcular_pagamento(self):
        pass

class FuncionarioComum(Funcionario):
    def __init__(self):
        Funcionario.__init__(self)
    pass

class Gerente(Funcionario):
    def __init__(self):
        Funcionario.__init__(self)
        self.__bonus_fixo = 0

    def get_bonus_fixo(self):
        return self.__bonus_fixo
    def set_bonus_fixo(self, bonus_fixo):
        self.__bonus_fixo = bonus_fixo

    def calcular_pagamento(self):
        return self.__bonus_fixo + self.get_salario()

class Diretor(Funcionario):
    def __init__(self):
        Funcionario.__init__(self)
        self.__lucro = 0
        self.__participacao = 0

    def set_lucro(self, lucro):
        self.__lucro = lucro
    def get_lucro(self):
        return self.__lucro
    def set_participacao(self, participacao):
        self.__participacao = participacao
    def get_participacao(self):
        return self.__participacao

    def calcular_pagamento(self):
        return ((self.__participacao / 100) * self.__lucro) + self.get_salario()
