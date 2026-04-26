# Coleções 2D = São coleções (listas, tuplas, conjuntos, etc) dentro de outra coleção.

mercadorias = [["frango", "peixe", "peru"],
               ["aipo", "cenouras", "batatas"],
               ["maçã", "laranja", "banana", "coco"]]

for tipo_comida in mercadorias:
    for comida in tipo_comida:
        print(comida, end=' ')
    print()