from codigo.heranca7 import *

def teste_produto_eletronico():
    p = ProdutoEletronico()
    p.set_nome("Smartphone")
    p.set_preco_unitario(2000.0)
    p.set_quantidade_estoque(5)

def teste_produto_roupa():
    p = ProdutoRoupa()
    p.set_nome("Camisa Polo")
    p.set_preco_unitario(100.0)
    p.set_quantidade_estoque(10)
    p.set_desconto(0.10)

def test_produto_alimento():
    p = ProdutoAlimento()
    p.set_nome("Queijo Mussarela")
    p.set_preco_unitario(50.0)
    p.set_quantidade_estoque(15.0)
    quantidade_comprada = 2.5
    preco_esperado = 50.0 * quantidade_comprada
    assert preco_esperado == 125