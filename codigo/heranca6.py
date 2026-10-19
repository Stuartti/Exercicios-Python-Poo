class Voo:
    def __init__(self):
        self.__origem = ""
        self.__distancia = 0.0
        self.__destino = ""
        self.__data_voo = ""

    def get_origem(self):
        return self.__origem
    def set_origem(self, origem):
        self.__origem = origem
    def get_distancia(self):
        return self.__distancia
    def set_distancia(self, distancia):
        self.__distancia = distancia
    def get_destino(self):
        return self.__destino
    def set_destino(self, destino):
        self.__destino = destino
    def get_data_voo(self):
        return self.__data_voo
    def set_data_voo(self, data_voo):
        self.__data_voo = data_voo


class VooDomestico(Voo):
    def __init__(self):
        Voo.__init__(self)
        self.__fator_domestico = 0.0

    def get_fator_domestico(self):
        return self.__fator_domestico
    def set_fator_domestico(self, fator_domestico):
        self.__fator_domestico = fator_domestico

    def calcular_voo(self):
        preco_base = self.get_distancia() * self.__fator_domestico
        return preco_base

class VooInternacional(Voo):
    def __init__(self):
        Voo.__init__(self)
        self.__fator_internacional = 0.0
        self.__taxa_conversao = 0.0

    def get_fator_internacional(self):
        return self.__fator_internacional
    def set_fator_internacional(self, fator_internacional):
        self.__fator_internacional = fator_internacional
    def get_taxa_conversao(self):
        return self.__taxa_conversao
    def set_taxa_conversao(self, taxa_conversao):
        self.__taxa_conversao = taxa_conversao


    def calcular_voo(self):
        preco_base = (self.get_distancia() * self.get_fator_internacional()) * self.__taxa_conversao
        return preco_base
