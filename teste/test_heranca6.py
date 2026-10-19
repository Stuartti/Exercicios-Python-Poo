from codigo.heranca6 import *

def teste_calculo_preco_voo_domestico():
    voo = VooDomestico()
    voo.set_distancia(360.0)
    voo.set_fator_domestico(0.15)
    preco_base = voo.calcular_voo()
    assert preco_base == 54.0

def teste_calculo_preco_voo_internacional():
    voo = VooInternacional()
    voo.set_distancia(1000.0)
    voo.set_fator_internacional(0.10)
    voo.set_taxa_conversao(5.0)
    preco_base = voo.calcular_voo()
    assert preco_base == 500.0