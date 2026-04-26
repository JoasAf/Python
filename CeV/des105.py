def notas(*n, sit=False):
    """
    ---> Analisar notas e situação de uma turma

    :param n: Notas
    :param sit: True para mostrar situação, False para não mostrar
    :return: Retorna um dicionário com total de notas, maior nota, menor nota, media e situacao se True.
    """
    turma = dict()

    turma['total'] = len(n)
    turma['maior'] = max(n)
    turma['menor'] = min(n)
    turma['media'] = sum(n)/len(n)

    if sit:
        if turma['media'] >= 7:
            situacao = 'BOA'
        elif 7> turma['media'] >= 6:
            situacao = 'RAZOÁVEL'
        else:
            situacao = 'RUIM'

        turma['situacao'] = situacao

    return turma


r = notas(2, 1.5, 10, 9, 8.5, 7, sit=True)
print(r)
help(notas)