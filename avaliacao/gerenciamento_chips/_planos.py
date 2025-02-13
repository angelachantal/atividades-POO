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
        pass
    
    def consultar_status(self):
        pass
    
    def realizar_chamada(self):
        pass

    def enviar_sms(self):
        pass

    def consumir_dados_internet(self):
        pass

    def __str__(self):
        pass
