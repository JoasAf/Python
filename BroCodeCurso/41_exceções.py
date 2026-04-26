# Exceções = É um evento que interrompe o programa
#            (ZeroDivisionError, TypeError, ValueError)
#            1.try, 2.except, 3.finally

try:
    número = int(input('Digite um número: '))
    print(1/número)
except ZeroDivisionError:
    print('Não é possível dividir por zero!')
except ValueError:
    print('Digite um número por favor!')
finally:
    print('Matémáticá')