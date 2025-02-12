from gerenciamento_chips import *

vivo = Operadoras()
alice = Clientes('Alice')
vivo.adicionar_cliente(alice)
vivo.listar_clientes()

# É possível passar diretamente uma instância sem atribuir ela à uma variável
chip1 = Chips('55 86 98826-0121', alice, PlanosPre())
chip2 = Chips('55 86 98855-5555', alice, PlanosPos())

alice.adicionar_chip(chip1)
alice.adicionar_chip(chip2)
# alice.adicionar_chip('pre', '55 86 98826657-0121')
# instanciar manualmente o chip, assim fica mais fácil acessar os métodos do chip
# Ao adicionar um chip, passar uma instância do plano ou adicionar o plano no instanciamento de chip?
# Ao chamar o chip.realizar_chamada(), o mesmo chama o método do plano ao qual herda

chip1.plano.adicionar_saldo(30)
chip1.realizar_chamada(2)
chip1.enviar_sms(3)
chip1.consumir_dados_internet(4)

# print(chip1.plano.calcular_custo())
# print(chip1.plano.consultar_status())

chip2.realizar_chamada(2)
chip2.enviar_sms(3)
chip2.consumir_dados_internet(4)
print(chip2.plano.calcular_custo())
print('--------------------')
print(chip2.plano.consultar_status())
# print(alice)
