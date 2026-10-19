from codigo.heranca4 import *

def test_salario_FuncionarioComum():
    funcionario = Funcionario()
    funcionario.set_salario(1500)
    assert funcionario.get_salario() == 1500

def test_salario_gerente():
    funcionario = Gerente()
    funcionario.set_salario(1500)
    funcionario.set_bonus_fixo(1500)
    assert funcionario.calcular_pagamento() == 3000

def test_salario_diretor():
    funcionario = Diretor()
    funcionario.set_salario(2000)
    funcionario.set_lucro(50000)
    funcionario.set_participacao(5)
    assert funcionario.calcular_pagamento() == 4500