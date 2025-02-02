def convert_result(tipo):
    def interna(func):
        def aninhada(*args, **kwargs): # pode chamar o aninhada de wrapper
            # Fazendo cast
            #return (tipo)(func(*args, **kwargs))
            result = func(*args, **kwargs)
            
            return tipo(result)
        return aninhada
    return interna

# Exemplo de uso:
@convert_result(int)
def soma(a, b): #-> str: Assim não funciona
    total = a + b
    return str(total)  

@convert_result(float)
def divisao(a, b):
    total = a / b
    return str(total)  

resultado = soma(5,5)
print(type(resultado)) 
print(type(divisao(10, 4.3)))