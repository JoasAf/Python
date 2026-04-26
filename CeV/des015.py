d = int(input("Quantos dias ficou com o carro?:"))
km = float(input("Quantos quilômetros foram rodados?: "))
print("Dias usados: {} X R$60 = R${:.2f}\n"
      "Quilômetros rodados: {:.2f} X R$0,15 = R${:.2f}\n"
      "Total a pagar: R${:.2f}".format(d, d*60, km, km*0.15, d*60+km*0.15))
