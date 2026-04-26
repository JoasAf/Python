from math import hypot
c1 = float(input("Digite o comprimento do 1º cateto: "))
c2 = float(input("Digite o comprimento do 2º cateto: "))
# h = (c1**2+c2**2)**(1/2)
print("A hipotenusa é {}".format(hypot(c1, c2)))
