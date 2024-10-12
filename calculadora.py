#Crie uma classe que defina uma calculadora básica. Defina os atributos básicos e implemente os comportamentos (métodos).
class Calculadora:
    numero_1 = None
    numero_2 = None
    operacao = None 
    resultado = None

    def calcular (self, numero_1, operacao, numero_2):    
        self.numero_1 = numero_1
        self.numero_2 = numero_2
        self.operacao = operacao
        if operacao == "A":
            self.resultado = numero_1 + numero_2
        elif operacao == "M":
            self.resultado = numero_1 * numero_2
        elif operacao == "D":
            self.resultado = numero_1 / numero_2
        elif operacao == "S":
            self.resultado = numero_1 - numero_2
        else:
            self.resultado = "Operação inválida."

        return self.resultado 
    
def main():
    minha_calculadora = Calculadora()
    minha_calculadora.numero_1 = float(input('Número 1: '))
    minha_calculadora.operacao = input('Operação (A - adição, S - subtração, M - multiplicação, D - divisão): ').strip().upper()
    minha_calculadora.numero_2 = float(input('Número 2: '))
    
    minha_calculadora.calcular(minha_calculadora.numero_1, minha_calculadora.operacao, minha_calculadora.numero_2)
    #minha_calculadora.calcular(float(input('Número 1: ')),float(input('Número 2: ')), input('Operação (S - soma, M - multiplicação, D - divisão): ').strip().upper())

    print (minha_calculadora.resultado)

if __name__ == "__main__":
    main()