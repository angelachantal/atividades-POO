import pytest
import re
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
    maria = Clientes('Maria')
    
    chip1 = Chips(86999999999, PlanosPre(86999999999))      #teste ok
    chip2 = Chips(86999999999, PlanosPre(86999999999))      #teste ok
    chip3 = Chips(86988888888, PlanosPre(86988888888))      #teste ok
    chip4 = Chips(86977777777, PlanosPos(86977777777))      #teste ok
    chip5 = '86966666666'
	
    assert isinstance (chip1, Chips) == True        #teste ok
    assert isinstance (chip2, Chips) == True        #teste ok
    assert isinstance (chip3, Chips) == True        #teste ok
    assert isinstance (chip4, Chips) == True        #teste ok
	
#     joao.adicionar_chip(chip1)      #teste ok
#     out, err = capfd.readouterr()
#     assert out == '''Associando o chip pré-pago (Número: 86999999999) ao cliente João...
# '''

    assert joao.adicionar_chip(chip1) == 'Associando o chip pré-pago (Número: 86999999999) ao cliente João...'
    
    # maria.adicionar_chip(chip2) 
    # out, err = capfd.readouterr()
    # assert out == 'O número 86999999999 não está disponível.'
    
    assert maria.adicionar_chip(chip1) == 'O número 86999999999 não está disponível.'
    
    assert maria.adicionar_chip(chip3) == 'Associando o chip pré-pago (Número: 86988888888) ao cliente Maria...'
    
    assert maria.adicionar_chip(chip4) == 'Associando o chip pós-pago (Número: 86977777777) ao cliente Maria...'
        
    with pytest.raises(TypeError,match='Insira um chip válido'):
        maria.adicionar_chip(chip5)
    
    maria.listar_chips() 
    out, err = capfd.readouterr()
    assert out == '''- Número: 86988888888 - Tipo: pré-pago
- Número: 86977777777 - Tipo: pós-pago
'''
    assert str(joao) == '''Cliente: João
Chips:
- Número: 86999999999 - Tipo: pré-pago
'''
    

def test_Chips(capfd):
    chip1 = Chips(86999999999, PlanosPre(86999999999))
    chip4 = Chips(86977777777, PlanosPos(86977777777))
    
    assert chip1.realizar_chamada(2) == '''Não há um cliente cadastrado nesse chip.
'''
    
    assert chip4.enviar_sms(3) == '''Não há um cliente cadastrado nesse chip.
'''
    
    assert chip4.consumir_dados_internet(4) == '''Não há um cliente cadastrado nesse chip.
'''
    
    assert str(chip1) == 'Chip sem cliente (Plano pré-pago, Número: 86999999999) → Saldo: R$ 0'
    
    assert str(chip4) == 'Chip sem cliente (Plano pós-pago, Número: 86977777777) → Saldo: R$ 0'
    
    joao = Clientes('João')     
    maria = Clientes('Maria')
    joao.adicionar_chip(chip1)
    maria.adicionar_chip(chip4)
    
    assert str(chip1) == 'Cliente: João (Plano pré-pago, Número: 86999999999) → Saldo: R$ 0'
    
    assert str(chip4) == 'Cliente: Maria (Plano pós-pago, Número: 86977777777) → Saldo: R$ 0'
    

def test_planos_pre(capfd):
    chip1 = Chips(86999999999, PlanosPre(86999999999))
    joao = Clientes('João')     
    joao.adicionar_chip(chip1)
    
    #re.escape evita erros com caracteres especiais como $
    with pytest.raises(ValueError,match=re.escape('''Saldo insuficiente!
Custo: R$ 0.5
Saldo atual: R$ 0.00''')):
        chip1.realizar_chamada(1) # Testa o método __verificar_saldo
    
    assert chip1.plano.adicionar_saldo(100) == 'Recarga de R$ 100.00 realizada com sucesso!'
    
    assert chip1.plano.mostrar_saldo() == 'Saldo atual: R$ 100.00'
    
    chip1.realizar_chamada(2)
    out, err = capfd.readouterr()
    assert out == '''Cliente João fez uma ligação de 2 minuto(s) (custo: R$ 1.00)...
Saldo atual: R$ 99.00
'''
    
    chip1.enviar_sms(10)
    out, err = capfd.readouterr()
    assert out == '''Cliente João enviou 10 SMS (custo: R$ 3.00)...
Saldo atual: R$ 96.00
'''
    chip1.consumir_dados_internet(4)
    out, err = capfd.readouterr()
    assert out == '''Cliente João consumiu 4GB de internet (custo: R$ 20.00)...
Saldo atual: R$ 76.00
'''
    
    # chip1.plano.consultar_status()
    assert str(chip1.plano) == '''## Custo total
### Consumo
- Chamadas: R$ 1.00
- SMS: R$ 3.00
- Internet: R$ 20.00

### Fatura
- Consumo total: R$ 24.00
- Saldo atual: R$ 76.00
'''
    
