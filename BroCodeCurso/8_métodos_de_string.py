nome = input('Seu nome: ').lower()

nome_len = len(nome)
nome_find = nome.find('a')
nome_rfind = nome.rfind('a')

nome_capitalize = nome.capitalize()
nome_upper = nome.upper()
nome_lower = nome.lower()

nome_isdigit = nome.isdigit()
nome_isalpha = nome.isalpha()

nome_count = nome.count('j')
nome_replace = nome.replace('j', 'g')

print(nome_len)
print(nome_find)
print(nome_rfind)
print(nome_capitalize)
print(nome_upper)
print(nome_lower)
print(nome_isdigit)
print(nome_isalpha)
print(nome_count)
print(nome_replace)
