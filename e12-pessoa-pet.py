# Implementar os 3 métodos na classe agregadora:
# - Cadastrar
# - Excluir
# - Mostrar

class Pet:
    def __init__(self,tipo,nome,idade,peso,raca,cor,castrado=False):
        self.__tipo = tipo
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__raca = raca
        self.__cor = cor
        self.__castrado = castrado


class Pessoa:
    def __init__(self,cpf,nome,endereço):
        self.__cpf = cpf
        self.__nome = nome
        self.__endereço = endereço
        self.__meus_pets = []

    @property
    def cpf(self):
      return self.__cpf

    @property
    def nome(self):
      return self.__nome

    def cadastrar_pet(self,pet):
     pass

    def excluir_pet(self,nome):
      pass

    def mostrar_meus_pets(self):
      pass

    def adotar_pet(self, pet):
      pass

def main():
  # Definir um código principal com a criação de pelo menos 3 objetos (Pessoas). 
    pessoa1 = Pessoa(12345678912,"Rogério", "IFPI")
    pessoa2 = Pessoa(98745632123, "Ângela", "Teresina")
    pessoa3 = Pessoa(36985214789, "Andressa", "Teresina")

    pet1 = Pet(gato,Mimi,1,3,"rafeiro",preto)
    pet2 = Pet(cachorro,Chico,9,6.3,"shih-tsu",Marrom,True)
    pet3 = Pet(cachorro,Bic,12,4.2,raca,Preto)

  # Fazer a adoção de pets "de rua" e de pets "de abrigos". 
    pessoa1.adotar_pet(pet1)
    pessoa2.adotar_pet(pet2)

  # Simular a perda de um deles e a consequente atualização (remoção) da lista de pets
 

if __name__ =='__main__':
    main()
