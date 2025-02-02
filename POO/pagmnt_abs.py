from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, valor:float):
        self.v = valor

    @abstractmethod
    def processar_pagamento(self):
        pass

class CartaoCredito(Pagamento):
    def processar_pagamento(self):
        print(f"Pagamento de {self.v} via Cartão de Crédito aprovado.")

class Boleto(Pagamento):
    def processar_pagamento(self):
        print(f"Boleto de {self.v} gerado para pagamento.")

class Pix(Pagamento):
    def processar_pagamento(self):
        print(f"Pix de {self.v} foi processado.")

#exemplos
print("\n  1.Exemplos para teste de instanciação")
P1 = CartaoCredito(200)
P2 = Boleto(750)
P3 = Pix(567)

P1.processar_pagamento()
P2.processar_pagamento()
P3.processar_pagamento()
print("\n  2.Lista com os diferentes tipos de pagamentos")

ListaPagamentos: list[Pagamento] = [
    CartaoCredito(200),
    Boleto(700.89), 
    Pix(230),
    CartaoCredito(187.69),
    Pix(33.45),
    Pix(12.91)
    ]

for pag in ListaPagamentos:
    pag.processar_pagamento()
print("\n")

'''
from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, valor:float):
        self.v = valor

    @abstractmethod
    def processar_pagamento(self):
        pass

class CartaoCredito(Pagamento):
    def __init__(self, valor:float = 200):
        self.v = valor

    def processar_pagamento(self):
        print(f"Pagamento de {self.v} via Cartão de Crédito aprovado.")

class Boleto(Pagamento):
    def __init__(self, valor:float):
        self.v = valor

    def processar_pagamento(self):
        print(f"Boleto de {self.v} gerado para pagamento.")

class Pix(Pagamento):
    def __init__(self, valor:float):
        self.v = valor

    def processar_pagamento(self):
        print(f"Pix de {self.v} foi processado.")

#exemplos
print("\n  1.Exemplos para teste de instanciação")
P1 = CartaoCredito()
P2 = Boleto(750)
P3 = Pix(567)

P1.processar_pagamento()
P2.processar_pagamento()
P3.processar_pagamento()
print("\n  2.Lista com os diferentes tipos de pagamentos")

ListaPagamentos = [CartaoCredito(),Boleto(700), Pix(230)]

i = 0
while i < len(ListaPagamentos):
    ListaPagamentos[i].processar_pagamento()
    i+=1
print("\n")
'''