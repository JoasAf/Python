km = float(input("Quantos kms você vai viajar?: "))
if km<=200:
    p= km*0.5
    print("Sua viagem de {:.2f}km vai custar R${:.2f}".format(km, p))
else:
    p= km*0.45+10
    print("Sua viagem de {:.2f}km vai custar R${:.2f}".format(km, p))
