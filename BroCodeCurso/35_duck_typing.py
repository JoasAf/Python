# "Duck Typing" = Outro jeito de ativar o polimorfismo ao lado de Herdar
#                 Objeto tem que ter os atribrutos/métodos mínimos necessários
#                 "Se isso se parece com um pato e faz quack igual um pato, tem que ser um pato"

class Carro:
    duro = True

class Civic(Carro):
    def combustível(self):
        print('Gasolina')

class Ônibus(Carro):
    def combustível(self):
        print('Diesel')

class Joás:
    duro = False

    def combustível(self):
        print('Café')


carros = [Civic(), Ônibus(), Joás()]

for carro in carros:
    carro.combustível()
    print(carro.duro)