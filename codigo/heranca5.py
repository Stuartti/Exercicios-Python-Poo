class Produto:
    def __init__(self):
        self.__nome = ""
        self.__preco_base = 0.0

    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        self.__nome = nome
    def get_preco_base(self):
        return self.__preco_base
    def set_preco_base(self, preco_base):
        self.__preco_base = preco_base

    def calcular_preco(self):
        pass

class ProdutoEletronico(Produto):
    def __init__(self):
        Produto.__init__(self)

    def calcular_preco(self):
        return self.get_preco_base() * 0.90

class ProdutoRoupa(Produto):
    def __init__(self):
        Produto.__init__(self)

    def calcular_preco(self):
        return self.get_preco_base() * 0.80

class ProdutoLivro(Produto):
    def __init__(self):
        Produto.__init__(self)

    def calcular_preco(self):
        return self.get_preco_base() * 0.95
