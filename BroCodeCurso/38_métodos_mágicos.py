# Métodos mágicos = Métodos Dunder (double underscore ou duplo sublinhado) __init__, __str__, __eq__
#                   Eles são automaticamente chamados por muitas operações internas do Python.
#                   Eles permitem que os desenvolvedores definam ou personalizem o comportamento de objetos.

class Livro:
    def __init__(self, titulo, autor, n_pág):
        self.titulo = titulo
        self.autor = autor
        self.n_pág = n_pág

    def __str__(self):
        return f'{self.titulo} por {self.autor}'

    def __eq__(self, outro):
        return self.titulo == outro.titulo and self.autor == outro.autor

    def __gt__(self, outro):
        return self.n_pág > outro.n_pág
    
    def __lt__(self, outro):
        return self.n_pág < outro.n_pág

    def __add__(self, outro):
        return self.n_pág + outro.n_pág

    def __sub__(self, outro):
        return self.n_pág - outro.n_pág

    def __contains__(self, caractere):
        return caractere in self.titulo or caractere in self.autor

    def __getitem__(self, key):
        match key:
            case 'titulo':
                return self.titulo
            case 'autor':
                return self.autor
            case 'pags':
                return self.n_pág
            case _:
                return 'Chave não encontrada'

livro1 = Livro('O Investidor Inteligente', 'Benjamin Graham', 256)
livro2 = Livro('Harry Poter e a Pedra Filosofal', 'J. K. Rowling', 342)
livro3 = Livro('Pequeno Príncipe', 'Antoine de Saint-Exupéry', 124)

# print(livro1) -> __str__
# print(livro1==livro2) -> __eq__
# print(livro1<livro2) -> __lt__
# print(livro1+livro2) -> __gt__ 
# print(livro2-livro3) -> __sub__
# print('Inteligente' in livro1) -> __contains__
# print(livro1['ano']) -> __getitem__
