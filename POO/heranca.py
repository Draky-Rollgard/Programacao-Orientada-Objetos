'''
DEFINIÇÃO

A herança evita a repetição de códigos. Sendo uma relação entre elementos mais genéricos e 
mais específicos. Também é chamado de generalização ou especificação.

------------------------------------------------------------------------------------
RELACIONAMENTO ENTRE CLASSES

premissas básicas de relacionamentos de herança:

- Uma classe (subclasse) estende (herda) outra classe(superclasse)

1. SUBCLASSES  - (ou classe derivada) ela herda todos os atributos e métodos. 
Abrange os atributos mais específicos. Ela pode adicionar novos atibutos ou
métodos particulares, mas não podem remover.
Exemplo.: Aluno: que vai conter todos os atributos e métodos da superclasse


2. SUPERCLASSES - (ou classe base) abrange o mais geral. Contém os atributos mais comuns.
Usuário onde há um relacionamento com aluno
--------------------------------------------------------------------------------------
SEMÂNTICA

Semântica: "é um"
A subclasse "é um" da superclasse.
O aluno "é uma" pessoa
O professor "é uma" pessoa

Contole remoto "é um" dispositivo eletrônico
Celular "é um" dispositivo eletrônico
Garrafinha não é um dispositivo eletrônico. -> Não pode herdar características de um dispositivo eletrônico

-------------------------------------------------------------------------------------
NÍVEIS DE HERANÇA





'''
class veiculo:
    def __init__(self, tipo, chassi, marca, modelo, ano):
        self.tipo = tipo
        self.chassi = chassi
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        
class carro(veiculo):
    def __init__(self, tipo, chassi, marca, modelo, ano, n_portas):
        super().__init__(tipo, chassi, marca, modelo, ano)
        self.n_portas = n_portas

class motocicleta(veiculo):
    def __init__(self, tipo, chassi, marca, modelo, ano, cc):
        super().__init__(tipo, chassi, marca, modelo, ano)
        self.cc = cc

carro1 = carro('carro', 'aefrfdfw3q2f', 'honda', 'civic', '2023', 4)
moto1 = motocicleta('motocicleta', 'aesraefr563', 'honda', 'Transalp', 2018, 600) 

'''
Função isinstance: é uma instância de...

'''
print(isinstance(carro1, carro))
print(isinstance(moto1, veiculo))
'''
extends: se é herança da outra classe
public class Aluno extends Pessoa'''