reta1=float(input('Insira o comprimento da 1º reta: '))
reta2=float(input('Insira o comprimento da 2º reta: '))
reta3=float(input('Insira o comprimento da 3º reta: '))
if reta1<reta2+reta3 and reta2<reta1+reta3 and reta3<reta1+reta2:
    print("É possível formar um triângulo com essas medidas")
else:
    print('É possível fazer um triângulo com essas medidas')
