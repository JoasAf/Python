#           ┌───────────────────────────────────────────────────────────────────────┐
#           │ É um arquivo contendo um código que você quer incluir em seu programa │
# Módulo =  │ Use 'import' para incluir o modulo (já embutido ou seu próprio)       │
#           │ Útil para quebrar um grande programa em arquivos reusáveis separados  │
#           └───────────────────────────────────────────────────────────────────────┘

# print(help('modules'))
# print(help('math'))
# import math as matemática
from math import sqrt as raiz_quadrada

resultado = raiz_quadrada(9)

print(resultado)