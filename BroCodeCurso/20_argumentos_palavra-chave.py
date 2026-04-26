# Argumento palavras-chaves = É um argumento precedido de um identificador
#                             ajuda na legibilidade

def ola(saudações, primeiro_nome, último_nome):
    print(f'{saudações} {primeiro_nome} {último_nome}')


ola('Olá', último_nome='Franco', primeiro_nome='Joás')


def telefone(país, DDD, prim_4_núm, últ_4_núm):
    return f'+{país} {DDD} 9 {prim_4_núm}-{últ_4_núm}'

print(telefone(país=55, DDD=47, prim_4_núm=9712, últ_4_núm=5672))