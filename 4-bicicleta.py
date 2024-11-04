# Implementar a classe Bicicleta, colocando limites máximos e mínimos para os estados: veloc_atual, altura_cela e calibragem_pneus através de seus respectivos métodos. Alterar os métodos: regular_cela, calibrar_pneus para permitirem as mudanças caso a bicicleta esteja parada (veloc_atual=0).

class Bicicleta:
    veloc_atual = None
    altura_cela = None
    calibragem_pneus = None
    
    def __init__(self, veloc_atual, altura_cela, calibragem_pneus):
        self.veloc_atual = float(veloc_atual)
        self.altura_cela = float(altura_cela)
        calibragem_pneus = float(calibragem_pneus)

    def regular_cela(self):
        pass

    def calibrar_pneus(self): 
        pass

def main():
    pass

if __name__=='__main__':
    main()