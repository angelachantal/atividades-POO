class ContaCorrente:
    def __init__(self, numero, saldo):
        self.__numero = numero
        self.__saldo = float(saldo)

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def numero(self):
        return self.__numero
    
    def __str__(self):
        return f'Conta: {self.__numero}  Saldo: R$ {self.__saldo:.2f}'
    
    def creditar(self, cred):
        #O método creditar(...) adiciona um valor recebido como parâmetro e adiciona ao atributo saldo. 
        self.__saldo+=cred
     
    def debitar(self, deb):
        #O método debitar(...) subtrai do atributo saldo o valor passado como parâmetro, somente se este valor for menor ou igual ao saldo da conta. 
        if deb <= self.__saldo:
            self.__saldo-=deb
        else:
            print ('Saldo insuficiente')           

    def transferir(self, conta_destino, valor):
        #O método transferir(...) transfere um valor da conta de origem para outra conta.
        if type(conta_destino) == ContaCorrente:
            conta_destino.creditar(valor)
            self.debitar(valor) 

class ContaPoupanca(ContaCorrente):
    def __init__(self, numero, saldo, taxa_juros):
        super().__init__(numero, saldo)
        self.

    def __str__(self):
        return super().__str__()

    def renderJuros():
    #O método renderJuros(...) da subclasse ContaPoupança aplica o percentual definido no parâmetro taxa_juros em cima do atributo saldo da classe ContaCorrente, atualizando-o.
        pass

class ContaImposto (ContaCorrente):
    def __init__(self, numero, saldo, percentual_imposto):
        super().__init__(numero, saldo)
        pass

    def __str__(self):
        return super().__str__()

    def calcula_Imposto():
        #subtrai do saldo, o valor do próprio saldomultiplicado pelo percentual do imposto.
        pass
    
def main():
    conta1 = ContaCorrente(1234, 20000)
    print (conta1)
    conta2 = ContaCorrente(123, 10000)
    print (conta2)
    
    conta1.transferir(conta2, 200)
    print (conta1)
    print (conta2)
        
if __name__ == '__main__':
    main()
