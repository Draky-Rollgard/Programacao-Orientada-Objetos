'''
Decorador é uma função que recebe outra função como parametro
estendemos o comportamneto de uma função sem modificar ela

Conhecemos os decoradores como o @. De foma mais pura entende-se por decoradores uma função

def soma_um(num):
    return num+1

return tranforma uma entrada em uma saída
mas se pararmos para pensar, o print retorna None e aparece no terminal como efeito
'''
def diga_ola(nome):
    return f'olá {nome}'

def seja_incrivel(nome):
    return f"Oi, {nome}. Juntos somos os mais incríveis!"

def cumprimente_bob(funcao_cumprimento):
    return funcao_cumprimento("Bob")

#print (diga_ola("joao"))
ret = cumprimente_bob(diga_ola)
print(ret)
ret = cumprimente_bob(seja_incrivel)

def pai():
    print("Imprimindo pai()")
    def primeiro_filho():
        print("Imprimindo primeiro_filho()")
    def segundo_filho():
        print("Imprimindo segundo_filho()")

    segundo_filho()
    primeiro_filho()
# não importa a ordem de definição de um método, mas sim a de chamada.

def pai(num):
    def primeiro_filho():
        print("Oi!! Eu sou Elias")
    def segundo_filho():
        print("Me chame de Ester")
    if num == 1:
        return primeiro_filho
    else:
        return segundo_filho

ret = pai(1)
print(ret())

def decorador(func):
    def aninhada():
        print("Algo esta acontecendo antes da função ser chamada")
        func()
        print("Algo esta acontecendo depois da função ser chamada")
        return aninhada
    
def diga_uau():
    print("UAUU!!")

diga_uau = decorador(diga_uau) #Englobar decorador na propria função diga_uau!

diga_uau()
#PROCESSO DE DECORAÇÃO

#SINTAX SUGAR
@decorador # é a redefinição de uma função, 
           # mas de uma forma menos trabalhosa.


def decorador(func):
    def aninhada():
        print("Algo esta acontecendo antes da função ser chamada")
        func()
        print("Algo esta acontecendo depois da função ser chamada")
        return aninhada
    
@decorador
def diga_uau():
    print("UAU!!!")

diga_uau()

# outro exemplo
def duas_vezes(func):
    def aninhada_duas_vezes():
        func()
        func()
    return aninhada_duas_vezes

@duas_vezes
def diga_uau():
    print("UAU!")

@duas_vezes
def cumprimentar(nome):
    print(f"Oi, {nome}!")

cumprimentar("Fulano") # se chamar isso aqui, vai dar erro pois estamos passando um parâmetro para funções que não aceitam argumentos, a menos que passe argumentos na função interna

''''''''''''''
def f(a:int, b:int):
    pass

f(1,2) #args aceita parametros posicionais
f(a=1,b=2)#kwargs aceita parametros nominais
''''''''''''''

def duas_vezes(func):
    def aninhada_duas_vezes(*args,**kwargs):
        func(*args,**kwargs) # Aceita 0 ou mais paramentros
        func(*args,**kwargs)
    return aninhada_duas_vezes

@duas_vezes
def diga_uau():
    print("UAU!")

@duas_vezes
def cumprimentar(nome):
    print(f"Oi, {nome}!")

diga_uau()
cumprimentar("Fulano")

from datetime import datetime
from time import sleep

def medidor_tempo(func):
    def aninhada(*args,**kwargs):
        tempo_inicial = datetime.now()

        resultado = func(*args,**kwargs)

        tempo_final = datetime.now()
        tempo = tempo_final - tempo_inicial

        print(f'{func.name} demorou {tempo.total_seconds()}')


##########################  EXERCÍCIO  #############################################

def repeat(n:int):
    def interna(func):
        def aninhada(*args,**kwargs):
            for i in range (n):
                func() #invocar a funcao n vezes
    
@repeat(5)
def diga_uau():
    print("Uau!")

diga_uau()
#############################################################
#   criar decorador convert_result que aceita varios tipos
#   como argumento e converta esse tipo antes de retorna-lo;

def convert_result(n):
    def interna(func):
        def aninhada(*args,**kwargs):
            convert =  
            func()
    
@convert_result("int")
def operacao() -> str: 
    resultado = 10.00 + 2.57
    return resultado
    

diga_uau()

#####################################################################
# fazer 