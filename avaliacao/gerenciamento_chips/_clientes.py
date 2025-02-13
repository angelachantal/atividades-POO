from ._chips import Chips

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
        if isinstance(chip, Chips):
            if chip.cliente == None:
                print(
                    f"Associando o chip {chip.plano.tipo}-pago (Número: {chip.numero}) ao cliente {self.__nome}..."
                )
                self.__chips_lista.append(chip)
                chip.cliente = self
                print(f'{chip.cliente.nome} associado(a) ao chip!')
            else:
                print(f"O número {chip.numero} não está disponível.")
        else:
            raise TypeError('Insira um chip válido.')
            
    def listar_chips(self):
        if len(self.__chips_lista) == 0:
            print(f'O usuário {self.__nome} não possui chips.\n')
        else:
            for chip in self.__chips_lista:
                print(f"- Número: {chip.numero} - Tipo: {chip.plano.tipo}-pago")

    def __str__(self):
        nome = self.__nome
        chips = ''
        for chip in self.__chips_lista:
            chips += f"- Número: {chip.numero} - Tipo: {chip.plano.tipo}-pago\n"
        return f"Cliente: {nome}\nChips:\n{chips}"
