# Exercício 8 dados de envio de produto

def dados_envio(*args, **kwargs):
    for arg in args:
        print(arg, end=' ')
    print()

    print(f'{kwargs.get("estado")}, {kwargs.get("cidade")}, {kwargs.get("bairro")}')
    print(f'{kwargs.get("rua")}, {kwargs.get("num")}')

dados_envio('Dr.', 'Joás', 'A.', 'Franco',
            estado='SC',
            cidade='Blumenau',
            bairro='Itoupava Norte',
            rua='Rua São Vicente',
            num=152)