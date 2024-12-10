# Implementar a classe Bicicleta, colocando limites máximos e mínimos para os estados: veloc_atual, altura_cela e calibragem_pneus através de seus respectivos métodos. Alterar os métodos: regular_cela, calibrar_pneus para permitirem as mudanças caso a bicicleta esteja parada (veloc_atual=0).

class Bicicleta:
    def __init__(self, veloc_atual, altura_cela, calibragem_pneus):
        self.veloc_atual = veloc_atual
        self.altura_cela = altura_cela
        self.calibragem_pneus = calibragem_pneus
    
    def regular_cela(self):
        while True:
            if self.veloc_atual == 0:
                nova_altura = int(input('Qual a nova altura da cela?'))
                self.altura_cela = nova_altura
                print (f'Altura da Cela: {self.altura_cela}')
                break
            elif self.veloc_atual < 0:
                print (f'Valor inválido. Tente novamente.')
                break
            else:
                print (f'A cela não pode ser regulada com a bicicleta em movimento.')
                break
                
    def calibrar_pneus(self):
        self.calibragem_pneus+=10
        return f'Calibragem dos pneus: {self.calibragem_pneus}'

def main():
    bike_1 = Bicicleta(0,0,0)
    print(bike_1.regular_cela())
    print(bike_1.calibrar_pneus())

if __name__=='__main__':
    main()
