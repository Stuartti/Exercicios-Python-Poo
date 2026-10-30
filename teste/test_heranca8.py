from codigo.heranca8 import *

def test_deve_depositar_conta_corrente():
    conta = ContaCorrente()
    conta.set_taxa_deposito(2.00)
    conta.depositar(100.00)
    assert conta.get_saldo() == 98.00