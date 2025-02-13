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
        for chip in self.__chips_lista:
            print(f"- Número: {chip.numero} - Tipo: {chip.plano.tipo}-pago")

    def __str__(self):
        nome = self.__nome
        chips = ''
        for chip in self.__chips_lista:
            chips += f"- Número: {chip.numero} - Tipo: {chip.plano.tipo}-pago\n"
        return f"Cliente: {nome}\nChips:\n{chips}"
