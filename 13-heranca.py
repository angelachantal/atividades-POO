#1. Implemente a hierarquia de classes descrita no diagrama acima.
#a) Defina os construtores das classes (__init__) e a saída de dados (__str__) nas classes indicadas.
#b) Implemente os métodos creditar(...), debitar(...), transferir(...) e saldo() da classe ContaCorrente. O método creditar(...) adiciona um valor recebido como parâmetro e adiciona ao atributo saldo. O método debitar(...) subtrai do atributo saldo o valor passado como parâmetro, somente se este valor for menor ou igual ao saldo da conta. O método saldo() na verdade é um decorador getter. O método transferir(...) transfere um valor da conta de origem para outra conta (verificar se a conta de origem tem saldo suficiente. Passar como parâmetros o valor e um objeto conta que é a conta destino).
#c) O método renderJuros(...) da subclasse ContaPoupança aplica o percentual definido no parâmetro taxa_juros em cima do atributo saldo da classe ContaCorrente, atualizando-o.
#d) Crie uma classe ContaImposto que herda de ContaCorrente e possui um atributo percentual_Imposto. Esta classe também possui um método calcula_Imposto() que subtrai do saldo, o valor do próprio saldomultiplicado pelo percentual do imposto.
     
class ContaCorrente:
    def __init__(self):
        pass

    def __str__(self):
        pass

class ContaPoupanca(ContaCorrente):
    def __init__(self):
        super().__init__()
        pass