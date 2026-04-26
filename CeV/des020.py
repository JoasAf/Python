from random import shuffle
alunos = [input("1º Aluno: "), input("2º Aluno: "), input("3º Aluno: "), input("4º Aluno: ")]
shuffle(alunos)
print("A ordem de apresentação vai ser: {}!".format(alunos))
