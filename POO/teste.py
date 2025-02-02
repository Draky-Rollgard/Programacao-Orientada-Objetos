

#-----------------------------------------------------------------------------------
#PASSAR 
#n = 20

#print (1)
#print (2)
#print (3)

#i = 0
#while i<n:
#    print (i + 1)
#    i += 1

#------------------------------------------------------------------------------------
#n = input()    #Leitura feita por input sempre retorna uma string. Precisamos 
                # converter a captura do imput para inteiro

#definição da função
def imprime_de_1_a_n(n):
    for i in range(n):  #Estrutura indexável (range). range = intervalo de 0 a n-1
        print (i + 1)
        #return n

#Execução principal
#n = int(input("Informe um número inteiro: "))        Variável n só existe dentro da função

valor = int(input("Informe um número inteiro: "))

#Invocação da função
imprime_de_1_a_n(valor)
imprime_de_1_a_n(valor*2)

#Pode ocorrer de funções ter um return

