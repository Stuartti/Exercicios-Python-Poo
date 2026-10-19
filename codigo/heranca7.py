class Produto:
    def __init__(self):
        self.__nome = ""
        self.__preco_unitario = 0.0
        self.__quantidade_estoque = 0.0

    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        self.__nome = nome
    def get_preco_unitario(self):
        return self.__preco_unitario
    def set_preco_unitario(self, preco_unitario):
        self.__preco_unitario = preco_unitario
    def set_quantidade_estoque(self, quantidade_estoque):
        self.__quantidade_estoque = quantidade_estoque
    def get_quantidade_estoque(self):
        return self.__quantidade_estoque
    ## getters e setters
    def vender_quantidade(self, quantidade_desejada):
        if quantidade_desejada <= self.__quantidade_estoque:
            preco_total = self.calcularPreco(quantidade_desejada)
            self.__quantidade_estoque -= quantidade_desejada

    def calcularPreco(self):
        pass

class ProdutoEletronico(Produto):
    def __init__(self):
        Produto.__init__(self)
        self.__quantidade_cliente = 0

    def get_quantidade_cliente(self):
        return self.__quantidade_cliente
    def set_quantidade_cliente(self, quantidade_cliente):
        self.__quantidade_cliente = quantidade_cliente
    def calcularPreco(self):
        return self.get_preco_unitario() * self.__quantidade_cliente

class ProdutoRoupa(Produto):
    def __init__(self):
        Produto.__init__(self)
        self.__desconto = 0
        self.__quantidade_cliente = 0

    def get_quantidade_cliente(self):
        return self.__quantidade_cliente
    def set_quantidade_cliente(self, quantidade_cliente):
        self.__quantidade_cliente = quantidade_cliente
    def get_desconto(self):
        return self.__desconto
    def set_desconto(self, desconto):
        self.__desconto = desconto

    def calcularPreco(self):
        preco_bruto = self.get_preco_unitario() * self.__quantidade_cliente
        valor_desconto = preco_bruto * self.__desconto
        preco_final = preco_bruto - valor_desconto
        return preco_final

class ProdutoAlimento(Produto):
    def __init__(self):
        Produto.__init__(self)
        self.__quilo = 0.0

    def get_quilo(self):
        return self.__quilo
    def set_quilo(self, quilo):
        self.__quilo = quilo

    def calcularPreco(self):
        return self.__quilo * self.get_preco_unitario()
