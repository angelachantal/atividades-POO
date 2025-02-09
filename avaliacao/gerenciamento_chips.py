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
        print(f'Cadastrando cliente {cliente.nome}')
        # Cadastrando cliente João...

    def listar_clientes(self):
        print('Clientes')
        for cliente in self.__clientes_lista:
            print(f'- {cliente.nome}')
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

    def adicionar_chip(self, tipo, numero): 
        chip = Chips(tipo, numero)
        self.__chips_lista.append(chip)
        print(f'Associando o chip {tipo}-pago (Número: {chip.numero}) ao cliente {self.__nome}')
        # Associando chip pré-pago (Número: 11987654321) ao cliente João...

    def listar_chips(self):
        chips = ''
        for chip in self.__chips_lista:
            chips += f'- Número: {chip.numero} - Tipo: {chip.tipo}\n'
        return chips

    def __str__(self):
        nome = self.__nome
        chip = self.listar_chips()
        return f'Cliente: {nome}\nChips:\n{chip}'

class Chips:
    def __init__(self, tipo, numero):
        self.__tipo = tipo
        self.__numero = numero
       
    @property
    def tipo(self):
        return self.__tipo
    
    @property
    def numero(self):
        return self.__numero

    def realizar_chamada(self, duracao): ...
    def enviar_sms(self, quantidade): ...
    def consumir_dados_internet(self, gb): ...

    def __str__(self):
        # João (Pré-pago, Número: 11987654321) → Saldo: R$ 33,50
        pass

class Planos:
    def calcular_custo(self):
        pass

    def __init__(self):
        pass

    def __str__(self):
        pass

class PlanosPre(Planos, Chips):
    def __init__(self):
        super().__init__()
        pass

    def calcular_custo(self): ...
    def realizar_chamada(self, duracao): ...
    def enviar_sms(self, quantidade): ...
    def consumir_dados_internet(self, gb): ...

    def __str__(self):
        return super(Planos).__str__() + f"."

class PlanosPre(Planos, Chips):
    def __init__(self):
        super().__init__()
        pass

    def calcular_custo(self): ...
    def realizar_chamada(self, duracao): ...
    def enviar_sms(self, quantidade): ...
    def consumir_dados_internet(self, gb): ...

    def __str__(self):
        return super().__str__() + f"."
