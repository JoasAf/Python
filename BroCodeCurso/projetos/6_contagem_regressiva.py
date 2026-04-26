from time import sleep

tempo = int(input('Segundos: '))

for c in range(tempo, 0, -1):
    s = c % 60
    m = c//60%60
    h = c//3600
    print(f'{h:02}:{m:02}:{s:02}')
    sleep(1)

print('Acabou o tempo!')