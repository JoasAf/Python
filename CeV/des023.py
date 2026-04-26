num = int(input('Escolha um número de 0 a 9999: '))


print('Unidades: {}\n'
      'Dezenas: {}\n'
      'Centenas: {}\n'
      'Milhares: {}'.format(num%10,num//10-num//100*10,
                            num//100-num//1000*10,num//1000))
