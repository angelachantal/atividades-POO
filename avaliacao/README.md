# Trabalho Final da Disciplina Programação Orientada a Objetos - Turma 266

# Equipe: 

- Ângela Chantal
- Murilo Monte
- Renan Miqueias
- Thiário Lima

# Reuso com Python

**Associação de classes, Herança, Polimorfismo**

Implementar um sistema de gerenciamento de chips de telefonia celular para uma operadora. 

O sistema deve permitir cadastrar clientes, associá-los a chips pré ou pós-pago e gerenciar as recargas, cobranças de faturas e o uso de serviços como chamadas, SMS e dados móveis.

## `class Operadoras` 

Pode conter múltiplos clientes (associação 1:N).

`adicionar_cliente(self, cliente)` - Adicionar um cliente à operadora

    Cadastrando cliente João...

    Cadastrando cliente Maria...

`listar_clientes(self)` - Listar todos os clientes cadastrados

## `class Clientes`: 

Representa um cliente da operadora, podendo possuir um ou mais chips de diferentes tipos.

`adicionar_chip(chip)` - Associa um novo chip ao cliente/ Registrar múltiplos chips (pré e pós-pago).

    Associando chip pré-pago (Número: 11987654321) ao cliente João...
    
    Associando chip pós-pago (Número: 21912345678) ao cliente Maria...

`listar_chips()` - Exibe todos os chips cadastrados do cliente/ Listar os chips ativos do cliente.

## `class Chips`: 

Representa um chip de telefonia celular, armazenando o número e o tipo (pré ou pós-pago).

Exibe detalhes do chip, incluindo número e tipo de plano.

    João (Pré-pago, Número: 11987654321) → Saldo: R$ 33,50

    Maria (Pós-pago, Número: 21912345678) → Fatura: R$ 155,50

## `class Plano`

Superclasse que representa um plano de telefonia, com um custo associado.

<!-- Estou na dúvida se os métodos abaixo entram aqui, ou na classe que trará o método polimórfico. -->

`calcular_custo(meses)` - Retorna o custo do plano com base no período de uso.

`realizar_chamada(duracao)` - Realiza uma chamada e debita do saldo ou adiciona na fatura (R$ 0,50/min).

`enviar_sms(quantidade)` - Envia mensagens SMS e debita do saldo ou adiciona na fatura (R$ 0,30/SMS).
    
`consumir_dados_internet(gb)` - Consome um pacote de dados e debita do saldo ou adiciona na fatura (R$ 5,00/GB).

### `class PlanoPrePago`

`saldo` - Atributo que armazena créditos disponíveis.
<!-- Criar método de recarga? -->

    Recarga de R$ 50,00 realizada com sucesso!

    Saldo atual: R$ 50,00

`realizar_chamada(duracao)` - Método sobrescrito. Realiza uma chamada e deduz o custo da chamada do saldo.

    Cliente João fez uma ligação de 10 minutos (custo: R$ 5,00)...
    
    Novo saldo: R$ 45,00

`enviar_sms(quantidade)` - Método sobrescrito. Envia mensagens SMS e deduz o custo dos SMS do saldo.

    Cliente João enviou 5 SMS (custo: R$ 1,50)...

    Novo saldo: R$ 43,50

`consumir_dados_internet(gb)` - Método sobrescrito. Consome um pacote de dados e deduz o custo do saldo.

    Cliente João consumiu 2GB de internet (custo: R$ 10,00)...
    
    Novo saldo: R$ 33,50

Utilizar exceções para tratar casos como saldo insuficiente para o pré-pago.

### `class PlanoPosPago`

`fatura_mensal` - Atributo que armazena o valor da fatura do mês.

    Fatura mensal de R$ 120,00 gerada.

`realizar_chamada(duracao)` - Método sobrescrito. Realiza uma chamada e adiciona o custo da chamada na fatura mensal.

    Cliente Maria fez uma ligação de 15 minutos (custo: R$ 7,50)...

    Nova fatura mensal: R$ 127,50

`enviar_sms(quantidade)` - Método sobrescrito. Envia mensagens SMS e adiciona o adiciona o custo na fatura mensal.

    Cliente Maria enviou 10 SMS (custo: R$ 3,00)...

    Nova fatura mensal: R$ 130,50

`consumir_dados_internet(gb)` - Método sobrescrito. Consome um pacote de dados e adiciona o adiciona o custo na fatura mensal.

    Cliente Maria consumiu 5GB de internet (custo: R$ 25,00)...

    Nova fatura mensal: R$ 155,50

Utilizar exceções para tratar casos como fatura em atraso para o pós-pago.

## Implementação extra:

Método polimórfico para imprimir os detalhes do consumo do chip, incluindo chamadas, SMS e dados móveis utilizados.

`class_xxxxx`

Criar um arquivo de testes utilizando pytest, cobrindo diferentes cenários de recarga e faturamento.

`test_adicionar_cliente(self, cliente)` 

`test_listar_clientes(self)` 

`test_adicionar_chip(chip)` 

`test_listar_chips()` 

`teste do __str__ do chip`

`test_calcular_custo(meses)` 

<!-- - Pré-pago?
- Pós-pago? -->

`test_realizar_chamada(duracao)`

- Pré-pago
- Pós-pago

`test_enviar_sms(quantidade)` 

- Pré-pago
- Pós-pago

`test_consumir_dados_internet(gb)`

- Pré-pago
- Pós-pago

`Teste da recarga?`

`Teste da fatura mensal?`

`Testes das exceções`.