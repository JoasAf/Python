# Herança múltipla = herdar mais de uma classe pai
#                    C(A, B)

# Herança multinível = herdar uma classe pai que herdou outra classe pai
#                      C(B) <-- B(A) <-- A

class Animal:
    def comer(self):
        print(f'Esse animal está comendo')

    def dormir(self):
        print(f'Esse animal está dormindo')


class Presa(Animal):
    def fugir():
        print('Esse animal está fugindo')

class Predador(Animal):
    def caçar():
        print('Esse animal está caçando')

class Coelho(Presa):
    pass

class Águia(Predador):
    pass

class Peixe(Presa, Predador):
    pass


coelho = Coelho()
águia = Águia()
peixe = Peixe()

peixe.dormir()