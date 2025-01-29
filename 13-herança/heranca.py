
     
class ContaCorrente:
    def __init__(self, numero, saldo):
        pass

    def __str__(self):
        pass

    def creditar():
        #O método creditar(...) adiciona um valor recebido como parâmetro e adiciona ao atributo saldo. 
        pass

    def debitar():
        #O método debitar(...) subtrai do atributo saldo o valor passado como parâmetro, omente se este valor for menor ou igual ao saldo da conta. 
        pass 

    def transferir():
        #O método transferir(...) transfere um valor da conta de origem para outra conta (verificar se a conta de origem tem saldo suficiente. Passar como parâmetros o valor e um objeto conta que é a conta destino).
        pass 

    def saldo():
        #O método saldo() na verdade é um decorador getter. 
        pass 

class ContaPoupanca(ContaCorrente):
    def __init__(self, numero, saldo, taxa_juros):
        super().__init__(numero, saldo)
        pass

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