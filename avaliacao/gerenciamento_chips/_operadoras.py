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
        return f'Operadora {self.__nome} ativa.'
