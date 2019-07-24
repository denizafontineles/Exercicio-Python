
class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def mostrar_nome(self):
        return self.nome

    def mostrar_idade(self):
        return self.idade

class Pet:
    def __init__(self,nome_pet,nome_dono,nascimento):
        self.nome_pet = nome_pet
        self.nome_dono = nome_dono
        self.nascimento = nascimento

    def mostrar_pet(self):
        print (self.nome_pet)
    
    def mostrar_dono(self):
        print (self.nome_dono)
    
    def mostrar_nascimento(self):
        print (self.nascimento)

pessoa = Pessoa ('Deniza', '20')
print(pessoa.mostrar_nome(), pessoa.mostrar_idade())

pet = Pet ('bob', 'deniza', '24/07/2019')
print(pet.mostrar_pet(), pet.mostrar_dono(), pet.mostrar_nascimento())