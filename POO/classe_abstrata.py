from abc import ABC, abstractmethod

class Myclass(ABC):
    @abstractmethod
    def my_method(self):
        pass

m1=Myclass()
m1.my_method()

# O que antes era realizado da forma a seguir: