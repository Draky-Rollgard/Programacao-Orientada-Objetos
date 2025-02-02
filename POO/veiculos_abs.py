from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, velocidade:float, marca:str):
        self.velocidade = velocidade
        self.marca = marca

    @abstractmethod
    def mover(self, metros:int)->str:
        pass

class Carro(Veiculo):
    def __init__(self, velocidade:float, marca:str, numPortas):
        super().__init__(velocidade, marca)
        self.numPortas = numPortas

    def mover(self, metros:int)->str:
        return f"O carro {self.marca} com uma velocidade de {self.velocidade} correu {metros} metros."
    
class Aviao(Veiculo):
    def __init__(self, velocidade:float, marca:str, tipo:str):
        super().__init__(velocidade, marca)
        self.tipo = tipo

    def mover(self, metros:int)->str:
        return f"O aviao {self.marca} com uma velocidade de {self.velocidade} voou {metros} metros."

class Barco(Veiculo):
    def __init__(self, velocidade:float, marca:str, tamanho:float):
        super().__init__(velocidade, marca)
        self.tamanho = tamanho

    def mover(self, metros:int)->str:
        return f"O barco {self.marca} com uma velocidade de {self.velocidade} navegou {metros} metros."

C1 = Carro(200.01, "Fiat Uno", 4)
print(C1.mover(12000))

A1 = Aviao(500.65, "XwFork", "jato")
print(A1.mover(2000))

B1 = Barco(300.00, "stringx", 200)
print(B1.mover(653))