# Criptografia
import random as rd
import string as str

carac = ' ' +  str.punctuation + str.digits + str.ascii_letters
carac = list(carac)

chave = carac.copy()

rd.shuffle(chave)

palavra = input('Palavra: ')
encrip_palavra = ''

for letra in palavra:
    index = carac.index(letra)
    encrip_palavra += chave[index]

print(encrip_palavra)


encrip_palavra = input('Palavra: ')
palavra = ''

for letra in encrip_palavra:
    index = chave.index(letra)
    palavra += carac[index]

print(palavra)