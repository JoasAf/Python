# Rolar dados em python
from random import randint
dados_arte = {
            1: (    "┌─────────┐",
                    "│         │",
                    "│    ●    │",
                    "│         │",
                    "└─────────┘"),
                2: ("┌─────────┐",
                    "│  ●      │",
                    "│         │",
                    "│      ●  │",
                    "└─────────┘"),
                3: ("┌─────────┐",
                    "│  ●      │",
                    "│    ●    │",
                    "│      ●  │",
                    "└─────────┘"),
                4: ("┌─────────┐",
                    "│  ●   ●  │",
                    "│         │",
                    "│  ●   ●  │",
                    "└─────────┘"),
                5: ("┌─────────┐",
                    "│  ●   ●  │",
                    "│    ●    │",
                    "│  ●   ●  │",
                    "└─────────┘"),
                6: ("┌─────────┐",
                    "│  ●   ●  │",
                    "│  ●   ●  │",
                    "│  ●   ●  │",
                    "└─────────┘")}

dados = []

quant = int(input('Quantos dados?: '))
for valor in range(quant):
    dados.append(randint(1, 6))

for linha in range(5):
    for dado in dados:
        print(dados_arte[dado][linha], end='')
    print()

print(f'Total = {sum(dados)}')
