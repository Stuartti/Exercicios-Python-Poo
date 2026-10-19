class FormaGeometrica:
    def __init__(self):
        pass
    def calcular_area(self):
        pass
    def calcular_perimetro(self):
        pass

class Circulos(FormaGeometrica):
    def __init__(self):
        self.__raio = 0.0

    def get_raio(self):
        return self.__raio
    def set_raio(self, raio):
        self.__raio = raio

    def calcular_area(self):
       return 3.14 * (self.__raio ** 2)

    def calcular_perimetro(self):
        return 2 * 3.14 * self.__raio

class Retangulos(FormaGeometrica):
    def __init__(self):
        self.__altura = 0
        self.__largura = 0

    def get_altura(self):
        return self.__altura
    def set_altura(self, altura):
        self.__altura = altura
    def get_largura(self):
        return self.__largura
    def set_largura(self, largura):
        self.__largura = largura

    def calcular_area(self):
        return self.__altura * self.__largura
    def calcular_perimetro(self):
        return 2 * (self.__largura + self.__altura)

