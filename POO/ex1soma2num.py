#Crie um programa em pyton que defina uma função
#que some dois números quaisquer e retorne o re-
#sultado da soma. Teste sua função lendo dois va-
#lores do usuário.

def soma_dois_numeros(x, y):
    return x + y

num1 = int (input("Informe um número"))
num2 = int (input("Informe outro número"))

result = soma_dois_numeros(num1, num2)
print(result)

