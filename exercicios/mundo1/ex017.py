#ler um comprimenro do cateto oposto e o cateto adjacente de um triangulo retangulo
#e mostrar o comprimento da hipotenusa
from math import hypot
c = float(input('Digite o valor do cateto opsto: '))
a = float(input('Digite o valor do cateto adjacente: '))
h = hypot(c,a)
print('A hipotenusa vai ser {:.2f}'.format(h))