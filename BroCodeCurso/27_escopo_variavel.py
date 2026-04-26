#                       ┌─────────────────────────────────────────┐
# Escopo de váriaveis = │ É onde a variável é visível e acessível │
#                       └─────────────────────────────────────────┘
#                       ┌──────────────────────────────────────────────────────────────────────┐
# Resolução de escopo = │ (LEGB) Local -> Fechada (enclosed) -> Global -> Inbutida (build-in)  │
#                       └──────────────────────────────────────────────────────────────────────┘

#                     ↓ esse 'x' é uma variável imbutida
from math import e as x


def func1():
    # ↓ esse 'x' é uma variável fechada
    # x = 1

    def func2():
        # ↓ esse 'x' é uma variável local
        # x = 2
        print(x)
    func2()

# ↓ esse 'x' é uma variável global
x = 3

func1()