'''
Métodos a serem desenvolvidos
abastecerPorValor() - informado o valor abastecido e mostra a quantidade de litros colocada
abastecerPorLitro() - informado a quantidade em litros de combustivel e mostra o valor a ser pagp
alterarValor() - altera o valor do litro
alterarQuantidadeCombustivel() - atera o combustivel restante na bomba

Sempre que ocorrer um abastecimento, 
é necessário atualizar a quantidade 
de combustível na bomba.
'''

'''
class BombaCombustivel:
    def __init__(self, valorLitro:float, quantidadeCombustivel:float):
        self.valorLitro = valorLitro
        self.__quantidadeCombustivel = quantidadeCombustivel

    
    def abastecerPorValor(valor:float) -> None:
        litros = valor / self.valorLitro
        if self.alterarQuantidadeCombustivel(self.__quantidadeCombustivel - litros):
            #
            print("Abastecendo", litros, "litros")
        else:
            print("Abastecimento não permitido")    

    def abastecerPorLitro(litros:float) -> None:
        if self.alterarQuantidadeCombustivel(self.__quantidadeCombustivel - litros):
            valor = litros * self.valorLitro
        print("Abastecendo", valor, "reais")
        else:
        print("Abastecimento não permitido")


  
    def __alterarValor(self, novoValor:float) -> None:
        if valor >= 0:
            self.__valorLitro = novoValor


    def __alterarQuantidadeCombustivel(self, novaQuantidade:float) -> bool:
        if novaQuantidade >= 0:
            self.__quantidadeCombustivel = novaQuantidade
            return True
        else:
            return False

    def relatorio(self):
        print("Quantidade de combustivel:", self.__quantidadeCombustivel)
        print("Valor de combustivel:", self.__quantidadeCombustivel)


BC = BombaCombustivel(5.50, 300)
print(BC.valorLitro, BC.quantidadeCombustivel)
#BC.__alterarQuantidadeCombustivel(200) é privado
BC.abastecerPorLitro(litros = 100)
BC.abastecerPorValor(valor = 200)
BC.relatorio()
BC.abastecerPorLitro(litros = 100)
BC.abastecerPorValor(valor = 200)
BC.relatorio()
BC.abastecerPorLitro(litros = 100)
BC.abastecerPorValor(valor = 200)
BC.relatorio()

'''
