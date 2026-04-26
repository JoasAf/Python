# Métodos estáticos = É um método que pertence a um classe ao invés
#                     de um objeto de uma classe (instância)
#                     Muito usado para maioria das funções úteis

# Métodos de Instância = Melhor para operações com instâncias da classe (objetos)
# Métodos estáticos = Melhor para funções de ultilidade que não precisam acessar os dados da classe

class Empregado:

    def __init__(self, nome, posição):
        self.nome = nome
        self.posição = posição

    def info(self):
        return f'{self.nome}: {self.posição}'
    
    @staticmethod
    def é_pos_valida(posição):
        pos_validas = ['Gerente', 'Caixa', 'Cozinheiro', 'Faxineiro']
        return posição in pos_validas
    
print(Empregado.é_pos_valida('Programador'))