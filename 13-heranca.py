class Pessoa:
    seq = 0

    def _init_(self, nome, idade, peso, altura, sexo, mãe=None, estado="vivo", est_civil="solteiro", conjuge=None):
        Pessoa.seq += 1
        self.__id = Pessoa.seq
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura
        self.__sexo = sexo
        self.__estado = estado
        self.__est_civil = est_civil
        self.__mãe = mãe
        self.__pai = None
        self.__conjuge = conjuge
        self.filhos = []

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

    def casar(self, conjuge):
        if type(conjuge) == Pessoa:
            if self.id != conjuge.id:
                if self._est_civil != "casado" and conjuge._est_civil != "casado":
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
                self._conjuge._est_civil = "viúvo"
                self._conjuge._conjuge = None
                print(f'{self.__conjuge.nome} agora está viúvo.')
        else:
            print(f'{self.__nome} já está morto.')

    def divorciar(self):
        if self.__est_civil == "casado":
            self.__est_civil = "divorciado"
            self._conjuge._est_civil = "divorciado"
            self._conjuge._conjuge = None
            self.__conjuge = None
            print(f'Divórcio realizado com sucesso.')
        else:
            print("A pessoa não está casada!")

    def ter_filhos(self, parceiro):
        if self._estado != "vivo" or parceiro._estado != "vivo":
            print("Ambos os parceiros devem estar vivos para ter filhos!")
            return
        if self._sexo == "F" and parceiro._sexo == "M":
            filho = Pessoa(nome="Filho de " + self.__nome, idade=0, peso=3.5, altura=0.5, sexo="M", mãe=self)
            filho.__pai = parceiro
            self.filhos.append(filho)
            parceiro.filhos.append(filho)
            print(f'{self.__nome} e {parceiro.nome} tiveram um filho chamado {filho.nome}.')
            return filho
        elif self._sexo == "M" and parceiro._sexo == "F":
            return parceiro.ter_filhos(self)
        else:
            print("É necessário um homem e uma mulher para ter filhos!")

    def adotar_filhos(self, criança):
        if criança._mãe is None and criança._pai is None:
            criança._mãe = self if self._sexo == "F" else None
            criança._pai = self if self._sexo == "M" else None
            self.filhos.append(criança)
            print(f'{self.__nome} adotou {criança.nome}.')
        else:
            print("A criança não é órfã e não pode ser adotada.")

    def _str_(self):
        return f'{self._nome}, {self.idade} anos, {self.est_civil}, {self._estado}'

# Exemplos de execução
maria = Pessoa("Maria", 30, 65, 1.7, 'F', Pessoa("Francisca", 65, 60, 1.6, 'F'))
joao = Pessoa("João", 25, 66, 1.7, 'M')

print(maria.id, joao.id)
maria.casar(maria)
maria.casar(joao)  # João e Maria -> casado
maria.morrer()  # Maria -> morto, João -> viúvo
ana = Pessoa("Ana", 28, 55, 1.65, 'F')
joao.casar(ana)  # João e Ana -> casado
pedro = ana.ter_filhos(joao)  # João e Ana têm um filho