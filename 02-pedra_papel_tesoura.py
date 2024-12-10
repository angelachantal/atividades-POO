import random

class Jogo:
    escoha_do_usuario = None
    escolha_do_computador = None
    reultado = None

    def obter_escolha_usuario (self):
        escolha = input("Escolha Pedra, Papel ou Tesoura (ou 'sair' para encerrar): ").strip().lower()
        if escolha in ['pedra', 'papel', 'tesoura']:
            self.escolha_do_usuario = escolha
            return self.escoha_do_usuario
        elif escolha == 'sair':
            self.escolha_do_usuario = None
            return self.escolha_do_usuario
        else:
            print("Escolha inválida. Tente novamente.")
            return self.obter_escolha_usuario()

    def obter_escolha_computador (self):
        self.escolha_do_computador = random.choice(['pedra', 'papel', 'tesoura'])
        return self.escolha_do_computador

    def vencedor (self):
        if self.escoha_do_usuario == self.escolha_do_computador:
            return "Empate!"
        elif (self.escoha_do_usuario == 'pedra' and self.escolha_do_computador == 'tesoura') or \
            (self.escoha_do_usuario == 'papel' and self.escolha_do_computador == 'pedra') or \
                (self.escoha_do_usuario == 'tesoura' and self.escolha_do_computador == 'papel'):
            return "Você venceu!"
        else:
            return "O computador venceu!"

def main ():
    meu_jogo = Jogo()

    while True:
        usuario = meu_jogo.obter_escolha_usuario()
        
        if usuario == None:
            print("Encerrando o jogo...")
            break
        print (meu_jogo.obter_escolha_computador())

        print(meu_jogo.vencedor())

if __name__=='__main__':
    main()
