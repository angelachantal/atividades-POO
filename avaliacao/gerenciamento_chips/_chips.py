class Chips:
    def __init__(self, numero, plano):
        self.__numero = numero
        self.__plano = plano
        self.__cliente = None

    @property
    def plano(self):
        return self.__plano

    @property
    def numero(self):
        return self.__numero

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    ## Métodos polimórficos
    def realizar_chamada(self, duracao):
        if self.__cliente != None:
            self.__plano.realizar_chamada(self, duracao)
        else:
            return "Não há um cliente cadastrado nesse chip.\n"

    def enviar_sms(self, quantidade):
        if self.__cliente != None:
            self.__plano.enviar_sms(self, quantidade)
        else:
            return "Não há um cliente cadastrado nesse chip.\n"

    def consumir_dados_internet(self, gb):
        if self.__cliente != None:
            self.__plano.consumir_dados_internet(self, gb)
        else:
            return "Não há um cliente cadastrado nesse chip.\n"

    def __str__(self):
        if self.__cliente != None:
            return f"Cliente: {self.__cliente.nome} (Plano {self.__plano.tipo}-pago, Número: {self.__numero}) → Saldo: R$ {self.__plano.consumo_total}"
        else:
            return f"Chip sem cliente (Plano {self.__plano.tipo}-pago, Número: {self.__numero}) → Saldo: R$ {self.__plano.consumo_total}"
