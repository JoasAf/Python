from pygame import mixer
mixer.init()
mixer.music.load('des021 audio.mp3')
mixer.music.play()
x = input("Digite algo para parar: ")
