# Operadores lógicos = Avaliam várias condições (or, and, not)
#                      or = Checa se 1 condição é True
#                      and = Checa se ambas condições são True
#                      not = Inverte a condição (not False == True)

temp = 25
chovendo = False

if temp > 35 or temp < 0 or chovendo:
    print('Fique em casa hoje')
else:
    print('Está um lindo dia lá fora!')

print('-'*40)

temp = 5
ensolarado = False

if temp >= 30 and ensolarado:
    print('Está quente lá fora 🥵')
    print('E está ensolarado ☀️')
elif temp < 0 and ensolarado:
    print('Está frio lá fora 🥶')
    print('E está ensolarado ☀️')
elif 30 > temp > 0 and ensolarado:
    print('Está bom lá fora 🙂')
    print('E está ensolarado ☀️')
    
elif temp >= 30 and not ensolarado:
    print('Está quente lá fora 🥵')
    print('E está nublado ☁️')
elif temp < 0 and not ensolarado:
    print('Está frio lá fora 🥶')
    print('E está nublado ☁️')
elif 30 > temp > 0 and not ensolarado:
    print('Está bom lá fora 🙂')
    print('E está nublado ☁️')