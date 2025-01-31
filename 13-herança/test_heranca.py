import pytest
from heranca import *
    
def testarContaCorrente():
    conta = ContaCorrente(1234, 20000)
    assert str(conta) == 'Conta: 1234  Saldo: R$ 20000.00' #correto
    
def testarCreditar():
    conta = ContaCorrente(1234, 20000)  
    assert conta.saldo + 100 == conta.creditar(100)
    
def testarDebitar():
    conta = ContaCorrente(1234, 20000)
    assert conta.saldo - 100 == conta.debitar(100)
    
def testarTransferir():
    conta1 = ContaCorrente(1234, 20000)
    conta2 = ContaCorrente(1235, 100)
    conta1.transferir(conta2, 100)
    assert str(conta1) == 'Conta: 1234  Saldo: R$ 19900.00'
    assert str(conta2) == 'Conta: 1235  Saldo: R$ 200.00' 
    
    # assert conta.transferir(100) == 
    # assert conta.saldo == 
    
#Executar pytest test_heranca.py
