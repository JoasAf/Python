# variáveis de classe = É compartilhada com todas as instâncias da classe
#                       Definidas fora do contructor
#                       Permite você compartilhar dados entre todos os objetos creados dentro da classe

class Estudante:
    ano = 2025
    num_estudantes = 0

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        Estudante.num_estudantes += 1


estudante1 = Estudante('Joás', 17)
estudante2 = Estudante('Anna', 16)
estudante3 = Estudante('Cintia', '16')
estudante4 = Estudante('Thalyta', '16')
estudante5 = Estudante('Thomas', 15)

print(f'Minha turma de {Estudante.ano} tem {Estudante.num_estudantes} estudantes')
print(estudante1.nome)
print(estudante2.nome)
print(estudante3.nome)
print(estudante4.nome)
print(estudante5.nome)

