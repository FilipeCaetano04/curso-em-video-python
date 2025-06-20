import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com')
except:
    print('Não foi possível acessar o site do youtube!')
else:
    print('Foi possível acessar o site do youtube!')