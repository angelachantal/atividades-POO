# Utilizando o processo de abstração, implemente uma classe em python que represente uma carteira de habilitação. Identifique atributos mutáveis e imutáveis, implemente um construtor da classe e métodos para manipulação dos atributos mutáveis. Faça todas as validações possíveis. Crie objetos para testar os métodos implementados.

from datetime import date

class CNH:
    def __init__(self, nome, cpf, d_nasc, mae, categoria, n_registro, d_habilitacao, d_emissao, d_validade, local, pai = '', observacao = 'Sem Observação.'):
        self.nome = nome
        self.cpf = cpf
        self.d_nasc = d_nasc
        self.mae = mae
        self.categoria = self.definir_categoria(categoria)
        self.n_registro=n_registro
        self.d_habilitacao = d_habilitacao
        self.d_emissao = d_emissao
        self.d_validade = d_validade
        self.local = local
        self.pai = pai
        self.observacao = observacao
    
    def __str__(self):
            pass

    
    def dados_pessoais(self, nome, cpf, d_nasc, mae, pai):
         self.nome = input('Nome: ').upper()
         self.cpf = input('CPF (***.***.***-**): ')

    def definir_categoria (self, categoria):
        if categoria in ['A','B','C','D','E','AB','AC','AD','AE']:
            return categoria
        else:
            raise ValueError('Categoria inválida.')
         

def main():
    pass

if __name__ == '__main__':
    main()
