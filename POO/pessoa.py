class Pessoa:
    def __init__(self, nome:str, idade:int):
        self.setNome(nome)
        self.setIdade(idade)
        #self.__nome = nome
        #self.__idade = idade

    def getNome(self) -> str:
        return self.__nome

    def setNome(self, nome:str) -> None:
        self.__nome = nome

    def getIdade(self) -> int:
        return self.__idade

    def setIdade(self, idade:int) -> None:
        if idade < 0:
            self.__idade = 0
        else:
            self.__idade = idade

p1 = Pessoa("Fulano", 10)
print(p1.getNome(), p1.getIdade())
p1 = Pessoa("Ciclano", 0)
print(p1.getNome(), p1.getIdade())


'''
EXISTEM PADRÕES A SEREM SEGUIDOS, como uma nova 
definição de getter e setter do qual se aplicam
conceitos de encapsulamento com uma diferente nomeclatura
'''

    
    