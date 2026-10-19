from codigo.heranca5 import *

def teste_calculo_preco_eletronico():
    eletronico = ProdutoEletronico()
    eletronico.set_preco_base(100.0)
    preco_final = eletronico.calcular_preco()
    assert preco_final == 90.0

def teste_calculo_preco_roupa():
    roupa = ProdutoRoupa()
    roupa.set_preco_base(50)
    preco_final = roupa.calcular_preco()
    assert preco_final == 40

def teste_calculo_preco_livro():
    livro = ProdutoLivro()
    livro.set_preco_base(200)
    preco_final = livro.calcular_preco()
    assert preco_final == 190