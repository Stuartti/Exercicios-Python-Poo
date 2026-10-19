from codigo.heranca3 import *

def teste_calculo_area_circulo():
    circulo = Circulos()
    circulo.set_raio(2)
    area = circulo.calcular_area()
    assert area == 12.56

def teste_calculo_perimetro_circulo():
    circulo = Circulos()
    circulo.set_raio(2)
    perimetro = circulo.calcular_perimetro()
    assert perimetro == 12.56

def teste_calculo_area_retangulo():
    retangulo = Retangulos()
    retangulo.set_altura(5)
    retangulo.set_largura(2)
    area2 = retangulo.calcular_area()
    assert area2 == 10

def teste_calculo_perimetro_retangulo():
    retangulo = Retangulos()
    retangulo.set_altura(5)
    retangulo.set_largura(2)
    perimetro2 = retangulo.calcular_perimetro()
    assert perimetro2 == 14