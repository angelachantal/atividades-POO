# Exercício 10 – Implementação da Classe Ar-Condicionado

class ArCondicionado():
    # Método construtor/inicializador:
    def __init__(self, temp_min, temp_max, vel_min, vel_max, temperatura, velocidade, modo, ligado=False):
        self.tem_min = temp_min
        self.temp_max = temp_max
        self.vel_min = vel_min
        self.vel_max = vel_max
        self.temperatura = temperatura
        self.velocidade = velocidade
        self.modo = modo
        self.ligado = ligado
            # temperatura: <temperatura_escolhida dentro dos limites>
            # velocidade: <velocidade escolhida dentro dos limites>
            # modo: <’automático’/’frio’/’ventilar’>
            # ligado: True/False) -> None:
    
    def __str__(self) -> str:
        pass
    
    # Métodos a serem implementados (CASOS DE USO):
    def ligar():
        pass
        # Fluxo normal: 
            # Sistema liga o aparelho
            # Sistema imprime “Aparelho ligado”
            # Sistema imprime estado atual
        # Extensões: 
            # 1a. Se o aparelho estiver ligado, imprimir “Aparelho já está ligado” e imprimir o estado atual do aparelho
    def desligar():
        pass       
        # Fluxo normal: 
            # Sistema desliga o aparelho
            # Sistema imprime “Aparelho desligado”
            # Sistema imprime estado atual
        # Extensões: 
            # 1a. Se o aparelho estiver desligado, imprimir “Aparelho já está desligado” e imprimir o estado atual do aparelho 
    def aumentar_temperatura():
        pass
        # Fluxo normal: 
            # Sistema pergunta quantos graus deseja aumentar.
            # Usuário informa a quantidade de graus.
            # Sistema incrementa a temperatura na quantidade de graus informada.
            # Sistema incrementa a temperatura em 1°C.
            # Sistema imprime estado atual.
        # Extensões: 
            # 1a. Se a temperatura for maior que 28°C, imprimir “Atingiu temperatura máxima” e imprimir o estado atual do aparelho.
    def diminuir_temperatura():
        pass
    # Fluxo normal: 
# Sistema decrementa a temperatura em 1°C.
# Sistema imprime estado atual.
# Extensões: 
# 1a. Se a temperatura for menor que 18°C, imprimir “Atingiu temperatura mínima” e imprimir o estado atual do aparelho.
    def aumentar_velocidade():
        pass
    # Fluxo normal: 
# Sistema incrementa a velocidade em 1.
# Sistema imprime estado atual.
# Extensões: 
# 1a. Se o modo for automático, imprime: “Não é possível alterar a velocidade” e imprimir o estado atual do aparelho.
# 1b. Se a velocidade for maior que 5, imprimir “Atingiu a velocidade máxima” e imprimir o estado atual do aparelho.
    def diminuir_velocidade():
        pass
    # Fluxo normal: 
# Sistema decrementa a velocidade em 1.
# Sistema imprime estado atual.
# Extensões: 
# 1a 1a. Se o modo for automático, imprime: “Não é possível alterar a velocidade” e imprimir o estado atual do aparelho.
# 1b Se a velocidade for menor que 1, imprimir “Atingiu a velocidade mínima” e imprimir o estado atual do aparelho.
    def mudar_modo(modo):
        pass
    # Fluxo normal: 
# Sistema pergunta qual modo o usuário deseja e apresenta as opções.
# Sistema altera o modo do aparelho
# Sistema imprime estado atual.
# Extensões: 
# 2a. Se o cliente escolher a opção 1, imprime “Frio”.
# 3b. Se o cliente escolher a opção 2, imprime “Ventilar”.
# 3c. Se o cliente escolher a opção 3, imprime “Automático”
# 3d. Se o cliente escolher a opção 4, imprime “Opção inválida”.
def main():
    pass
# Imprimir estado
    # Fluxo normal: 
        # Sistema lê o estado atual do aparelho
        # Sistema imprime o estado atual do aparelho
        # Sistema pergunta o que o usuário deseja fazer e apresenta opções.
    # Extensões: 
        # 3a. Se o cliente escolher a opção 1, encerrar o programa.
        # 3b. Se o cliente escolher a opção 2, ligar o aparelho.
        # 3c. Se o cliente escolher a opção 3, desligar o aparelho
        # 3d. Se o cliente escolher a opção 4, aumentar a temperatura.
        # 3e. Se o cliente escolher a opção 5, diminuir a temperatura
        # 3f. Se o cliente escolher a opção 6, aumentar a velocidade.
        # 3g. Se o cliente escolher a opção 7, diminuir a velocidade.
        # 3h. Se o cliente escolher a opção 8, mudar o modo.

if __name__='__main__':
    main()
