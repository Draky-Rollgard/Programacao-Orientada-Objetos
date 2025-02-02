from datetime import date
class pessoa:
    
    def __init__(self, nome:str, sexo:str, cpf:str, data_nasc:date):
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf
        self.data_nasc = data_nasc
    def __str__(self):
        return f"{self.nome}, {self.sexo}, {self.cpf}, {self.data_nasc}"
        
class aluno(pessoa):
    def __init__(self, nome: str, sexo: str, cpf: str, data_nasc: date, curso:str, data_ingresso:date):
        super().__init__(nome, sexo, cpf, data_nasc)
        self.data_nasc = data_nasc
        self.curso = curso
        self.data_ingresso = data_ingresso
    def __str__(self):
        return f"{self.nome}, {self.sexo}, {self.cpf}, {self.data_nasc}, {self.curso}, {self.data_ingresso}"

class funcionario(pessoa):
    def __init__(self, nome: str, sexo: str, cpf: str, data_nasc: date, departamento:str, data_admissao:date, salario:float):
        super().__init__(nome, sexo, cpf, data_nasc)
        self.departamento = departamento
        self.data_admissao = data_admissao
        self.salario = salario
    
    def __str__(self):
        return f"{self.nome}, {self.sexo}, {self.cpf}, {self.data_nasc}, {self.departamento}, {self.data_admissao}, {self.salario}"

class professor(funcionario):
    def __init__(self, nome: str, sexo: str, cpf: str, data_nasc: date, departamento: str, data_admissao: date, salario: float, titulacao:str):
        super().__init__(nome, sexo, cpf, data_nasc, departamento, data_admissao, salario)
        self.titulacao = titulacao
    
    def __str__(self):
        return f"{self.nome}, {self.sexo}, {self.cpf}, {self.data_nasc}, {self.departamento}, {self.data_admissao}, {self.salario},{self.titulacao}"

class TecnicoAdministrativo(funcionario):
    def __init__(self, nome: str, sexo: str, cpf: str, data_nasc: date, departamento: str, data_admissao: date, salario: float, cargo: str):
        super().__init__(nome, sexo, cpf, data_nasc, departamento, data_admissao, salario)
        self.cargo = cargo
    
    def __str__(self):
        return f"{self.nome}, {self.sexo}, {self.cpf}, {self.data_nasc}, {self.departamento}, {self.data_admissao}, {self.salario}, {self.cargo}"





p1 = pessoa('f', 'm', '1341423213', date(2002, 7, 14))
#print(p1.nome, p1.sexo, p1.cpf, p1.data_nasc)