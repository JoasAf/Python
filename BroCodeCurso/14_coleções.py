# Coleções = São "Variáveis" que conseguem armazenar vários valores
#       listas = [] Ordenadas, mutáveis. Valores duplos OK.
#       Conjuntos = {} Desordenados, imútaveis, mas Adicionar/Remover Ok. Sem valores duplos.
#       tuplas = () Ordenados, imútaveis. Valores duplos OK. Rápidos

# Listas
l_frutas = ['maça', 'laranja', 'banana', 'pêssego']

# print(dir(l_frutas))
# print(help(l_frutas))

l_frutas[1] = 'abacaxi'
l_frutas.append('coco')
l_frutas.remove('pêssego')
l_frutas.insert(2, 'kiwi')
l_frutas.sort()
l_frutas.reverse()

print(l_frutas)


# Conjunto
s_frutas = {'maça', 'laranja', 'banana', 'pêssego'}

# print(dir(l_frutas))
# print(help(l_frutas))

s_frutas.add('coco')
s_frutas.remove('banana')
s_frutas.pop()

print(s_frutas)


# Tuplas
t_frutas = ('maça', 'laranja', 'banana', 'pêssego')

# print(dir(l_frutas))
# print(help(l_frutas))


print(t_frutas)