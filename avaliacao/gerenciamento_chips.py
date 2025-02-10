# Avaliação POO
# Equipe 2: Ângela Chantal; Murilo Monte; Renan Miqueias; Thiário Lima
## from random import randint
# fazer verificações


class Operadoras:
    def __init__(self):
        self.__clientes_lista = []
        pass

    def adicionar_cliente(self, cliente):
        self.__clientes_lista.append(cliente)
        print(f"Cadastrando cliente {cliente.nome}")
        # Cadastrando cliente João...

    def listar_clientes(self):
        print("Clientes")
        for cliente in self.__clientes_lista:
            print(f"- {cliente.nome}")
        # Clientes:
        # - João
        # - Maria

    def __str__(self):
        pass


class Clientes:
    def __init__(self, nome):
        self.__nome = nome
        self.__chips_lista = []

    @property
    def nome(self):
        return self.__nome

    @property
    def chips(self):
        return self.__chips

    def adicionar_chip(self, chip):
        self.__chips_lista.append(chip)
        print(
            f"Associando o chip {chip.tipo}-pago (Número: {chip.numero}) ao cliente {self.__nome}"
        )

    def listar_chips(self):
        chips = ""
        for chip in self.__chips_lista:
            chips += f"- Número: {chip.numero} - Tipo: {chip.tipo}\n"
        return chips

    def __str__(self):
        nome = self.__nome
        chip = self.listar_chips()
        return f"Cliente: {nome}\nChips:\n{chip}"


class Chips:
    def __init__(self, tipo, numero, cliente, plano):
        self.__tipo = tipo
        self.__numero = numero
        self.__plano = plano  # instancia de plano
        self.__cliente = cliente
        self.__saldo = 0

    @property
    def tipo(self):
        return self.__tipo
    
    @property
    def plano(self):
        return self.__plano

    @property
    def numero(self):
        return self.__numero

    @property
    def cliente(self):
        return self.__cliente

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    ## Métodos polimórficos
    def realizar_chamada(self, duracao):
        # Deduz o custo da chamada do saldo (R$ 0,50/min).
        custo = 0.5 * duracao
        self.__plano.realizar_chamada(self, duracao, custo)

    def enviar_sms(self, quantidade):
        # Deduz o custo dos SMS do saldo (R$ 0,30/SMS).
        custo = 0.3 * quantidade
        self.__plano.enviar_sms(self, quantidade, custo)

    def consumir_dados_internet(self, gb):
        # Deduz o custo do saldo (R$ 5,00/GB).
        custo = 5 * gb
        self.__plano.consumir_dados_internet(self, gb, custo)

    def adicionar_saldo(self, saldo):
        self.__saldo = saldo
        print(f"Recarga de R$ {saldo:.2f} realizada com sucesso!")

    def mostrar_saldo(self):
        return f"{self.__saldo:.2f}"

    def __str__(self):
        # João (Pré-pago, Número: 11987654321) → Saldo: R$ 33,50
        pass


class Planos:
    def __init__():
        ...

    def calcular_custo(self):
        pass

    def __str__(self):
        pass


class PlanosPre(Planos):
    def __init__(self):
        super().__init__()
        self.__consumo_sms = 0
        self.__consumo_chamada = 0
        self.__consumo_internet = 0
        self.__consumo_total = 0

    def calcular_custo(self):
        return (
            f"Chamadas: R$ {self.__consumo_total}"
            f"SMS: R$ {self.__consumo_total}"
            f"Internet: R$ {self.__consumo_total}"
            f"Consumo total: R$ {self.__consumo_total}"
        )

    def realizar_chamada(self, chip, duracao, custo):
        # Pré-pago: Deduz o custo da chamada do saldo (R$ 0,50/min).
        chip.saldo -= custo
        self.__consumo_chamada = custo
        print(
            f"Cliente {chip.cliente.nome} fez uma ligação de {duracao} minutos (custo: R$ {custo:.2f})..."
        )
        print(f"Saldo atual: {chip.mostrar_saldo()}")

    def enviar_sms(self, chip, quantidade, custo):
        chip.saldo -= custo
        self.__consumo_sms = custo
        print(
            f"Cliente {chip.cliente.nome} enviou {quantidade} SMS (custo: R$ {custo:.2f})..."
        )
        print(f"Saldo atual: {chip.mostrar_saldo()}")

    def consumir_dados_internet(self, chip, gb, custo):
        chip.saldo -= custo
        self.__consumo_internet = custo
        print(
            f"Cliente {chip.cliente.nome} consumiu  {gb}GB de internet (custo: R$ {custo:.2f})..."
        )
        print(f"Saldo atual: {chip.mostrar_saldo()}")

    def __str__(self):
        return super().__str__() + f"."


class PlanosPos(Planos):
    def __init__(self):
        super().__init__()
        pass

    def calcular_custo(self): ...
    def realizar_chamada(self, duracao):
        print("Chamada Pos")

    def enviar_sms(self, quantidade): ...
    def consumir_dados_internet(self, gb): ...

    def __str__(self):
        return super().__str__() + f"."
