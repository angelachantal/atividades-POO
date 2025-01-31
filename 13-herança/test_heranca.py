import pytest
from heranca import *
    
def testarContaCorrente():
    conta = ContaCorrente(1234, 20000)
    assert str(conta) == 'Conta: 1234  Saldo: R$ 20000.00' #correto
    assert conta.saldo + 100 == conta.creditar(100)
    assert conta.saldo - 100 == conta.debitar(100)
    # assert conta.transferir(100) == 
    # assert conta.saldo == 
    
#Executar pytest test_heranca.py
