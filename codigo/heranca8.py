class ContaBancaria:
    def __init__(self):
        self.__numero_conta = 0
        self.__saldo = 0
        self.__titular = ""

    def set_saldo(self, valor):
            self.__saldo = valor

    def get_saldo(self):
        return self.__saldo


class ContaCorrente(ContaBancaria):
    def __init__(self):
        ContaBancaria.__init__(self)
        self.__taxa_deposito = 0.0
        self.__taxa_manutencao_mensal = 0.0
    def set_taxa_deposito(self, taxa):
        self.__taxa_deposito = taxa # CORRIGIDO: usando os 2 underscores
    def get_taxa_deposito(self):
        return self.__taxa_deposito
    def set_taxa_manutencao_mensal(self, taxa):
        self.__taxa_manutencao_mensal = taxa
    def get_taxa_manutencao_mensal(self):
        return self.__taxa_manutencao_mensal
    def depositar(self, valor):
        novo_saldo = self.get_saldo() + valor - self.__taxa_deposito
        self.set_saldo(novo_saldo)

class ContaPoupanca(ContaBancaria):
    def __init__(self):
        ContaBancaria.__init__(self)
        self.__taxa_juros = 0.0
    def depositar(self):
        pass

