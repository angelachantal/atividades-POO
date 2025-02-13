from datetime import datetime
from dateutil.relativedelta import relativedelta
from ._planos import Planos

class PlanosPos(Planos):
    def __init__(self, numero):
        super().__init__()
        self.__tipo = 'pós'
        self.__numero = numero
        self.__fatura_inicial = 120
        self.__fatura = self.__fatura_inicial
        self.__data_criacao = datetime.today()
        self.__vencimento = self.__data_criacao + relativedelta(months=1)

        print(f'## Chip criado!\nNúmero: {self.__numero}\nTipo: {self.__tipo}\nFatura mensal de R$ {self.__fatura} gerada.\n')

    @property
    def tipo(self):
        return self.__tipo
    
    def set_vencimento(self, vencimento):
        try:
            vencimento_valido = datetime.strptime(vencimento, "%d/%m/%Y")
            self.__vencimento = vencimento_valido
            print(f'Vencimento da fatura alterada para: {self.__vencimento}\n')
        except ValueError:
            raise ValueError("Data e hora inválidas!")

    def __verificar_vencimento(self):
        if datetime.today() < self.__vencimento:
            return True
        else:
            raise ValueError(f"Fatura vencida!\nData do vencimento: {self.__vencimento}")
        
    def calcular_custo(self, meses=1):
        calculo = meses * self.__fatura_inicial
        print(
            f'## Cálculo de custo em meses\n'
            f'- Fatura: R$ {self.__fatura_inicial:.2f}\n'
            f'- Valor da fatura durante {meses} meses: R$ {calculo}\n'
        )

    def consultar_status(self):
        self.__consumo_total = (self.consumo_sms + self.consumo_chamada + self.consumo_internet)
        valor_final = self.__consumo_total + self.__fatura

        print (
            f"## Custo total\n"
            f"### Consumo\n"
            f"- Chamadas: R$ {self.consumo_chamada:.2f}\n"
            f"- SMS: R$ {self.consumo_sms:.2f}\n"
            f"- Internet: R$ {self.consumo_internet:.2f}\n\n"
            f"### Fatura\n"
            f'- Fatura: R$ {self.__fatura:.2f}\n'
            f'- Consumo além da fatura: R$ {self.__consumo_total:.2f}\n'
            f"------------------------\n"
            f'- Total a pagar: R$ {valor_final:.2f}\n'
            f'- Vencimento: {self.__vencimento}\n'
        )
        
    def realizar_chamada(self, chip, duracao):
        self.__verificar_vencimento()

        custo = 0.30 * duracao
        self.__fatura += custo
        self.consumo_chamada = custo
        print(
            f"Cliente {chip.cliente.nome} fez uma ligação de {duracao} minutos (custo: R$ {custo:.2f})..."
        )
        print(f"Fatura atual: R$ {self.__fatura:.2f}\n")

    def enviar_sms(self, chip, quantidade):
        self.__verificar_vencimento()

        custo = 0.20 * quantidade
        self.__fatura += custo
        self.consumo_sms = custo
        print(
            f"Cliente {chip.cliente.nome} enviou {quantidade} SMS (custo: R$ {custo:.2f})..."
        )
        print(f"Fatura atual: R$ {self.__fatura:.2f}\n")

    def consumir_dados_internet(self, chip, gb):
        self.__verificar_vencimento()

        custo = 2 * gb
        self.__fatura += custo
        self.consumo_internet = custo
        print(
            f"Cliente {chip.cliente.nome} consumiu  {gb}GB de internet (custo: R$ {custo:.2f})..."
        )
        print(f"Fatura atual: R$ {self.__fatura:.2f}\n")

    def __str__(self):
        self.consultar_status()
