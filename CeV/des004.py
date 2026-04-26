v = input("Digite algo: ")
print("É uma letra? {}\n"
      "É um número? {}\n"
      "É uma alfanúmerico? {}\n"
      "É decimal? {}\n"
      "É tudo mínusculo? {}\n"
      "É tudo maíusculo? {}\n"
      "Tipo primitivo: {}".format(v.isalpha(), v.isnumeric(), v.isalnum(),
                                    v.isdecimal(), v.islower(), v.isupper(), type(v)))
