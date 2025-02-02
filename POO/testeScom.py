
#definição da função
def imprime_de_1_a_n(n):
    for i in range(n):  
        print (i + 1)
        

#Execução principal
valor = int(input("Informe um número inteiro: "))

#Invocação da função
imprime_de_1_a_n(valor)
imprime_de_1_a_n(valor*2)


