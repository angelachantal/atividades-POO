# Modelar uma classe Relógio_Digital_Simples com seus estados e comportamentos - criar a respectiva classe e, depois, 2 objetos. Imprimir os valores de seus atributos e executar os métodos criados. Recomendação: criar estados que possam ter seus valores alterados por seus métodos.

class Relogio_Digital_Simples:
    hora = 0
    minuto = 0
        
    def __init__(self, hora, minuto):       
        self.hora = int(hora)
        self.minuto = int(minuto)
    
    def hora_atual(self):
        return f'Hora atual: {self.hora:02}:{self.minuto:02}'
    
    def hora_atualizada(self, minutos_passados):
        self.minuto+=minutos_passados
        if self.minuto == 60:
            self.minuto = 00
            self.hora += 1
        elif self.minuto > 60:
            self.minuto -= 60
            self.hora += 1
        return f' Hora atualizada: {self.hora:02}:{self.minuto:02}'
    
def main():
    hora = input('Hora atual: ')
    minuto = input ('Minuto atual: ')
    
    relogio = Relogio_Digital_Simples(hora, minuto)
    print (f'{relogio.hora_atual()}')
    
    while True:
        atualizar = input('Deseja atualizar o horário? (S/N) ').upper()
        if atualizar == 'S':
            minutos_passados = int(input('Quanto tempo passou, em minutos? '))
            print (relogio.hora_atualizada(minutos_passados))
        elif atualizar == 'N':
            print ('O horário não foi atualizado. \nPrograma encerrado.')
            break
        else:
            print ('Resposta inválida. Tente novamente')    

if __name__ == '__main__':
    main()