# @propriedade = Decorator usado para definir um método como uma propriedade
#                (Pode ser acessado como um atributo)
#                Benefícios: Adiciona uma lógica quando ler escrever ou deletar atributos
#                Dá a você os métodos getter, setter e deleter

class Retângulo:
    def __init__(self, largura, altura):
        self._largura = largura
        self._altura = altura

    @property
    def largura(self):
        return f'{self._largura:.1f}cm'

    @property
    def altura(self):
        return f'{self._altura:.1f}cm'
    
    @largura.setter
    def largura(self, nova_largura):
        if nova_largura > 0:
            self._largura = nova_largura
        else:
            print('Largura tem que ser maior que 0')

    @altura.setter
    def altura(self, nova_altura):
        if nova_altura > 0:
            self._altura = nova_altura
        else:
            print('Altura tem que ser maior que 0')

    @largura.deleter
    def largura(self):
        del self._largura
        print('Deletado')
    
    @altura.deleter
    def altura(self):
        del self._altura
        print('Deletado')

retangulo = Retângulo(5, 6)

del retangulo.largura
del retangulo.altura

