class Data:
    def __init__(self, dia:int, mes:int, ano:int):
        self.dia = dia
        self.__mes = mes
        self.__ano = ano

    @dia.setter
    def dia(self, valor:int) -> None:
        if dia < 1:

            if mes%2 != 0 or mes = 8:
                if dia >0 and <= 31:
                    self.__dia = valor
            if mes%2 = 0 and mes != 8:
                 

                   
        
        self.__dia = valor
        
    def mes(self, valor:int) -> None:
        #self.__mes = valor
        if valor > 0:
            if valor <= 11:
                self.__mes = valor
        else:
            print("Data inválida")    

            

        
    def ano(self, valor:int) -> None:
        if valor >= 0:
            self.__ano = valor
        
    
    
    def __str__(self) -> str:
        return f"{self.__dia:02}/{self.__mes:02}/{self.__ano:04}" # interpolação de strings
        #return str(self.__dia) + '/'+ str(self.__mes)  + '/'+ str(self.__ano)

d1 = Data(12, 11, 2024)
print(d1)

# 01 03 05 07 08 10 12 são meses com 31 dias