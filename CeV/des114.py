import urllib
import urllib.request

try:
    site=urllib.request.urlopen('https://www.youtube.com/')
except urllib.request.URLError:
    print('O Youtube não está acessível no momento')
else:
    print('Consegui abrir o Youtube com sucesso!')