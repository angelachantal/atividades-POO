# Avaliação POO
# Equipe 2: Ângela Chantal; Murilo Monte; Renan Miqueias; Thiário Lima

class Operadoras:
    def __init__(self):
        pass
    
    def __str__(self):
        pass
    
class Clientes:
    def __init__(self):
        pass
    
    def __str__(self):
        pass

class Chips:
        def __init__(self):
        pass
    
    def __str__(self):
        pass
    
class Planos:
    def __init__(self):
        pass
    
    def __str__(self):
        pass

class PlanosPre(Planos):
    def __init__(self):
        super().__init__()
        pass

    def __str__(self):
        return super().__str__() + f'.'

class PlanosPre(Planos):
    def __init__(self):
        super().__init__()
        pass

    def __str__(self):
        return super().__str__() + f'.'


class Consumo:
    #verificar nome da classe
    def __init__(self):
        pass

    # Confirmar se este é o metodo polimórfico solicitado na questão
    def calcular_custo(self, mes):
        pass

    #     self._totalCusto += veiculo.calcula_custo(distancia, preco_combustivel)
    #     return self._totalCusto

