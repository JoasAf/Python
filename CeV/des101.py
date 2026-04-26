def voto(nasc):
    """
    ---> Verifica se uma pessoa tem idade suficiente para votar.

    :param nasc: Ano de nascimento da pessoa.
    :return: Retorna idade.
    """
    from datetime import date

    idade = date.today().year - nasc

    if 65 > idade >= 18:
        print(f'Com {idade} anos: Voto Obrigatório')

    elif idade < 16:
        print(f'Com {idade} anos: Não Vota')

    else:
        print(f'Com {idade} anos: Voto Opicional')



voto(int(input('Ano de nascimento: ')))