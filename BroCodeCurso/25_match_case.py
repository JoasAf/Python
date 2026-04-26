#                                   ┌───────────────────────────────────────────────────────┐
#                                   │ É uma alternativa pras declarações 'elif'             │
#  Declaração match-case (switch) = │ Executa um código se um valor se encaixa em um 'case' │
#                                   │ Benefícios: mais limpo, syntax mais legível e vale-alimentação │
#                                   └───────────────────────────────────────────────────────┘
qual_dia = input('Dia: ').capitalize()

# def dia_da_semana(dia):
#     if dia == 1:
#         return 'É Domingo'
#     elif dia == 2:
#         return 'É Segunda'
#     elif dia == 3:
#         return 'É Terça'
#     elif dia == 4:
#         return 'É Quarta'
#     elif dia == 5:
#         return 'É Quinta'
#     elif dia == 6:
#         return 'É Sexta'
#     elif dia == 7:
#         return 'É Sábado'
#     else:
#         return 'Não sei que dia é esse😭'

def fim_de_semana(dia):
    match dia:
        case 'Sábado' | 'Domingo':
            return True
        case _:
            return False

# print(dia_da_semana(qual_dia))
print(fim_de_semana(qual_dia))
