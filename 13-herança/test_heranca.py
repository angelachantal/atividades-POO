import pytest
from heranca import *

def tnome():
    conta = ContaCorrente(1234, 20000)
    assert conta.ceditar() == ""
    assert conta.debitar() == ""
    assert conta.transferir() == None
    assert conta.saldo() == None
    assert str(conta) == f'Conta Corrente: {}'