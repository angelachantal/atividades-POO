# Implementar uma classe Veiculo que represente o registro de um veículo em um sistema de controle de veículos. A atividade deve explorar a criação de construtores, atributos obrigatórios e opcionais, e o uso de métodos para exibir e atualizar as informações do veículo.
# Atributos obrigatórios: chassi (string); marca (string): marca do veículo; modelo (string): modelo do veículo; ano (int): ano de fabricação do veículo.
# Atributos opcionais: placa (string): placa do veículo; cor (string): cor do veículo (padrão: "Não especificada"); proprietario (string): nome do proprietário do veículo (padrão: "Não especificado"); quilometragem (int): quilometragem atual do veículo (padrão: 0).
# Método __init__: define os atributos obrigatórios e permite incluir os opcionais com valores padrão.
# Método __str__: imprime todas as informações do veículo, incluindo os atributos opcionais.

class Veiculo:
    def __init__(self, chassi, marca, modelo, ano):
        #Atributos obrigatórios
        self.chassi = chassi
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        #Atributos opcionais
        self.placa 
        self.cor = "Não especificada"
        self.proprietario = "Não especificado"
        self.quilometragem = 0
        pass
    def avancar_km (self, quilometragem):
        self.quilometragem = 0
    def __str__(self):
        pass
    
def main():
    veiculo1 = Veiculo('jbf457j964078q', 'Chevrolet', 'Classic', 2011)
    veiculo1.avancar_km()

if __name__ == '__main__':
    main()
