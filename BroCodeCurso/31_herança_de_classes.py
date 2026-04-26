# Herança de classe = Permite um classe herdar atributos e métodos de outra classe
#                     Ajuda na reusabilidade e extensibilidade
#                     criança(pai)

class Animal:
    def __init__(self, nome):
        self.nome = nome
        self.vivo = True

    def comer(self):
        print(f'{self.nome} está comendo')

    def dormir(self):
        print(f'{self.nome} está dormindo')



class Cão(Animal):
    def falar(self):
        print('AuAu!')

class Gato(Animal):
    def falar(self):
        print('Miau!')

cao = Cão('Rubi')

gato = Gato('Lise')

print(gato.nome)
print(gato.vivo)
gato.comer()
gato.dormir()
gato.falar()