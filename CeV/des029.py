v = float(input("Velocidade do Carro: "))
if v>83:
    m = (v-80)*7
    print("Você ultrapassou o limite de velocidade!")
    print("Será cobrada uma multa de R${:.2f} pelos {:.2f}km acima do limite!".format(m, v-80))

print("Tenha um bom dia e dirija com segurança.")
