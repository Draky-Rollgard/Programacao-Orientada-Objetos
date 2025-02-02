'''
REALIZAÇÃO ORIGINAL DA ATIVIDADE

from abc import ABC, abstractmethod

class Publicacao(ABC):
    def __init__(self, titulo:str, autor:str):
        self.titulo = titulo
        self.autor = autor

    @abstractmethod
    def informacoes(self)->str:
        pass

class Livro(Publicacao):
    def __init__(self, titulo:str, autor:str, numero_paginas:int):
        super().__init__(titulo, autor)
        self.np = numero_paginas

    def informacoes(self):
        #return super().informacoes()
        return f"Livro: {self.titulo}, {self.autor}, {self.np}."
    
class Artigo(Publicacao):
    def __init__(self, titulo:str, autor:str, revista:str):
        super().__init__(titulo, autor)
        self.rv = revista

    def informacoes(self):
        #return super().informacoes()
        return f"Artigo: {self.titulo}, {self.autor}. Publicado em: {self.rv}."
    
class Revista(Publicacao):
    def __init__(self, titulo:str, autor:str, edicao:int):
        super().__init__(titulo, autor)
        self.ed = edicao

    def informacoes(self):
        #return super().informacoes()
        return f"Revista: {self.titulo}, {self.autor} Edição: {self.ed}."

L1 = Livro("As crônicas de Nárnia", "C.S. Lewis", 200)
print(L1.informacoes())

A1 = Artigo("Jogos LARP RPG como alternativa aos desafios da aprendizagem na defasagem educacional", "Fulano", "De Olho no Mundo")
print(A1.informacoes())

R1 = Revista("De Olho no Mundo", "Ciclano", 200)
print(R1.informacoes())
'''






'''

TESTE ALTERNATIVO
from abc import ABC, abstractmethod

class Publicacao(ABC):
    def __init__(self, titulo:str, autor:str):
        self.titulo = titulo
        self.autor = autor

    @abstractmethod
    def __str__(self)->str:
        pass

class Livro(Publicacao):
    def __init__(self, titulo:str, autor:str, numero_paginas:int):
        super().__init__(titulo, autor)
        self.np = numero_paginas

    def __str__(self):
        #return super().informacoes()
        return f"Livro: {self.titulo}, {self.autor}, {self.np}."
    
class Artigo(Publicacao):
    def __init__(self, titulo:str, autor:str, revista:str):
        super().__init__(titulo, autor)
        self.rv = revista

    def __str__(self):
        #return super().informacoes()
        return f"Artigo: {self.titulo}, {self.autor}. Publicado em: {self.rv}."
    
class Revista(Publicacao):
    def __init__(self, titulo:str, autor:str, edicao:int):
        super().__init__(titulo, autor)
        self.ed = edicao

    def __str__(self):
        #return super().informacoes()
        return f"Revista: {self.titulo}, {self.autor} Edição: {self.ed}."

L1 = Livro("As crônicas de Nárnia", "C.S. Lewis", 200)
A1 = Artigo("Jogos LARP RPG como alternativa aos desafios da aprendizagem na defasagem educacional", "Fulano", "De Olho no Mundo")
R1 = Revista("De Olho no Mundo", "Ciclano", 200)

print(L1)
print(A1)
print(R1)
print("\n")

#inserindo em uma lista seria:
Pub: list[Publicacao] = [L1, A1, R1]
#print(Pub)  corresponde a impressão sem uma representação

for p in Pub:
    print(p)
'''


#posso utilizar repr para reparar/ formatar a impressão. Como abaixo:
from abc import ABC, abstractmethod

class Publicacao(ABC):
    def __init__(self, titulo:str, autor:str):
        self.titulo = titulo
        self.autor = autor

    @abstractmethod
    def __repr__(self)->str:
        pass

class Livro(Publicacao):
    def __init__(self, titulo:str, autor:str, numero_paginas:int):
        super().__init__(titulo, autor)
        self.np = numero_paginas

    def __repr__(self):
        #return super().informacoes()
        return f"Livro: {self.titulo}, {self.autor}, {self.np}."
    
class Artigo(Publicacao):
    def __init__(self, titulo:str, autor:str, revista:str):
        super().__init__(titulo, autor)
        self.rv = revista

    def __repr__(self):
        #return super().informacoes()
        return f"Artigo: {self.titulo}, {self.autor}. Publicado em: {self.rv}."
    
class Revista(Publicacao):
    def __init__(self, titulo:str, autor:str, edicao:int):
        super().__init__(titulo, autor)
        self.ed = edicao

    def __repr__(self):
        #return super().informacoes()
        return f"Revista: {self.titulo}, {self.autor} Edição: {self.ed}."

L1 = Livro("As crônicas de Nárnia", "C.S. Lewis", 200)
A1 = Artigo("Jogos LARP RPG como alternativa aos desafios da aprendizagem na defasagem educacional", "Fulano", "De Olho no Mundo")
R1 = Revista("De Olho no Mundo", "Ciclano", 200)

#inserindo em uma lista seria:
Pub: list[Publicacao] = [L1, A1, R1]
print(Pub)