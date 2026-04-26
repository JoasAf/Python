alunos = []
quant = -1
while True:
    quant += 1
    sn = ' '
    alunos.append([])
    alunos[quant].append(input('Nome: '))
    alunos[quant].append(float(input('1ª Nota: ')))
    alunos[quant].append(float(input('2ª Nota: ')))
    alunos[quant].append((alunos[quant][1]+alunos[quant][2])/2)
    while sn not in 'SN':
        sn = input('Quer continuar? [S/N]: ').upper().strip()
    if sn == 'N':
        break

print('\33[1m_'*23)
print(f'\33[4m{'Nº':<5}{'NOME':<13}{'MÉDIA'}\33[0m')
for c in range(0, len(alunos)):
    print(f'{c+1:<4}{alunos[c][0]:<10}{alunos[c][3]:>8.1f}')
print('\33[1m_'*23)
print('\33[0m')
while True:
    sn = ' '
    aluno = int(input('Boletim: '))-1
    sit = ' '
    if alunos[aluno][3]>=7:
        sit = ' APROVADO'
    else:
        sit = 'REPROVADO'
    print(f'\33[4m{'NOME':10}{'1ªNOTA':8}{'2ªNOTA':8}{'MÉDIA'}{'SITUAÇÃO':>12}\33[0m')
    print(f'{alunos[aluno][0]:<10}{alunos[aluno][1]:<8.1f}{alunos[aluno][2]:<8.1f}'
          f'{alunos[aluno][3]:<8.1f}{sit:>}')
    while sn not in 'SN':
        print('\33[1m_'*41)
        sn = input('\33[0mVer boletim de algum aluno? [S/N]: ').upper().strip()
        if sn == 'N':
            break
    if sn == 'N':
        break
    print('\33[1m_'*23)
    print(f'\33[4m{'Nº':<5}{'NOME':<13}{'MÉDIA'}\33[0m')
    for c in range(0, len(alunos)):
        print(f'{c+1:<5}{alunos[c][0]:<13}{alunos[c][3]:.1f}')
    print('\33[1m_'*23)
    print('\33[0m')
