import pytest
from gerenciamento_chips import *

#Executar pytest test_gerenciamento_chips.py
def test_Operadoras():
    operadora = Operadoras()
    assert str(operadora) == 'Operadora ativa.'

def test_adicionar_cliente(self, cliente):
    # Entrada: João | Saída Esperada:  Cadastrando cliente João...
    # Entrada: Maria | Saída Esperada:  Cadastrando cliente Maria...
    # Entrada: João | Saída Esperada:  O cliente João já está cadastrado!
    pass 

def test_listar_clientes(self):
    # Entrada: operadora | Saída Esperada:  
    # Clientes:
    # - João
    # - Maria
    pass
    
def test_adicionar_chip(chip):
    #Entrada para chip1 pré de João: 86999999999 | Saída esperada: Associando o chip pré-pago (Número: 86999999999) ao cliente João...
    
    #Entrada para chip2 pré de Maria: 86999999999 | Saída esperada: O número 86999999999 não está disponível..
    
    #Entrada para chip2 pré de Maria: 86988888888 | Saída esperada: Associando o chip pré-pago (Número: 86988888888) ao cliente Maria...
    
    #Entrada para chip3 pós de Maria: 86977777777 | Saída esperada: Associando o chip pos-pago (Número: 86977777777) ao cliente Maria...
    pass

def test_listar_chips():
    # Entrada: Maria | Saída esperada: 
    # - Número: {86988888888} - Tipo: pré-pago
    # - Número: {86977777777} - Tipo: pós-pago
    pass

def test_Clientes():
    cliente = Clientes('João')
    assert str(cliente) == 'Cliente: João\nChips:86999999999'

def test_realizar_chamada(duracao):
    pass
    # - Pré-pago?
    # - Pós-pago?
def test_enviar_sms(quantidade) :
    pass
    # - Pré-pago?
    # - Pós-pago?
def test_consumir_dados_internet(gb):
    pass
    # - Pré-pago?
    # - Pós-pago?
    
def test_calcular_custo(meses) :
    pass
    # - Pré-pago?
    # - Pós-pago?
    
def test_Chips():
    assert str(chip1) == 'João  (pré-pago, Número: 86999999999) → Saldo: R$ {self.__plano.consumo_total}'
    
def test_Planos():
    # assert str(chip1) == 'João  (pré-pago, Número: 86999999999) → Saldo: R$ {self.__plano.consumo_total}'