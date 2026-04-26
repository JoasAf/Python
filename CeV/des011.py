h = float(input("Qual é a altura da parede?(m): "))
w = float(input("Qual é a largura da parede?(m): "))
a = h*w
print("A área da parede é {:.0f}m², tendo {}m de altura e {}m de largura.\n"
      "É preciso de {:.2f} litros de tinta para pinta-lá".format(a, h, w, a/2))
