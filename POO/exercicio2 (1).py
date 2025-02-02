class Ponto2D:
    def __init__(self, X:float = 0, Y:float = 0): # valor dedfault do parametro.
        self.__x = X
        self.__y = Y

    def Compara(self, outtroponto:'Ponto2D') -> bool:
        if self.__x == outtroponto.__x and self.__y == outtroponto.__y:
            return
        
p1 = Ponto2D(10, 10)
p2 = Ponto2D() # construtor default
if(p1.compara(p2)):
    print("Os pontos são iguais")
else:
    print("Os pontos são diferentes")
    

