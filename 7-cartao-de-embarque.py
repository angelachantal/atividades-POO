# Utilizando o processo de abstração, implemente uma classe em Python que represente um cartão de embarque de voo. Identifique atributos mutáveis e imutáveis, implemente um construtor da classe e métodos para manipulação dos atributos mutáveis. Faça todas as validações possíveis. Crie objetos para testar os métodos implementados.
from datetime import date

class CartaoEmbarque:
    def __init__(self, nome, voo, localizador, data_emb, hora_emb, status = 'Check-in não realizado', assento = 'Aleatório') -> None:
        pass
    
    def check_in (self):
        # altera o status e associa um assento (aleatório) disponível ao passageiro.
        pass
    def escolher_assento (self):
        # alterar o assento (apenas se o check-in já tiver sido realizado).
        pass
    def validacao (self):
        # Validações para garantir que assentos indisponíveis não sejam atribuídos e que o check-in só possa ser feito uma vez.
        # Requisitos de validação: o código da reserva deve ter 6 caracteres alfanuméricos; a hora do embarque não pode ser retroativa em relação ao momento de execução do código.
        pass
    def __str__(self) -> str:
        pass
    
def main():
    passageiro1 = CartaoEmbarque()
    passageiro2 = CartaoEmbarque()
    passageiro3 = CartaoEmbarque()
    pass

if __name__=='__main__':
    main()
    
