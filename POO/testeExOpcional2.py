#Crie um programa em pyton que defina uma função
#que some dois números quaisquer e retorne o re-
#sultado da soma. Teste sua função lendo dois va-
#lores do usuário.

#-----------------------------------------------------------------------------------------------------

#Python ignora tipos. Você pode definir tipos, mas também pode verificar o tipo com testes

# Execute no terminal e veja o erro
def soma(a:int, b:int):   # tipagem para, opcionalmente, executar o analisador de tipo: mypy aula1.py
    return a + b

x = "oi"
y = 3

result = soma(x, y)
print(result)
#-----------------------------------------------------------------------------------------------------

#Outro exemplo de tipagem
def soma(a, b): 
    return a + b

x:str = "oi"
y:str = "Tudo bem"

result = soma(x, y)
print(result)

#-----------------------------------------------------------------------------------------------------