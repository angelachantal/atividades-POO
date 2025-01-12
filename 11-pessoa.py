class Pessoa:
    seq = 0
    
    def __init__ (self, nome, idade, peso, altura, sexo, estado = "vivo",est_civil = "solteiro", mae = None):
        Pessoa.seq += 1
        self.__id = Pessoa.seq
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura
        self.__sexo = sexo
        self.__estado = estado
        self.__est_civil = est_civil
        self.__conjuge = None
        self.__mae = mae
        self.filhos = []
        self.__pai = None
        self.__mae_adotiva = None
        self__pai_adotivo = None
    
    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def conjuge(self):
        return self.__conjuge
    
    @property
    def est_civil(self):
        return self.__est_civil
    
    @nome.setter
    def nome(self, valor):
        if self.__est_civil == "casado":
            nome_antigo = self.__nome.split(" ")
            nome_conjuge = self.__conjuge.nome.split(" ")
            novo_nome = valor.split(" ")
            for i in novo_nome:
                if (i not in nome_antigo) and (i not in nome_conjuge):
                    print("Nome inválido!")
                    return
            self.__nome = valor
            print("Alteração efetuada com sucesso!")
     
    # Impedir que uma pessoa "casada"  possa se casar novamente. 
    # Exceções: Quando a pessoa se tornar "viúva" ou "divorciada"       
    def casar (self, conjuge):
        if type(conjuge) == Pessoa:
            if self.id != conjuge.id:
                if self.__est_civil != "casado" and conjuge.__est_civil != "casado":
                    self.__est_civil = "casado"
                    self.__conjuge = conjuge
                    conjuge.__est_civil = "casado"
                    conjuge.__conjuge = self
                    print(f'{self.__nome} casou-se com {conjuge.nome}')
                else:
                    print("Uma das pessoas já está casada!")
            else:
                print("Pessoa não pode se casar com ela mesma!")
    
    def morrer(self):
        if self.__estado == "vivo":
            self.__estado = "morto"
            print(f'{self.__nome} faleceu.')
            if self.__est_civil == "casado":
                self.__conjuge.__est_civil = "viúvo"
                self.__conjuge.__conjuge = None
                print(f'{self.__conjuge.nome} agora está viúvo.')
        else:
            print(f'{self.__nome} já está morto.')

    def divorciar(self):
        if self.__est_civil == "casado":
            self.__est_civil = "divorciado"
            self.__conjuge.__est_civil = "divorciado"
            self.__conjuge.__conjuge = None
            self.__conjuge = None
            print(f'Divórcio realizado com sucesso.')
        else:
            print("A pessoa não está casada!")
            
    def ter_filhos (self, parceiro):
        # a) Pessoa ser do sexo: "Feminino"
        if type(parceiro) == Pessoa:
            if self.__estado != "vivo" or parceiro.__estado != "vivo":
                print("Ambos os parceiros devem estar vivos para ter filhos!")
            if self.__id != parceiro.__id:
                # b) Segunda pessoa ser do sexo: "Masculino"
                if self.__sexo == 'F' and parceiro.__sexo == 'M':
                    #Esse método tem que retornar um novo objeto do tipo "Pessoa"
                    filho = Pessoa(nome="Filho de " + self.__nome, idade=0, peso=3.5, altura=0.5, sexo="M", mae=self)
                    # c) acrescentar os atributos: Pai e Mãe (tipo: Pessoa).
                    filho.__pai = parceiro
                    # d) Inserir na lista: filhos, todos os objetos gerados.
                    self.filhos.append(filho)
                    parceiro.filhos.append(filho)
                    print(f'{self.__nome} e {parceiro.nome} tiveram um filho.')
                    return filho
                elif self._sexo == "M" and parceiro._sexo == "F":
                    return parceiro.ter_filhos(self)
                else: 
                    raise ValueError ('É necessário um homem e uma mulher para ter filhos.')
            else:
                raise ValueError ('Uma pessoa não pode engravidar de si mesma.')
        def adotar_filhos(self, criança):
            if criança._mae is None and criança._pai is None:
                criança._mae = self if self._sexo == "F" else None
                criança._pai = self if self._sexo == "M" else None
                self.filhos.append(criança)
                print(f'{self.__nome} adotou {criança.nome}.')
            else:
                print("A criança não é órfã e não pode ser adotada.")
                
    def __str__(self):
        return f'Nome: {self.__nome}. \nIdade: {self.__idade} anos. \nPeso: {self.__peso}. \nAltura: {self.__altura}. \nSexo: {self.__sexo}. \nEstado: {self.__estado}. \nEstado Civil: {self.__est_civil}.' 
           
    
def main():
    maria = Pessoa("Maria", 30, 65, 1.7, 'F')
    
    joao = Pessoa("João", 25, 66, 1.7, 'M')

    #print(maria.id, joao.id)
    #maria.casar(maria)
    maria.casar(joao)
    maria.morrer()
    ana = Pessoa("Ana", 28, 55, 1.65, 'F')
    joao.casar(ana)  # João e Ana -> casado
    pedro = ana.ter_filhos(joao)
    
    #print (f'{maria}\n')
    print (f'\n{joao}')
    print (f'\n{ana}')
    print (f'\n{pedro}')

if __name__ == '__main__':
    main()
