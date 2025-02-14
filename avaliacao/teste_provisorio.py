# Avaliação POO
# Equipe 2: Ângela Chantal; Murilo Monte; Renan Miqueias; Thiário Lima

from gerenciamento_chips import *

## Criando operadora
vivo = Operadoras(
    nome="Vivo",
)

## Criando cliente
alice = Clientes(
    nome="Alice",
)

hiromi = Clientes(
    nome="Hiromi",
)

## Adicionando clientes a operadora
vivo.adicionar_cliente(alice)
vivo.adicionar_cliente(hiromi)
vivo.listar_clientes()

## Adicionando chips a cliente
chip1 = Chips(
    numero="55 86 98765-4321",
    plano=PlanosPre(
        "55 86 98765-4321",
    ),
)
print(alice.adicionar_chip(chip1))

chip2 = Chips(
    numero="55 86 98855-5555",
    plano=PlanosPos(
        "55 86 98855-5555",
    ),
)
print(alice.adicionar_chip(chip2))

## Listando chips de cliente
alice.listar_chips()

## Mostrando os dados do cliente
print(alice)

## Testando planoPre
print(chip1.plano.adicionar_saldo(30))
chip1.realizar_chamada(2)
chip1.enviar_sms(3)
chip1.consumir_dados_internet(4)

chip1.plano.adicionar_saldo(11.9)
chip1.consumir_dados_internet(4)

print(chip1.plano.consultar_status())

## Testes plano pós-pago
chip2.plano.set_vencimento("12/03/2025")
chip2.realizar_chamada(2)
chip2.enviar_sms(3)
chip2.consumir_dados_internet(4)

print(chip2.plano.consultar_status())
print(chip2.plano.calcular_custo(3))
