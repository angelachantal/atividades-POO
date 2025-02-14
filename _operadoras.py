from ._clientes import Clientes

#teste ok

class Operadoras:       
    def __init__(self, nome):
        self.__clientes_lista = []
        self.__nome = nome
    
    @property
    def nome(self):
        return self.__nome

    def adicionar_cliente(self, cliente):
        if isinstance(cliente, Clientes):
            if cliente in self.__clientes_lista:
                print(f"O cliente {cliente.nome} já está cadastrado!\n")
            else:
                self.__clientes_lista.append(cliente)
                print(f"Cadastrando cliente {cliente.nome}...\n")
        else:
            raise TypeError(f'Só é possível adicionar clientes válidos.')

    def listar_clientes(self):
        if len(self.__clientes_lista) == 0:
            print('Não há clientes.\n')
        else:
            print("Clientes:")
            for cliente in self.__clientes_lista:
                print(f"- {cliente.nome}")

    def __str__(self):
        return f'Operadora {self.__nome} ativa.\n'
