# Despertador em python

import datetime as dt
import pygame as pg
from time import sleep

def definir_alarme(hora_alarme):
    print(f'Alarme ativado para as {hora_alarme}')
    som_alarme = 'projetos/17_alarme.mp3'

    while True:
        hora_atual = dt.datetime.now().strftime('%H:%M:%S')
        print(hora_atual)

        if hora_atual == hora_alarme:
            print('Hora de acordar 😩')
            pg.mixer.init()
            pg.mixer.music.load(som_alarme)
            pg.mixer.music.play()
            
            while pg.mixer.music.get_busy():
                sleep(1)
            break

        sleep(1)

if __name__ == '__main__':
    definir_alarme(input('Definir alarme (HH:MM:SS): '))