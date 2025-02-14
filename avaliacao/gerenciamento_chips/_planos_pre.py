from ._planos import Planos


class PlanosPre(Planos):
    def __init__(self, numero):
        super().__init__()
        self.__tipo = "pré"
        self.__saldo = 0
        self.__numero = numero

        # print(f'## Chip criado!\nNúmero: {self.__numero}\nTipo: {self.__tipo}')

    @property
    def tipo(self):
        return self.__tipo

    def consultar_status(self):
        self.consumo_total = (
            self.consumo_sms + self.consumo_chamada + self.consumo_internet
        )
        return (
            f"## Custo total\n"
            f"### Consumo\n"
            f"- Chamadas: R$ {self.consumo_chamada:.2f}\n"
            f"- SMS: R$ {self.consumo_sms:.2f}\n"
            f"- Internet: R$ {self.consumo_internet:.2f}\n\n"
            f"### Fatura\n"
            f"- Consumo total: R$ {self.consumo_total:.2f}\n"
            f"- Saldo atual: R$ {self.__saldo:.2f}\n"
        )

    def adicionar_saldo(self, saldo):
        self.__saldo += saldo
        return f"Recarga de R$ {saldo:.2f} realizada com sucesso!"

    def mostrar_saldo(self):
        return f"Saldo atual: R$ {self.__saldo:.2f}"

    def __verificar_saldo(self, custo):
        if self.__saldo < custo:
            raise ValueError(
                f"Saldo insuficiente!\nCusto: R$ {custo}\nSaldo atual: R$ {self.__saldo:.2f}"
            )

    def realizar_chamada(self, chip, duracao):
        # Pré-pago: Deduz o custo da chamada do saldo (R$ 0,50/min).
        custo = 0.5 * duracao
        self.__verificar_saldo(custo)
        self.__saldo -= custo
        self.consumo_chamada += custo
        print(
            f"Cliente {chip.cliente.nome} fez uma ligação de {duracao} minuto(s) (custo: R$ {custo:.2f})..."
        )
        print(f"Saldo atual: R$ {self.__saldo:.2f}")

    def enviar_sms(self, chip, quantidade):
        # Deduz o custo dos SMS do saldo (R$ 0,30/SMS).
        custo = 0.3 * quantidade
        self.__verificar_saldo(custo)
        self.__saldo -= custo
        self.consumo_sms += custo
        print(
            f"Cliente {chip.cliente.nome} enviou {quantidade} SMS (custo: R$ {custo:.2f})..."
        )
        print(f"Saldo atual: R$ {self.__saldo:.2f}")

    def consumir_dados_internet(self, chip, gb):
        # Deduz o custo do saldo (R$ 5,00/GB).
        custo = 5 * gb
        self.__verificar_saldo(custo)
        self.__saldo -= custo
        self.consumo_internet += custo
        print(
            f"Cliente {chip.cliente.nome} consumiu {gb}GB de internet (custo: R$ {custo:.2f})..."
        )
        print(f"Saldo atual: R$ {self.__saldo:.2f}")

    def __str__(self):
        return self.consultar_status()
