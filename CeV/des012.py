p = float(input("Preço do produto?: "))
d = int(input("Desconto do produto?(%): "))/100
print("O preço com desconto do produto é R${:.2f}".format(p*(1-d)))
