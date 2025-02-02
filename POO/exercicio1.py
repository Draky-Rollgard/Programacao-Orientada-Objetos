'''
MODIFIQUE O CODIGO DA CLASSE A SEGUIR PARA
TRANSFORMAR GETTER E SETTER USANDO O PADRÃO
DE PROPRIEDADE EM PYTON.
'''
class Student:
    def __init__(self, nome, age):
        self.nome = nome
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age > 0:
            self.__age = age
            #print("Error!!!! The age informed is not true! Please, try again.")
            #self.__age = 0
        else:
            #self.__age = age
            print("Error!!!! The age informed is not true! Please, try again.")
            self.__age = 0
            

stud = Student('Vanessa', 19)
print('Name:', stud.nome, stud.age)
stud.age =12
#Não use stud.age(16), pois um TypeError é informado: 
#'int' object is not callable

print('Name:', stud.nome, stud.age)


    


