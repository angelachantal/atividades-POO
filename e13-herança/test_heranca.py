import pytest
from heranca import *
    
def testarContaCorrente():
    conta = ContaCorrente(1234, 20000)
    #conta.numero = 1235     #não pode ser alterado#não pode ser alterado
    #conta.saldo = 1000      #não pode ser alterado
    assert str(conta) == 'Conta: 1234  Saldo: R$ 20000.00'      #correto
    
def testarCreditar():
    conta = ContaCorrente(1234, 20000)  
    assert conta.saldo + 100 == conta.creditar(100)     #correto
    
def testarDebitar():
    conta = ContaCorrente(1234, 20000)
    assert conta.saldo - 100 == conta.debitar(100)      #correto
    
def testarTransferir():
    conta1 = ContaCorrente(1234, 20000)     #correto
    conta2 = ContaCorrente(1235, 100)   #correto
    conta1.transferir(conta2, 100)      #correto
    assert str(conta1) == 'Conta: 1234  Saldo: R$ 19900.00'
    assert str(conta2) == 'Conta: 1235  Saldo: R$ 200.00' 
    
def testarPoupanca():
    conta = ContaPoupanca(1236, 3000, 1.5)
    #conta.numero = 1235     #não pode ser alterado#não pode ser alterado
    #conta.saldo = 1000      #não pode ser alterado
    assert str(conta) == 'Conta: 1236  Saldo: R$ 3000.00    Taxa de Juros: 1.5%'        #correto
    
def testarRender():
    conta3 = ContaPoupanca(1235, 1000, 1.5)
    rendimento = conta3.saldo * (1.5/100)
    assert conta3.saldo + rendimento == conta3.renderJuros()        #correto
    
def calculaImposto():
    conta3 = ContaImposto(1235, 1000, 1.5)
    imposto = conta3.saldo * (1.5/100)
    assert conta3.saldo - imposto == conta3.calculaImposto()
    

#Executar pytest test_heranca.py
