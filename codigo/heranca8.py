class ContaBancaria:
    def __init__(self):
        self.__numero_conta = 0
        self.__saldo = 0
        self.__titular = ""


class ContaCorrente(ContaBancaria):
    def __init__(self):
        ContaBancaria.__init__(self)
        self.__taxa_deposito = 0
        self.__taxa_manutencao_mensal = 0

    def depositar(self, valor):
        self.set_saldo(self.get_saldo() + valor - self.__taxa_deposito)

class ContaPoupanca(ContaBancaria):
    def __init__(self):
        ContaBancaria.__init__(self)
        self.__taxa_juros = 0.0
    def depositar(self):
        pass

