import pytest
from gerenciamento_chips import *

#Executar pytest test_gerenciamento_chips.py

def test_Operadoras(capfd):     #teste ok
    vivo = Operadoras('Vivo')
    assert str(vivo) == '''Operadora Vivo ativa.
'''      #teste ok

    with pytest.raises(TypeError,match='Só é possível adicionar clientes válidos.'):
        vivo.adicionar_cliente('João')      #teste ok
        
    joao = Clientes('João')
    vivo.adicionar_cliente(joao)
    out, err = capfd.readouterr() 
    assert out == '''Cadastrando cliente João...

'''        #teste ok
    
    maria = Clientes('Maria')
    vivo.adicionar_cliente(maria) 
    out, err = capfd.readouterr()
    assert out == '''Cadastrando cliente Maria...

'''     #teste ok

    vivo.adicionar_cliente(joao)
    out, err = capfd.readouterr()
    assert out == '''O cliente João já está cadastrado!

'''        #teste ok
         
    vivo.listar_clientes()      #teste ok
    out, err = capfd.readouterr()
    assert out == '''Clientes:
- João
- Maria
''' 
    assert isinstance (joao, Clientes) == True      #teste ok
    
    assert isinstance (maria, Clientes) == True      #teste ok
    
    assert isinstance (vivo, Operadoras) == True      #teste ok

    
def test_Clientes(capfd):
    # vivo = Operadoras('Vivo')
    # vivo.adicionar_cliente(joao)
    joao = Clientes('João')     #teste ok
    
    chip1 = Chips(86999999999, PlanosPre(86999999999))      #teste ok
    chip2 = Chips(86999999999, PlanosPre(86999999999))      #teste ok
    chip3 = Chips(86988888888, PlanosPre(86988888888))      #teste ok
    chip4 = Chips(86977777777, PlanosPos(86977777777))      #teste ok
	
    assert isinstance (chip1, Chips) == True        #teste ok
    assert isinstance (chip2, Chips) == True        #teste ok
    assert isinstance (chip3, Chips) == True        #teste ok
    assert isinstance (chip4, Chips) == True        #teste ok
	
    joao.adicionar_chip(chip1) 
    out, err = capfd.readouterr()
    assert out == 'Associando o chip pré-pago (Número: 86999999999) ao cliente João...'
