# Avaliação POO
# Equipe 2: Ângela Chantal; Murilo Monte; Renan Miqueias; Thiário Lima
## from random import randint
# fazer verificações

# PENDÊNCIAS:
# - Criar as exceções que faltam
# - Código do pytest
# - comentar código 
# - datas - ok

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

class Operadoras:
    def __init__(self, nome):
        self.__clientes_lista = []
        self.__nome = nome
    
    @property
    def nome(self):
        return self.__nome

    def adicionar_cliente(self, cliente):
        if cliente in self.__clientes_lista:
            print(f"O cliente {cliente.nome} já está cadastrado!")
        else:
            self.__clientes_lista.append(cliente)
            print(f"Cadastrando cliente {cliente.nome}...")

    def listar_clientes(self):
        print("Clientes:")
        for cliente in self.__clientes_lista:
            print(f"- {cliente.nome}")

    def __str__(self):
        return f'Operadora ativa.'


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
        if chip in self.__chips_lista:
            print(f"O número {chip.numero} não está disponível.")
        else:
            self.__chips_lista.append(chip)
            print(
                f"Associando o chip {chip.plano.tipo}-pago (Número: {chip.numero}) ao cliente {self.__nome}..."
            )

    def listar_chips(self):
        chips = ""
        for chip in self.__chips_lista:
            chips += f"- Número: {chip.numero} - Tipo: {chip.plano.tipo}-pago\n"
        return chips

    def __str__(self):
        nome = self.__nome
        chip = self.listar_chips()
        return f"Cliente: {nome}\nChips:\n{chip}"


class Chips:
    def __init__(self, numero, cliente, plano):
        self.__numero = numero
        self.__plano = plano
        self.__cliente = cliente
        self.__cliente.adicionar_chip(self)

    @property
    def plano(self):
        return self.__plano

    @property
    def numero(self):
        return self.__numero

    @property
    def cliente(self):
        return self.__cliente

    ## Métodos polimórficos
    def realizar_chamada(self, duracao):
        self.__plano.realizar_chamada(self, duracao)

    def enviar_sms(self, quantidade):
        self.__plano.enviar_sms(self, quantidade)

    def consumir_dados_internet(self, gb):
        self.__plano.consumir_dados_internet(self, gb)

    def __str__(self):
        return f'{self.__cliente.nome} ({self.__plano.tipo}-pago, Número: {self.__numero}) → Saldo: R$ {self.__plano.consumo_total}'


class Planos:
    def __init__(self):
        self.__tipo = ''
        self.__consumo_sms = 0
        self.__consumo_chamada = 0
        self.__consumo_internet = 0
        self.__consumo_total = 0

    @property
    def tipo(self):
        return self.__tipo
    
    @property
    def consumo_sms(self):
        return self.__consumo_sms

    @consumo_sms.setter
    def consumo_sms(self, valor):
        self.__consumo_sms = valor

    @property
    def consumo_chamada(self):
        return self.__consumo_chamada

    @consumo_chamada.setter
    def consumo_chamada(self, valor):
        self.__consumo_chamada = valor

    @property
    def consumo_internet(self):
        return self.__consumo_internet

    @consumo_internet.setter
    def consumo_internet(self, valor):
        self.__consumo_internet = valor

    @property
    def consumo_total(self):
        return self.__consumo_total

    @consumo_total.setter
    def consumo_total(self, valor):
        self.__consumo_total = valor

    def calcular_custo(self, meses):
        return 'Cálculo de custo só está disponível em planos pós-pagos!'
    
    def consultar_status(self):
        pass
    
    def realizar_chamada(self):
        pass

    def enviar_sms(self):
        pass

    def consumir_dados_internet(self):
        pass

    def adicionar_saldo(self):
        print('Saldo só está disponível em planos pré-pagos!')

    def mostrar_saldo(self):
        print('Saldo só está disponível em planos pré-pagos!')

    def set_vencimento(self):
        print('Só é possível mudar o vencimento em planos pós-pagos!')

    def __str__(self):
        pass


class PlanosPre(Planos):
    def __init__(self):
        super().__init__()
        self.__tipo = 'pré'
        self.__saldo = 0

    @property
    def tipo(self):
        return self.__tipo

    def consultar_status(self):
        self.consumo_total = (self.consumo_sms + self.consumo_chamada + self.consumo_internet)
        return (
            f"## Custo total\n"
            f"Chamadas: R$ {self.consumo_chamada:.2f}\n"
            f"SMS: R$ {self.consumo_sms:.2f}\n"
            f"Internet: R$ {self.consumo_internet:.2f}\n"
            f"------------------------\n"
            f"Consumo total: R$ {self.consumo_total:.2f}\n"
            f"Saldo atual: R$ {self.mostrar_saldo()}"
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
        print(f"Recarga de R$ {saldo:.2f} realizada com sucesso!")

    def mostrar_saldo(self):
        return f"{self.__saldo:.2f}"

    def __verificar_saldo(self, custo):
        if self.__saldo < custo:
            raise ValueError(f'Saldo insuficiente!\nCusto: R$ {custo}\nSaldo atual: R$ {self.__saldo:.2f}')

    def realizar_chamada(self, chip, duracao):
        # Pré-pago: Deduz o custo da chamada do saldo (R$ 0,50/min).
        custo = 0.5 * duracao
        self.__verificar_saldo(custo)
        self.__saldo -= custo
        self.consumo_chamada += custo
        print(
            f"Cliente {chip.cliente.nome} fez uma ligação de {duracao} minutos (custo: R$ {custo:.2f})..."
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
            f"Cliente {chip.cliente.nome} consumiu  {gb}GB de internet (custo: R$ {custo:.2f})..."
        )
        print(f"Saldo atual: R$ {self.__saldo:.2f}")

    def __str__(self):
        self.consultar_status()


class PlanosPos(Planos):
    def __init__(self):
        super().__init__()
        self.__tipo = 'pós'
        self.__fatura_inicial = 120
        self.__fatura = self.__fatura_inicial
        self.__data_criacao = datetime.today()
        self.__vencimento = self.__data_criacao + relativedelta(months=1)

        print(f'Fatura mensal de R$ {self.__fatura} gerada.')

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
