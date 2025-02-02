#Listas

#------------------------------------------------------
#índ 0  1  2  3  4
#    |  |  |  |  |
l = [1, 2, 3, 4, 5] #Listas indexadas a partir do 0

print(len(l)) # Imprime o tamanho da lista
print(l[0]) # acessa o primeiro elemento da lista
print(l[-1]) # acessa o ultimo elemento da lista

#Adiciona um novo elemento no final da lista
#-----------------------------------------------------

l = [] # Lista vazia

print(len(l))

#Adicionar um novo elemento no final da lista
l.append(5)
l.append(7)
l.append(9)

print(l)

#--------------------------------------------------
l = [0, "oi", 3.14, [1,2,3]]

# Ver o tipo da Lista
print(type(l[0])) 
print(type(l[1]))
print(type(l[3]))
print(type(l[4]))

print(type(l[3][0]))

print("esta é a sublista:", l[3])

#-------------------------------------------------
# Concatenar lista

l1 = [1, 3, 5, 7]
l2 = [2, 4, 6, 8]

l3 = l1+l2
l3.sort()
print(l3)

#-----------------------------------------------