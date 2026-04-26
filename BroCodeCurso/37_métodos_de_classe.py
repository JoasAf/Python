# Métodos de Classe = Permite operações relacionadas à própria classe
#                     Pega (cls) como primeiro parâmetro, que representa a própria classe

class Estudante:

    cont = 0
    médiatotal = 0

    def __init__(self, nome, média):
        self.nome = nome
        self.média = média
        Estudante.cont += 1
        Estudante.médiatotal += média
 
    # Método de Instância
    def info(self):
        return f'{self.nome}: {self.média}'
    
    @classmethod
    def pega_cont(cls):
        return f'Total de estudantes: {cls.cont}'
    
    @classmethod
    def pega_media(cls):
        if cls.cont == 0:
            return 0
        
        return f'Média total: {cls.médiatotal/cls.cont:.1f}'


est1 = Estudante('Joás', 7.8)
est2 = Estudante('Anna', 9.2)

print(Estudante.pega_cont())
print(Estudante.pega_media())