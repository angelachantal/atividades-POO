# Exercício 10 – Implementação da Classe Ar-Condicionado

class ArCondicionado:
    # Método inicializador:
    def __init__(self, modo='Automático', ligado=False):
        self.temperatura= 20
        self.velocidade = 3
        self.modo = modo
        self.ligado = ligado
    
    def __str__(self) -> str:
        if self.ligado == True:
            return f'APARELHO LIGADO\nModo: {self.modo}\nTemperatura: {self.temperatura}°C\nVelocidade: {self.velocidade}\n'
        else:
            return f'APARELHO DESLIGADO\n'
       
    def operacao (self):
        op_operacao = int(input(f'Informe a operação desejada:\n   1 - Sair\n   2 - Ligar o aparelho\n   3 - Desligar o aparelho\n   4 - Aumentar a temperatura\n   5 - Diminuir a temperatura\n   6 - Aumentar a velocidade\n   7 - Diminuir a velocidade\n   8 - Mudar o modo\n'))
        # Sistema executa a operação desejada.
        if op_operacao == 1:
            print (self)
        elif op_operacao == 2:
            self.ligar()
        elif op_operacao == 3:
            self.desligar()
        elif op_operacao == 4:
            self.aumentar_temperatura()
        elif op_operacao == 5:
            self.diminuir_temperatura()
        elif op_operacao == 6:
            self.aumentar_velocidade()
        elif op_operacao == 7:
            self.diminuir_velocidade()
        elif op_operacao == 8:
            self.mudar_modo()
        else:
            raise ValueError ('Opção inválida.')
    
    def ligar(self):
        #Se o aparelho estiver ligado, imprimir “Aparelho já está ligado” e imprimir o estado atual do aparelho
        if self.ligado == True:
            print ('Aparelho já está ligado\n')
        else: 
            self.ligado = True
        # Sistema imprime estado atual
        print(self)
        return self.operacao()   
        
    def desligar(self):
        #Se o aparelho estiver desligado, imprimir “Aparelho já está desligado” e imprimir o estado atual do aparelho
        if self.ligado == True:
            self.ligado = False
        else: 
            print ('Aparelho já está desligado.\n')
        # Sistema imprime estado atual
        print(self)
        return self.operacao() 
    
    def aumentar_temperatura(self):
        # Sistema pergunta quantos graus deseja aumentar.
        temp = int(input ('Em quantos graus deseja aumentar a temperatura?\n'))
        # Sistema incrementa a temperatura na quantidade de graus informada.
        self.temperatura += temp
        # Se a temperatura for maior que 28°C, imprimir “Atingiu temperatura máxima” e imprimir o estado atual do aparelho.
        if self.temperatura > 28:
            print ('O aparelho atingiu a temperatura máxima (28°C).\n')
            self.temperatura = 28
            print (self)
        # Sistema imprime estado atual.
        else: print (self)
        return self.operacao()
    
    def diminuir_temperatura(self):
        temp = int(input ('Em quantos graus deseja diminuir a temperatura?\n'))
        self.temperatura -= temp
        if self.temperatura < 18:
            print ('O aparelho atingiu a temperatura mínima (18°C).\n')
            self.temperatura = 18
            print (self)
        # Sistema imprime estado atual.
        else: print (self)
        return self.operacao()
    
    def aumentar_velocidade(self):
        # Sistema incrementa a velocidade em 1.
        self.velocidade += 1
        # Se a velocidade for maior que 5, imprimir “Atingiu velocidade máxima” e imprimir o estado atual do aparelho.
        if self.velocidade > 5:
            print ('O aparelho atingiu a velocidade máxima (5).\n')
            self.velocidade = 5
            print (self)
        # Sistema imprime estado atual.
        else: print (self)
        return self.operacao()
    
    def diminuir_velocidade(self):
        # Sistema decrementa a velocidade em 1.
        self.velocidade -= 1
        # Se a velocidade for menor que 1, imprimir “Atingiu velocidade mínima e imprimir o estado atual do aparelho.
        if self.velocidade <1:
            print ('O aparelho atingiu a velocidade máxima (5).\n')
            self.velocidade = 1
            print (self)
        # Sistema imprime estado atual.
        else: print (self)
        return self.operacao()
    
    def mudar_modo(self):
        op_modo = int(input(f'Informa a opção desejada:\n   1 - Frio\n   2 - Ventilar\n   3 - Automático\n'))
        if op_modo == 1:
            self.modo = 'Frio'
        elif op_modo == 2:
            self.modo = 'Ventilar'
        elif op_modo == 3:
            self.modo = 'Automático'
        else:
            raise ValueError ('Opção Inválida\n')
        print (self)
        self.operacao()
        
def main():
    aparelho = ArCondicionado()
    # Imprimir estado do aparelho
    print (aparelho)
    
    # Sistema pergunta o que o usuário deseja fazer e apresenta opções.
    aparelho.operacao()
    
if __name__=='__main__':
    main()
