#Crie um programa em python que inicia uma lista vazia
# leia um inteiro n do usuário e "aumente" a lista in-
#crementalmente contendo os inteiros de 1 a n.

l= []
n = int(input("Informe n: "))

for i in range(n):
    l.append(i+1)
    print(l)
