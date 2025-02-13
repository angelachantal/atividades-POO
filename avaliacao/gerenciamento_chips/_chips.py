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
