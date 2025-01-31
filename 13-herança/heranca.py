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
    
    @saldo.setter
    def saldo(self, saldo):            
        self.__saldo = saldo
    
    def __str__(self):
        return f'Conta: {self.__numero}  Saldo: R$ {self.__saldo:.2f}'
    
    def creditar(self, cred):
        #O método creditar(...) adiciona um valor recebido como parâmetro e adiciona ao atributo saldo. 
        self.__saldo+=cred
        return self.__saldo
     
    def debitar(self, deb):
        #O método debitar(...) subtrai do atributo saldo o valor passado como parâmetro, somente se este valor for menor ou igual ao saldo da conta. 
        if deb <= self.__saldo:
            self.__saldo-=deb
            return self.__saldo
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
        self.__taxa_juros = taxa_juros

    @property
    def taxa_juros(self):
        return self.__taxa_juros
        
    def __str__(self):
        return f'{super().__str__()}    Taxa de Juros: {self.__taxa_juros}%'
        
    def renderJuros(self):
    #O método renderJuros() da subclasse ContaPoupança aplica o percentual definido no parâmetro taxa_juros em cima do atributo saldo da classe ContaCorrente, atualizando-o.
        tx = self.taxa_juros/100
        rendimento = self.saldo * tx
        self.saldo += rendimento
        return self.saldo

class ContaImposto (ContaCorrente):
    def __init__(self, numero, saldo, percentual_imposto):
        super().__init__(numero, saldo)
        self.__percentual_imposto = percentual_imposto
        
    @property
    def percentual_imposto(self):
        return self.__percentual_imposto
        
    def __str__(self):
        return f'{super().__str__()}    Imposto: {self.__percentual_imposto}%'

    def calcula_Imposto(self):
        #subtrai do saldo, o valor do próprio saldo multiplicado pelo percentual do imposto.
        tx_imp = self.percentual_imposto/100
        imposto = self.saldo * tx_imp
        self.saldo -= imposto
        return self.saldo
    
def main():
    # conta1 = ContaCorrente(1234, 20000)
    # conta2 = ContaCorrente(123, 10000)
    # print (conta1)
    # print (conta2)
    
    # conta1.transferir(conta2, 200)
    # print (conta1)
    # print (conta2)
    
    # conta1.creditar(100)
    # print (conta1)
       
    # conta3 = ContaPoupanca(1235, 1000, 1.5) 
    # conta3.renderJuros()
    # print (conta3)
    
    conta4 = ContaImposto(1236, 1000, 1.5) 
    conta4.calcula_Imposto()
    print (conta4)
if __name__ == '__main__':
    main()
