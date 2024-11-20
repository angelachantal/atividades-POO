# Utilizando o processo de abstração, implemente uma classe em Python que represente um cartão de embarque de voo. Identifique atributos mutáveis e imutáveis, implemente um construtor da classe e métodos para manipulação dos atributos mutáveis. Faça todas as validações possíveis. Crie objetos para testar os métodos implementados.
from datetime import datetime

class CartaoEmbarque:
    # Método construtor/inicializador:
    def __init__(self, nome, voo, localizador, data_emb, hora_emb, status = 'Check-in não realizado', assento = 'Aleatório'):
        self.nome = nome
        self.voo = voo
        self.localizador = localizador
        self.data_emb = data_emb
        self.hora_emb = hora_emb
        self.status = status
        self.assento = assento
    
    def realizar_check_in (self, status, assento):
        # altera o status e associa um assento (aleatório) disponível ao passageiro.
        # Validações para garantir que o check-in só possa ser feito uma vez.
        pass
    def escolher_assento (self, assento):
        # alterar o assento (apenas se o check-in já tiver sido realizado).
        # Validações para garantir que assentos indisponíveis não sejam atribuídos.
        pass
    def validar_reserva (self, reserva):
        # o código da reserva deve ter 6 caracteres alfanuméricos
        pass
    def validar_hora (self, hora):
        # a hora do embarque não pode ser retroativa em relação ao momento de execução do código.
        pass
    def __str__(self) -> str:
        return (f'Passageiro: {self.nome}\n'
                f'Vôo: {self.voo}\n'
                f'Localizador: {self.localizador}\n' 
                f'Data de Embarque: {self.data_emb}\n'
                f'Hora de Embarque: {self.hora_emb}\n'
                f'Status: {self.status}\n'
                f'Assento: {self.assento}\n'
                )
    
def main():
    passageiro1 = CartaoEmbarque('Ângela Nunes', '235', 'IHHH3M', '24/11/2024', '08:56')
    passageiro2 = CartaoEmbarque('Roberto Lemos', '235', 'OMNH5I', '24/11/2024', '08:56')
    passageiro3 = CartaoEmbarque('Denise Pereira', '235', 'AOMF9O', '24/11/2024', '08:56')
    print(passageiro1)
    print(passageiro2)
    print(passageiro3)
    
if __name__=='__main__':
    main()
