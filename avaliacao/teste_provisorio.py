from gerenciamento_chips import Operadoras, Clientes

vivo = Operadoras()
alice = Clientes('Alice')
vivo.adicionar_cliente(alice)
vivo.listar_clientes()

# vivo.adicionar_cliente(alice)

alice.adicionar_chip('pos', '55 86 98826-0121')
alice.adicionar_chip('pre', '55 86 98826657-0121')
print(alice.listar_chips())
print(alice)
