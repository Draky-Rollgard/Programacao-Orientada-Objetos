def limit_calls(numero_limite:int):
    def interna(func):
        count = 0
        def wrapper(*args,**kwargs):
            nonlocal count #usar count de fora
            if count > numero_limite:
                raise Exception("Limites de chamada excedido")
            count +=1
            func(*args, **kwargs)
        return wrapper
    return interna

@limit_calls(4)
def imprime_mensagem():
    print("Mais um dia se passa!")

imprime_mensagem()
imprime_mensagem()
imprime_mensagem()
imprime_mensagem()
#imprime_mensagem()