from math import tan, cos, sin, radians
a = radians(float(input("Digite um ângulo: ")))
print("O seno é {:.2f},\n"
      "O cosseno é {:.2f}\n"
      "E a tangente é {:.2f}".format(sin(a), cos(a), tan(a)))
