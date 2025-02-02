class Pessoa:
    def __init__(self, nome:str, idade:int):
        #self.setNome(nome)
        #self.setIdade(idade)
        #self.__nome = nome
        #self.__idade = idade
        self.nome = nome
        self.idade = idade

    @property
    def nome(self) -> str: #getter propriedade
        return self.__nome
    @nome.setter
    def nome(self, nome:str) -> None:
        self.__nome = nome
    @property # temos aqui um decorador ou decorator
    def idade(self) -> int: #getter
        return self.__idade
    @idade.setter
    def idade(self, idade:int) -> None:
        if idade < 0:
            self.__idade = 0
        else:
            self.__idade = idade

p1 = Pessoa("Fulano", 10)
print(p1.nome, p1.idade) #não ha necessidade de invocação na instanciação
p2 = Pessoa("Ciclano", 0)
print(p2.nome, p2.idade)
