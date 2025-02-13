from gerenciamento_chips import *

## Criando operadora
vivo = Operadoras(
    nome="Vivo",
)

## Criando cliente
alice = Clientes(
    nome="Alice",
)

## Adicionando clientes a operadora
vivo.adicionar_cliente(alice)
vivo.listar_clientes()

## Adicionando chips a cliente
chip1 = Chips(
    numero="55 86 98826-0121",
    cliente=alice,
    plano=PlanosPre(),
)

chip2 = Chips(
    numero="55 86 98855-5555",
    cliente=alice,
    plano=PlanosPos(),
)

## Listando chips de cliente
print(alice.listar_chips())

# print(chip2.plano.calcular_custo())

# chip1.plano.adicionar_saldo(30)
# chip1.realizar_chamada(2)
# chip1.enviar_sms(3)
# chip1.consumir_dados_internet(4)
# chip1.plano.adicionar_saldo(11.9)
# chip1.consumir_dados_internet(4)
# print(chip1.plano.calcular_custo())
# # print(chip1.plano.consultar_status())

# chip2.plano.set_vencimento('12/01/2025')
chip2.realizar_chamada(2)
chip2.enviar_sms(3)
chip2.consumir_dados_internet(4)
print(chip2.plano.calcular_custo())
chip1.plano.set_vencimento()
# # print(alice)
