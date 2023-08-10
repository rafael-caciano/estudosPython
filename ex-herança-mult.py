class pessoa:
    def __init__(self):
        self.cpf = 111111111
        self.nome= none   
        self.endereco= none

class funcionario(pessoa):
    def __init__(self):
        self.matricula = None
        self.salario = None

    
f1 = funcionario()
f1.nome = 'mauricio'

print (f1.nome)
