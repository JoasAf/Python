# super() = Função usada em uma classe criança para chamar métodos de uma classe pai (superclass)
#           Permite você estender

class Formas:
    def __init__(self, cor, preenchido):
        self.cor = cor
        self.preenchido = preenchido

    def descrição(self):
        print(f'É {self.cor} e {"é preenchido" if self.preenchido else "não é preenchido"}')

class Círculo(Formas):
    def __init__(self, cor, preenchido, raio):
        super().__init__(cor, preenchido)
        self.raio = raio

    def descrição(self):
        super().descrição()
        print(f'É um círculo com a área de {3.14*self.raio**2:.2f}cm²')

class Quadrado(Formas):
    def __init__(self, cor, preenchido, largura):
        super().__init__(cor, preenchido)
        self.largura = largura

    def descrição(self):
        super().descrição()
        print(f'É um quadrado com a área de {self.largura**2:.2f}cm²')

class Triângulo(Formas):
    def __init__(self, cor, preenchido, largura, altura):
        super().__init__(cor, preenchido)
        self.largura = largura
        self.altura = altura

    def descrição(self):
        super().descrição()
        print(f'É um triângulo com a área de {(self.largura*self.altura)/2:.2f}cm²')


circulo = Círculo('Azul', False, 7)
quadrado = Quadrado('Amarelo', True, 10)
triangulo = Triângulo('Vermelho', True, 7, 5)

# print(triangulo.cor)
# print(triangulo.preenchido)
# print(f'{triangulo.largura}cm')
# print(f'{triangulo.altura}cm')

circulo.descrição()