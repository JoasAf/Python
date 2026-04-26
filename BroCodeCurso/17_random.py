import random

baixo = 1
alto = 100
opções = ('pedra', 'papel', 'tesoura')
cartas = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# número = random.randint(baixo, alto)
# número = random.random()
# número = random.choice(opções)
random.shuffle(cartas)

print(cartas)