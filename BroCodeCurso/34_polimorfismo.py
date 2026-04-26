# polimorfismo = Palavra grega que significa "Ter várias formas ou faces"
#                Poli = Vários
#                Morfo = Forma

#                Dois jeitos de ativar polimorfismo
#                1. Herança: Um objeto pode ser tratado da mesma forma que a classe pai
#                2. "Duck Typing": Objeto que tem necessáriamente atributos/métodos

class Formas:
    def area(self):
        pass

class Círculo(Formas):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * self.raio**2  

class Quadradro(Formas):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado**2

class Triângulo(Formas):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura / 2

class Pizza(Círculo):
    def __init__(self, sabor, raio):
        self.sabor = sabor
        self.raio = raio


formas = [Círculo(4), Quadradro(5), Triângulo(6, 7), Pizza('Calabresa', 22.5)]

for forma in formas:
    print(f'{forma.area()}cm²')